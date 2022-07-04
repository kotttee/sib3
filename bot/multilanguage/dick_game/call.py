from .languages.supporting_code import languages


async def get_text(lang_code, text_id, **kwargs):
    if kwargs:
        return languages[lang_code][text_id].format(**kwargs)
    return languages[lang_code][text_id]