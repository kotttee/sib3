import asyncio

from aiogram import Router
from aiogram.types import Message
from aiogram import F, Bot

router = Router()

module_errors = {"in developing" : "sorry you can't use the module because it's still in development",
                 "disabled by the chat administrators" : "the module has been disabled by the chat administrators.\n/settings"}

language_errors = {"module not support chat language" : "sorry you can't use the module because module not support your chat language \nsettings"}


@router.message(F.text.startswith("%%module error"))
async def sib_s(message: Message, bot: Bot, queue: asyncio.Queue):
    await queue.put(bot.send_message(message.chat.id, module_errors[message.text[15:]], reply_to_message_id=message.message_id))


@router.message(F.text.startswith("%%language error"))
async def sib_s(message: Message, bot: Bot, queue: asyncio.Queue):
    print(1)
    await queue.put(bot.send_message(message.chat.id, language_errors[message.text[17:]], reply_to_message_id=message.message_id))