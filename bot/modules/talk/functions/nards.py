import random


class Player:
    def __init__(self, key, chat_id, name, user_id, cache):
        self.cache = cache
        self.key = key
        self.chat_id = chat_id
        self.name = name
        self.user_id = user_id
        self.score = 100

    async def game(self, range: int, name):
        self.name = name
        profit = random.randint(-(int(range)), int(range)*2)
        if self.score < int(range):
            return {"text": "ты не можешь поставить больше чем у тебя есть"}
        if self.score + profit < 0:
            self.score = 100
            await self.cache.set(f"NARDS GAME USER={self.key}", self, 72000)
            await self.set_rate()
            return {'text': f"ты проигралл все. но я продал твою жопу и теперь у тебя 100 монет"}
        self.score += profit
        await self.cache.set(f"NARDS GAME USER={self.key}", self, 72000)
        await self.set_rate()
        return {'text': f"тебе выпало: {profit}, теперь у тебя - {self.score} монет"}

    async def set_rate(self):
        chat_rate = await self.cache.get(f"NARDS GAME CHAT RATE={self.chat_id}")
        if not chat_rate:
            chat_rate = {self.user_id: [self.score, self.name]}
            await self.cache.set(f"NARDS GAME CHAT RATE={self.chat_id}", chat_rate, 140000)
        else:
            chat_rate[self.user_id] = [self.score, self.name]
            await self.cache.set(f"NARDS GAME CHAT RATE={self.chat_id}", chat_rate, 140000)


async def get_rate(chat_id, cache):
    chat_rate = await cache.get(f"NARDS GAME CHAT RATE={chat_id}")
    if not chat_rate:
        return {"text" : "извини но в чате никто не играет по этому рейтинг недоступен"}
    else:
        chat_rate = dict(sorted(chat_rate.items(), key=lambda x: x[0]))
        result = ""
        place = 1
        for i in chat_rate.keys():
            result += f"{place}. <a href='tg://user?id={i}'>{chat_rate[i][1]}</a> - {chat_rate[i][0]} монет\n"
            place += 1
        return {"text" : result}


async def play(data):
    try:
        if data["args"] == "рейтинг":
            result = await get_rate(data["message"].chat.id, data["cache"])
            return result
        if data["args"] == "что это?":
            return {"text": "нарды это безпроигнрашаная игра. ты модешь играть в нее сколько хочешь но твои данные храняться только 20 часов. так что тебе нужно играть регулярно"}
        key = str(data['message'].chat.id) + str(data['message'].from_user.id)
        player = await data["cache"].get(f"NARDS GAME USER={key}")
        if not player:
            player = Player(key, data['message'].chat.id, data['message'].from_user.full_name, data['message'].from_user.id, data["cache"])
            await data["cache"].set(f"NARDS GAME USER={key}", player, 72000)
            return {"text": "ты вошел в игру нарды у тебя 100 монет"}
        result = await player.game(data["args"], data["message"].from_user.full_name)
        return result
    except:
        return {"text": "используй - сиб, нарды: цифра"}