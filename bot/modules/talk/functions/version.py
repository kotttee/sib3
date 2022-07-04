from configparser import ConfigParser
parser = ConfigParser()
parser.read('bot.ini')


async def version():
        try:
            return {"text" : parser.get('bot', 'version')}
        except:
            return {"text" : "извини произошла ошибка. попробуй через пару минут"}