import asyncio
from bot.entities.chat import Chat
from aiogram import Router
from aiogram.types import Message
from aiogram import F, Bot
from bot.modules.dick_game.call import dick
router = Router()


@router.message(commands=["dick"])
async def dick_game(message, bot, queue, cache, chat, session_pool):
    await dick(message, bot, queue, cache, chat, session_pool)