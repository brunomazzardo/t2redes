from src.game.Game import Game


class GameManager:
    def __init__(self):
        self.games = []

    def list_games(self):
        return self.games

    def create_game(self):
        game = Game()
        self.games.append(game)


class GameManagerSingleton:
    game_manager = None

    @staticmethod
    def get_instance(self):
        if self.game_manager is None:
            self.game_manager = GameManager()
        return self.game_manager
