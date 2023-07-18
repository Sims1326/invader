class Stats:

    def __init__(self, game):
        self.settings = game.settings
        self.reset()

    def reset(self):
        self.lives_left = self.settings.lives
