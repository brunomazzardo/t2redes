
from flask_socketio import emit

from .. import socketio


@socketio.on('make_play')
def make_play(message):
    pass


@socketio.on('connect')
def respond_to_request(message=None):
    emit('connection_result', {'success': True})
