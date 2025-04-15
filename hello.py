from flask import Flask

app = Flask(__name__)

db_url = 'postgres://u71tjn7urbb255:pf8cbeacf614de01f5f9c1f3a6e4b04eca424c680723cec5bd98b689664376179@c5p86clmevrg5s.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dt7786muekh2d'

@app.route('/')
def hello():
    return 'Hello World!'