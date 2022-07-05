from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, insert
from bot.modules.dick_game.db.models import Dick_player
import random
import aiogram


async def register_mew_user(session_pool, message: aiogram.types.Message, profit):
    try:
        async with session_pool() as session:
            player = Dick_player(key=str(message.chat.id) + str(message.from_user.id),
                                 size=profit, name=message.from_user.full_name,
                                 time=message.date.timestamp(), chat_id=message.chat.id,
                                 tlgr_id=message.from_user.id)
            session.add(player)
            await session.commit()
            return True
    except:
        # excepter.set("can`t register new user for dick_game")
        return None


async def set_user_data(player, session_pool):
        async with session_pool() as session:
            print(player.size)
            await session.execute(update(Dick_player).where(Dick_player.key == player.key).values({
                Dick_player.key: player.key,
                Dick_player.time: player.time,
                Dick_player.size: player.size,
                Dick_player.name: player.name,
                Dick_player.tlgr_id: player.tlgr_id,
                Dick_player.chat_id: player.chat_id, }))
            await session.commit()
            return True



async def get_user_data(key, session_pool): #excepter
    try:
        async with session_pool() as session:
            player = await session.execute(select(Dick_player).where(Dick_player.key == key))
            await session.commit()
            return player.scalars().first(), True
    except:
        # excepter.set("can`t receive user data for dick_game")
        return None, False
