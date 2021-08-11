from flask import Flask, render_template
from flask_clickhouse import ClickHouse

app = Flask(__name__)
ch = ClickHouse(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
