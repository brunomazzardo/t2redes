from collections import namedtuple

from flask_socketio import emit

from src.communication.emiters import update_game, turn_second, turn_owner
from src.game.GameManagerSingleton import GetGameManager
from .. import socketio

game_manager = GetGameManager()


@socketio.on('make_play')
def make_play(json):
    play_request = namedtuple("request_connection", json.keys())(*json.values())
    game_update = game_manager.make_play(play_request.id, play_request.numero_quadrado, play_request.player)
    if game_update is not None:
        update_game(play_request.id, game_update)
        if int(play_request.player) == 1:
            turn_second(play_request.id)
        else:
            turn_owner(play_request.id)


@socketio.on('connect')
def respond_to_request(message=None):
    emit('connection_result', {'success': True})
