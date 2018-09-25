from src.game.GameManager import GameManager

game_manager = None


def GetGameManager():
    global game_manager
    if game_manager is None:
        game_manager = GameManager()
    return game_manager
