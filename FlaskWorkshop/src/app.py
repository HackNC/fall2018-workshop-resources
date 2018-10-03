from flask import Flask

app = Flask(__name__)

x = 0

@app.route("/")
def root():
    return "hello world"

@app.route("/show/")
def show():
    return "x is " + str(x)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
