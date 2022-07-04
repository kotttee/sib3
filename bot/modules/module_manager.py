from bot.modules.talk.entity import Talk_module
from bot.modules.dick_game.entity import Dick_game_module
from bot.entities.chat import Chat

talk = Talk_module()
dick_game = Dick_game_module()

modules_list = [talk, dick_game]


async def filter(text):
    for i in modules_list:
        if await i.recognize(text):
            return i


async def available(chat: Chat, text, module):
    if module.status == "online":
        if chat.lang not in module.languages:
            return "%%language error module not support chat language"
        if module.name not in chat.allowed_modules:
            return "%%module error disabled by the chat administrators"
    else:
        return "%%module error " + module.status
