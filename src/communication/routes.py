import jwt
from flask import request, jsonify
from src.communication import main
from src.game.GameManager import GameManagerSingleton

game_manager = GameManagerSingleton.get_instance()


@main.route('/list_games')
def list_agents():
    return jsonify(game_manager.list_games())


@main.route('/create_game')
def create_game():
    pass


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
