from flask import Flask

app = Flask(__name__)


@app.route('/')
def index() -> None:
    return 'Raj IT Hacks 2.0'

if __name__ == '__main__':
    app.run()