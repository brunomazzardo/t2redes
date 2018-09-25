from .. import socketio


def game_started(token):
    socketio.emit(token + '/game_started', "Game Started", callback=ack)


def update_game(token, game_update):
    socketio.emit(token + '/update_game', game_update, callback=ack)


def ack():
    print('message was received!')
