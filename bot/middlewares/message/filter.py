from typing import Callable, Awaitable, Dict, Any
from aiogram import F
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
import re
from bot.modules.talk.entity import Talk_module
from bot.modules.module_manager import filter
talk = Talk_module()



class FilterMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        module = await filter(re.sub("@sib_sis_bot", "", data['event_update'].message.text))
        if module:
            data["module"] = module
            return await handler(event, data)
