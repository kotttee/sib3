import asyncio
import aiogram
from bot.modules.talk import supporting_code, main, dicts


#эта функция принимает текст сообщение и пытается определить что от нее хотят
async def dialog(message: aiogram.types.Message, bot: aiogram.Bot, queue: asyncio.Queue, cache):
    result = {"text" : "прости я еще не могу отвечать на это", "keyboard" : None}; call = {"args" : None, "cache" : cache}
    call = call | await supporting_code.format_text(message.text[5:])
    if call["text"] in dicts.answers_simple.keys():
        result["text"] = dicts.answers_simple[call["text"]]

    elif call["text"] in dicts.answers_interactive.keys():
       result = result | await main.call_function(dicts.answers_interactive[call["text"]], call)

    else:
        result = result | await supporting_code.prompting(call["text"])

    await queue.put(bot.send_message(message.chat.id, text=result["text"], reply_markup=result["keyboard"], disable_web_page_preview=True, reply_to_message_id=message.message_id))
