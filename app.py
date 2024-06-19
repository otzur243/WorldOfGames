from flask import Flask

import MainScores

app = Flask(__name__)


@app.route("/")
def score_page():
    return MainScores.score_server()


if __name__ == '__main__':
    app.run()
