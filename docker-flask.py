from flask import Flask

docker_app = Flask(__name__)

@docker_app.route("/", methods=["GET", "POST"])
def hello_flask():
    return "success"

docker_app.run(debug=True, host="0.0.0.0")