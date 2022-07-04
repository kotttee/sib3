from configparser import ConfigParser


parser = ConfigParser()
parser.read('bot.ini')


class Dick_game_module():
    def __init__(self):
        self.name = "dick_game"
        self.status = str(parser.get('dick_game', 'status'))
        self.languages = ["ru"]
        self.call_text = ["/dick", "/dick@sib_sis_bot"]

    async def recognize(self, text):
        if text in self.call_text:
            return True
        else:
            return False
