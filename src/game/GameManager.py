from src.game.Game import Game


class GameManager:
    def __init__(self):
        self.games = []

    def list_games(self):
        return [_.to_json() for _ in self.games]

    def create_game(self, player):
        game = Game(player)
        self.games.append(game)
        return game.to_json()

    def join_game(self, player, game_id):
        for game in self.games:
            if game.id == game_id:
                game.second_player = player
                return game.id
        return None

    def make_play(self, game_id, square_number, player):
        for game in self.games:
            if game.id == game_id:
                return game.make_play(square_number, player)
        return None
