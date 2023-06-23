from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'app1'

if __name__ == '__main__':
    app.debug = True
    app.run()