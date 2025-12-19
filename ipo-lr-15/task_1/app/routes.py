from flask import request, jsonify
from app import app


@app.route('/')
def main_page():
    return "Простейший Flask-сервис запущен."


@app.route('/hello/<username>')
def say_hello(username):
    return f"Здравствуйте, {username}!"


@app.route('/square/<int:value>')
def get_square(value):
    square_value = value * value
    return f"Квадрат числа {value} равен {square_value}"


@app.route('/json', methods=['POST'])
def process_json():
    user_data = request.get_json()

    if user_data is None:
        return jsonify({"error": "Данные должны быть переданы в формате JSON"}), 400

    if 'name' not in user_data or 'age' not in user_data:
        return jsonify({"error": "Отсутствуют обязательные поля name или age"}), 400

    name = user_data['name']
    age = user_data['age']

    try:
        age = int(age)
    except ValueError:
        return jsonify({"error": "Возраст должен быть числом"}), 400

    text = f"Пользователя зовут {name}, ему {age} лет."
    return jsonify({"result": text})


@app.route('/multiply/<a>/<b>')
def multiply_numbers(a, b):
    try:
        first = float(a)
        second = float(b)
    except ValueError:
        return jsonify({"error": "В параметры должны передаваться числа"}), 400

    multiplication = first * second

    return jsonify({
        "first_number": first,
        "second_number": second,
        "result": multiplication
    })
