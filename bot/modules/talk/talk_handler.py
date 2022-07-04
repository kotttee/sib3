import asyncio
from bot.entities.chat import Chat
from aiogram import Router
from aiogram.types import Message
from aiogram import F, Bot
from bot.modules.talk.call import dialog
router = Router()


@router.message(commands=["sss"])
async def start(message: Message, bot: Bot, queue: asyncio.Queue, chat: Chat):
    await queue.put(bot.send_message(message.chat.id,"lox"))


@router.message(F.text.lower().in_({"сиб", "си сиб"}))
async def sib_s(message: Message, bot: Bot, queue: asyncio.Queue):
    await queue.put(bot.send_message(message.chat.id, "си сис"))


@router.message(F.text.lower().startswith("сиб, "))
async def sib(message, bot, queue, cache):
    await dialog(message, bot, queue, cache)
