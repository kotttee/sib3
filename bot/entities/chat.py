class Chat():
    def __init__(self, id, lang):
        self.id = id
        self.lang = lang
        self.allowed_modules = ["talk", "dick_game"] #и это
        self.dick_game_timeout = 36000 # и это тоже
        self.dick_game_range = [-10, 10] # сделать это изменяемым