import flask
from application import APPLICATION

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "hello"


@app.route("/api/v1/models", methods=["GET"])
def models():
    return APPLICATION.list_models()


@app.route("/api/v1/models/<model_id>", methods=["DELETE"])
def model_delete(model_id):
    return "hello"


@app.route("/api/v1/models/<model_id>", methods=["PUT"])
def model_update(model_id):
    return "hello"


@app.route("/api/v1/tools/<tool_id>", methods=["DELETE"])
def tool_delete(tool_id):
    return "hello"


@app.route("/api/v1/tools/<tool_id>", methods=["PUT"])
def tool_update(tool_id):
    return "hello"


@app.route("/api/v1/tools", methods=["GET"])
def tools():
    return "hello"


@app.route("/api/v1/chat/completions", methods=["POST"])
def chat_completions():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
