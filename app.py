from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "ID Delivery server работает!"

@app.route("/test")
def test():
    return jsonify({
        "status": "ok",
        "message": "Сервер готов"
    })

couriers = {}

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
