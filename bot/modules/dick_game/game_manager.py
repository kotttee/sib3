import random
import time
import aiogram
from aiocache import SimpleMemoryCache
from bot.entities.chat import Chat
from bot.modules.dick_game.db.requests import get_user_data, set_user_data, register_mew_user
from bot.modules.dick_game.db.models import Dick_player
import datetime
from bot.multilanguage.lang_manager import get_text


async def start_game(message: aiogram.types.Message, cache: SimpleMemoryCache, chat: Chat, session_pool):
    player, s = await cache.get(f"DICK_GAME_PLAYER={str(message.chat.id) + str(message.from_user.id)}"), True
    if not player:
        player, s = await get_user_data(str(message.chat.id) + str(message.from_user.id), session_pool)
    if not s:
        return {"text": await get_text("dick_game", chat.lang, 3)}
    else:
        time_now: int = int(message.date.timestamp())
        profit = random.randint(chat.dick_game_range[0], chat.dick_game_range[1])
        if hasattr(player, "key"):
            await cache.set(f"DICK_GAME_PLAYER={str(message.chat.id) + str(message.from_user.id)}", player, chat.dick_game_timeout - 60 if chat.dick_game_timeout > 61 else 0)
            player.time_old = player.time
            if player.time + chat.dick_game_timeout < time_now:
                player.name = message.from_user.full_name
                player.size = player.size + profit
                player.time = time_now
                print(player.size)
                s = await set_user_data(player, session_pool)
                if not s:
                    return {"text": await get_text("dick_game", chat.lang, 3)}
                else:
                    if profit > -1:
                        return {"text": await get_text("dick_game", chat.lang, 2, prof=profit,
                                                       size=player.size)}
                    else:
                        return {"text": await get_text("dick_game", chat.lang, 2.1, prof=abs(profit),
                                                       size=player.size)}
            else:
                return {"text": await get_text("dick_game", chat.lang, 4, time=int(
                    (player.time_old + chat.dick_game_timeout - time_now) / 60))}
        else:
            profit_new_player = random.randint(0, 7)
            s = await register_mew_user(session_pool, message, profit_new_player)
            if not s:
                return {"text": await get_text("dick_game", chat.lang, 3)}
            return {"text": await get_text("dick_game", chat.lang, 1, size=profit_new_player)}


#оставил потому что тут кейс с использованием словаря
async def start_game_old_unused(message: aiogram.types.Message, cache: SimpleMemoryCache, chat: Chat, session_pool):
    game_data = await get_user_data(str(message.chat.id) + str(message.from_user.id), session_pool)
    profit = random.randint(chat.dick_game_range[0], chat.dick_game_range[1])
    time_now: int = int(message.date.timestamp())
    if hasattr(game_data['player'], "key"):
        if game_data['player'].time > time_now + chat.dick_game_timeout:
            game_data['player'].size = game_data['player'].size + profit
            game_data = game_data | await set_user_data(game_data['player'], session_pool)
            if not game_data['data_saved_successfully']:
                return {"text": await get_text("dick_game", chat.lang, 3)}
            if profit > -1:
                return {"text": await get_text("dick_game", chat.lang, 2, prof=profit,
                                               size=game_data['player'].size + profit)}
            else:
                return {"text": await get_text("dick_game", chat.lang, 2.1, prof=abs(profit),
                                               size=game_data['player'].size + profit)}
        else:
            return {"text": await get_text("dick_game", chat.lang, 4, time=int(
                (game_data['player'].time + chat.dick_game_timeout - time_now) / 60))}
    else:
        profit_new_player = random.randint(0, 7)
        game_data = game_data | await register_mew_user(session_pool, message, profit_new_player)
        if not game_data['new_user_registered_successfully']:
            return {"text": await get_text("dick_game", chat.lang, 3)}
        return {"text": await get_text("dick_game", chat.lang, 1, size=profit_new_player)}



