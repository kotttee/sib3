from bot.multilanguage.base import call as call_base
from bot.multilanguage.dick_game import call as call_dick_game


async def get_text(module, lang_code, text_id, **kwargs):
    if module == "base":
        return await call_base.get_text(lang_code, text_id, **kwargs)
    elif module == "dick_game":
        return await call_dick_game.get_text(lang_code, text_id, **kwargs)
    else:
        return "sorry error"
