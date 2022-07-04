from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from bot.base.chat.language.manager import get_language
from bot.entities.chat import Chat
from bot.modules.module_manager import available


class BasicMiddleware(BaseMiddleware):
    def __init__(self, cache, session_pool, queue):
        super().__init__()
        self.queue = queue
        self.cache = cache
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
            #print(data["event_chat"].id)
            async with self.session_pool() as session:
                lang = await get_language(data["event_chat"].id, session, self.cache)
            chat = Chat(data['event_update'].message.chat.id, lang)
            error_text = await available(chat, data['event_update'].message.text, data["module"])
            data["queue"] = self.queue
            if error_text:
                data['event_update'].message.text = error_text
                return await handler(event, data)
            data['session_pool'] = self.session_pool
            data["chat"], data['cache'] = chat, self.cache
            return await handler(event, data)