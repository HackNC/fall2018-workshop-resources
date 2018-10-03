from flask import Flask, request

app = Flask(__name__)

x = 0

@app.route("/")
def root():
    return "hello world"

@app.route("/show/")
def show():
    return "x is " + str(x)

@app.route("/incr/")
def incr():
    global x
    x = x + 1
    return "x is now " + str(x)

@app.route("/reset/")
def reset():
    global x
    x = 0
    return "x has been reset"

@app.route("/incr_by/<int:n>")
def incr_by(n):
    global x
    x = x + n
    return "x has been incremented by " + int(n)

@app.route("/form/")
def form():
    form_html = """
    <body>
        <form action="/form_endpt/" method='post'>
            <input name='n'>
            <button type='submit'>Submit</button>
        </form>
    </body>
    """
    return form_html

@app.route("/form_endpt/", methods = ['GET', 'POST'])
def handle_form():
    n = int(request.form['n'])
    global x
    x = x + n
    return "got form, incr by " + str(n)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
