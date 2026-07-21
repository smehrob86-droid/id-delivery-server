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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
