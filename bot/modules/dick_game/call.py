import asyncio
import aiogram
from bot.entities.chat import Chat
from .game_manager import start_game


async def dick (message: aiogram.types.Message, bot: aiogram.Bot, queue: asyncio.Queue, cache, chat: Chat, session):
    result = {"text" : "sorry, error", "keyboard" : None}; call = {"args" : None, "cache" : cache}
    result = result | await start_game(message, cache, chat, session)
    await queue.put(bot.send_message(message.chat.id, text=result["text"], reply_markup=result["keyboard"], disable_web_page_preview=True, reply_to_message_id=message.message_id))
