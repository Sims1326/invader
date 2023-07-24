
class Stats:

    def __init__(self, game):
        self.settings = game.settings
        self.high_score = 0
        self.reset()

    def reset(self):
        self.points = 0
        self.settings.default_settings()
