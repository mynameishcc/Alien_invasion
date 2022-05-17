import os

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        try:
            cur_path = os.path.abspath(os.path.dirname(__file__))
            cur_path.replace('\\', '/')
            with open(cur_path+ '/high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1