import requests
from bs4 import BeautifulSoup
import requests
from configparser import ConfigParser
parser = ConfigParser()
parser.read('bot.ini')
from aiocache import SimpleMemoryCache


async def weather_req(city_name):
    try:
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                         params={'q': city_name["args"], 'type': 'like', 'units': 'metric', 'APPID': parser.get('weather', 'APIkey')})
        except:
            print("гавно не могу к поиску городов подключиться")
            return "извини не могу подключиться к серверу поиска городов. попробуй через папру минут"
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        city_id = data['list'][0]['id']
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': parser.get('weather', 'APIkey')})
        except BaseException as e:
            print("гавно не могу погоду спиздить", e)
            return "извини не могу подключиться к серверу погоды. попробуй через папру минут"
        data = res.json()
        return f"в городе: {data['name']}, {data['sys']['country']} - {data['weather'][0]['description']}\n\nтемпература: \
{round(data['main']['temp'])}°C\nчувствуется как: {round(data['main']['feels_like'])}°\nC сегодня температура\
 от {round(data['main']['temp_min'])} до {round(data['main']['temp_max'])} °C\nвлажность: {data['main']['humidity']}%\nскорость ветра: {data['wind']['speed']} км\ч"
    except IndexError:
        return "прости не удалось найти твой город. попробуй написать его английскими буквами."
    except BaseException as e:
        print("ошибка в погоде:", e)
        return "извини сейчас я не могу сказать тебе погоду. попробуй через папру минут"


async def get_weather(data):
        try:
            cache: SimpleMemoryCache = data["cache"]
            cached: str = await cache.get(data["args"])
            if cached:
                return {"text": cached}
            if data["args"] is None:
                return {"text": "Используй пожалуйста - \nсиб, погода: город"}
            weather = await weather_req(data)
            await cache.set(data["args"], weather, 300)
            return {"text" : weather}
        except:
            return {"text" : "извини произошла ошибка. попробуй через пару минут"}