from flask import Flask
print("Hello World")

app = Flask("docker-hello-flask")
@app.route("/")
def hello():
    return "Success"


def main():
    app.run()


if __name__ == "__main__":
    main()