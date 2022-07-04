import asyncio
from bot.multilanguage import lang_manager
from aiogram import Router
from aiogram.types import Message
from aiogram import F, Bot
from bot.entities.chat import Chat

router = Router()


@router.message(commands=["start"])
async def start(message: Message, bot: Bot, queue: asyncio.Queue, chat: Chat):
    await queue.put(bot.send_message(message.chat.id, await lang_manager.get_text("base", chat.lang, 1)))


@router.message(commands=["chat_info"])
async def start(message: Message, bot: Bot, queue: asyncio.Queue, chat: Chat):
    await queue.put(bot.send_message(message.chat.id, await lang_manager.get_text("base", chat.lang, 2, lang = chat.lang)))