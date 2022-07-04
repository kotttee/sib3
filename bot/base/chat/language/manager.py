from sqlalchemy.ext.asyncio import AsyncSession
from aiocache import SimpleMemoryCache
from bot.base.chat.model import Chat
from sqlalchemy import select



async def get_language(chat_id, session:AsyncSession, cache: SimpleMemoryCache):
        cached = await cache.get(f"LANGUAGE {chat_id}")
        if cached:
                return cached
        try:
                lang = await session.execute(select(Chat.lang).where(Chat.id == chat_id))
        except:
                lang = "ru"
        await cache.set(f"LANGUAGE {chat_id}", lang, 43200)
        return lang