from bs4 import BeautifulSoup
import requests
from aiocache import SimpleMemoryCache



async def news_tsn():
    try:
        filteredNews = {"status" : "success"}
        url = 'https://tsn.ua/news'
        try:
            page = requests.get(url)
        except BaseException as e:
            print("не могу подключиться тсн", e)
            return {"status": "connect error"}
        soup = BeautifulSoup(page.text, "html.parser")
        allNews = soup.findAll('a', class_='c-card__link')
        for data in allNews:
            data = str(data).replace('"', "")
            filteredNews[(str(data).split('>')[1])[:-3]] = (str(data).split('href=')[1]).split('>')[0]
      
        else:
            return filteredNews
    except BaseException as e:
        print("тут парсер говна поел чекни: ",e)
        return {"status" : "error"}


async def news(data):
    cache: SimpleMemoryCache = data["cache"]
    cached: str = await cache.get("NEWS TSN")
    if cached:
        return {"text": cached}
    result = await news_tsn()
    if result["status"] == "connect error":
        return {"text": "извини, не могу подключиться к серверу ТСН"}
    elif result["status"] == "error":
        return {"text": "извини, извини ошибка с новостями"}
    else:
        text = "вот твои новости)\n\n"
        del result["status"]
        for i in result.keys():
            text = text + f'<a href = "{result[i]}">{i}</a>\n\n'
        await cache.set("NEWS TSN", text, 600)
        return {"text": text}

