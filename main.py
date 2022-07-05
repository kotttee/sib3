import asyncio
import logging
from configparser import ConfigParser
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.handlers import base
from bot.handlers import errors_handler
from bot.modules.talk import talk_handler
from bot.modules.dick_game import dick_game_handler
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from bot.middlewares.base import BasicMiddleware
from bot.middlewares.message.filter import FilterMiddleware


from aiocache import Cache


parser = ConfigParser()
parser.read('bot.ini')


async def main():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    engine = create_async_engine(
        f"postgresql+asyncpg://{parser.get('db', 'username')}:{parser.get('db', 'password')}@127.0.0.1:5432/sib",
        echo=False,
    )
    cache = Cache(Cache.MEMORY)
    queue = asyncio.Queue()
    db_pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    bot = Bot(token=parser.get('bot', 'token'), parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.outer_middleware(FilterMiddleware())
    dp.message.outer_middleware(BasicMiddleware(cache, db_pool, queue))
    dp.include_router(dick_game_handler.router)
    dp.include_router(talk_handler.router)
    dp.include_router(errors_handler.router)
    dp.include_router(base.router)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send, 'interval', [queue], seconds=0.4)
    scheduler.start()
    await dp.start_polling(bot)


async def send(queue: asyncio.Queue):
    if not queue.empty():
        task = await queue.get()
        await task
        queue.task_done()

asyncio.run(main())









