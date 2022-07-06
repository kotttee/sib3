import re

# значит этот словарь просто словарь можете даже не смотреть на него


#эта функция форматирует текст в 0 если приходит: "сиб, рандом: 3 8" выводит - "рандом" то есть само название функции
async def format_text(text):
    obj = (str(text)).split(":")[0]
    obj = obj.replace("]", "").replace("[", "").replace(" ", "")
    obgret = re.sub("[),(#*;?:'.]", "", obj)
    try:
        args = str(text).split(":")[1]
        if str(text).split(":")[1][0] == " ":
            args = str(text).split(":")[1][1:]
    except:
        args = None
    return {"text" : obgret.lower(), "args" : args}



#это подсказки на минималках
async def prompting(text):
    if re.search("погода", text):
        return {"text" : "Возможно ты имел ввиду:\nсиб, погода: город"}
    if re.search("нового", text) or re.search("новости", text):
        return {"text" :  "Возможно ты имел ввиду:\nсиб, что нового?"}
    if re.search("рандом", text):
        return {"text" :  "Возможно ты имел ввиду:\nсиб, рандом: [от] [до]\nпример - сиб, рандом: 2 30"}
    if re.search("нарды", text):
        return {"text" :  "Возможно ты имел ввиду:\nсиб, нарды: [число]\nпример - сиб, нарды: 30"}
    else:
        return {}

