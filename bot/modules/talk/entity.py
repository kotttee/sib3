from configparser import ConfigParser

parser = ConfigParser()
parser.read('bot.ini')


class Talk_module():
    def __init__(self):
        self.name = "talk"
        self.status = str(parser.get('talk', 'status'))
        self.languages = ["ru"]
        self.call_text = ["сиб, "]

    async def recognize(self, text):
        if text.lower()[:5] in self.call_text:
            return True
        else:
            return False
