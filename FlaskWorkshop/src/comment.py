from flask import Flask, request

app = Flask(__name__)

comment_block = ""
form_html = """
        <form action="/form_endpt/" method='post'>
            Username: <input name="username">
            Comment: <input name="comment">
            <button type='submit'>Comment</button>
        </form>
    """


@app.route("/")
def root():
    return "<body>" + comment_block + "<br>" + form_html + "</body>"

@app.route("/form_endpt/", methods = ['GET', 'POST'])
def handle_form():
    username = request.form['username']
    comment = request.form['comment']
    global comment_block
    comment_block += '<p><b>%s</b>: %s</p>' % (username, comment)
    return '<p>Your comment has been posted, go <a href="/">home</a></p>'


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
