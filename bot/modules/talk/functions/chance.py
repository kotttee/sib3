import random as rand


async def chance(data):
    try:

        return {"text": "шанс " + str(data["args"]) + " - " + str(rand.randint(1, 100)) + "%"}
    except:
        return {"text": "Используй правильно, пример: \n\"сиб, шанс: того что сегодня будет дождь\""}

