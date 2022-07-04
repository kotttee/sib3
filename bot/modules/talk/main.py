from bot.modules.talk.functions import version, chance, weather, rand, choose, news


# вот это позорище полное

# тут я вызываю функции и передаю им дату
async def call_function(id: int, data: dict) -> dict:
    match id:
        case 1:
            result = await news.news(data)
            return result
        case 2:
            result = await rand.random(data)
            return result
        case 3:
            result = await weather.get_weather(data)
            return result
        case 4:
            result = await version.version()
            return result
        case 5:
            result = await choose.oder(data)
            return result
        case 6:
            result = await chance.chance(data)
            return result
