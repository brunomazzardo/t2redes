from .. import socketio


def game_started(token):
    socketio.emit(token + '/game_started', "Game Started", callback=ack)


def update_game(token, game_update):
    socketio.emit(token + '/update_game', game_update, callback=ack)


def turn_owner(token):
    socketio.emit(token + '/1', "Turn Started", callback=ack)


def turn_second(token):
    socketio.emit(token + '/2', "Turn Started", callback=ack)


def ack():
    print('message was received!')
