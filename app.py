from flask import Flask, jsonify, request

app = Flask(__name__)


# Главная страница
@app.route("/")
def home():
    return "ID Delivery server работает!"


# Проверка сервера
@app.route("/test")
def test():
    return jsonify({
        "status": "ok",
        "message": "Сервер готов"
    })


# Курьеры
couriers = {}


# Регистрация курьера
@app.route("/courier/register", methods=["POST"])
def register_courier():
    data = request.json

    courier_id = str(data["id"])

    couriers[courier_id] = {
        "name": data.get("name"),
        "phone": data.get("phone"),
        "status": "offline"
    }

    return jsonify({
        "message": "Курьер зарегистрирован"
    })


# Изменение статуса курьера
@app.route("/courier/status", methods=["POST"])
def courier_status():
    data = request.json

    courier_id = str(data["id"])

    if courier_id in couriers:
        couriers[courier_id]["status"] = data["status"]

        return jsonify({
            "message": "Статус изменён"
        })

    return jsonify({
        "error": "Курьер не найден"
    }), 404


# Заказы
orders = []


# Создание заказа
@app.route("/order/create", methods=["POST"])
def create_order():
    data = request.json

    order = {
        "id": len(orders) + 1,
        "client": data.get("client"),
        "address": data.get("address"),
        "status": "new"
    }

    orders.append(order)

    return jsonify(order)


# Запуск сервера
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
