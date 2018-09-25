import jwt
from flask import request, jsonify, json
from src.communication import main
from src.communication.emiters import game_started
from src.game.GameManagerSingleton import GetGameManager
from collections import namedtuple

game_manager = GetGameManager()


@main.route('/list_games')
def list_agents():
    return json.dumps(game_manager.list_games(), for_json=True)


@main.route('/create_game', methods=['POST'])
def create_game():
    player = request.get_json()
    return json.dumps(game_manager.create_game(player))


@main.route('/join_game', methods=['POST'])
def connect_to_game():
    join_request = request.get_json()
    d_named = namedtuple("request_connection", join_request.keys())(*join_request.values())
    game_connection = game_manager.join_game(d_named.id, d_named.player)
    if game_connection is not None:
        game_started(game_connection)
        return "Começou"
    else:
        return "Não encontrado"


@main.route('/requestConnection', methods=['POST'])
def connect():
    agent = request.get_json()
    print(agent)
    encoded = jwt.encode(agent, 'secret', algorithm='HS256')
    response = {
        "encoded": encoded.decode('utf-8'),
        "ip": '127.0.0.1',
        "port": 5000
    }
    return jsonify(response)
