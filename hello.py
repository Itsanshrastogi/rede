# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect("https://tringcoin.com/", code=302)

if __name__ == '__main__':
    app.run()

