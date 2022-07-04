import random as rand


async def oder(data):
    try:
        arg1 = data["args"].split('или')[0]
        arg2 = data["args"].split('или')[1]
        numb = rand.randint(1, 1000)
        if numb % 2 == 0:
            return {"text" : arg2}
        else:
            return {"text": arg1}
    except:
        return {"text": "Укажи 2 опции, пример: \n\"сиб, выбери: покушать или погулять\""}

