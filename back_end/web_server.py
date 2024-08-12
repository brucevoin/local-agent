from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import json
from application.service import APPLICATION

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on("connect")
def connect():
    print("Client connected")
    emit("response", {"data": "Connected"})


@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")


@socketio.on("message")
def handle_message(message):
    print("Received message: " + message)
    emit("response", message, broadcast=True)


@app.route("/")
def index():
    return "hello"


@app.route("/api/v1/models", methods=["GET"])
def models():
    models = APPLICATION.list_models()
    return jsonify({"data": models})


@app.route("/api/v1/models/<model_id>", methods=["DELETE"])
def model_delete(model_id):
    APPLICATION.delete_model(model_id)


@app.route("/api/v1/models", methods=["PUT"])
def model_update():
    data = request.json
    APPLICATION.update_model(data)


@app.route("/api/v1/models", methods=["POST"])
def model_create():
    data = request.json
    print(data)
    APPLICATION.create_model(data)
    return jsonify({"data": "ok"})


@app.route("/api/v1/tools/<tool_id>", methods=["DELETE"])
def tool_delete(tool_id):
    APPLICATION.delete_tool(tool_id)


@app.route("/api/v1/tools", methods=["PUT"])
def tool_update():
    data = request.json
    APPLICATION.update_tools(data)


@app.route("/api/v1/tools", methods=["GET"])
def tools():
    tools = APPLICATION.list_models()
    return jsonify({"data": tools})


@app.route("/api/v1/chat/completions", methods=["POST"])
def chat_completions():
    data = request.json
    res = APPLICATION.run(
        data["message"],
        data["models"],
        data["tools"],
        data["tempreture"],
        data["max_consecutive_replay"],
    )
    return jsonify({"data": res})


if __name__ == "__main__":
    APPLICATION.init()
    #app.run(host="0.0.0.0", port=5000)
    socketio.run(app, host="0.0.0.0", port=5000)
