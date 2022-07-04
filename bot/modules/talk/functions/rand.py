import random as rand


async def random(data):
    try:
        n1 = int(str(data["args"]).split()[0])
        n2 = int(str(data["args"]).split()[1])
        return {"text": rand.randint(n1, n2)}
    except:
        return {"text": "Укажи 2 числа, пример: \"сиб, рандом: 2 8\""}

