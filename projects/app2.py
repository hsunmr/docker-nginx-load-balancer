from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'app2'

if __name__ == '__main__':
    app.debug = True
    app.run()