from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    time_now = datetime.now().strftime("%H:%M:%S")
    return '<h1>Hello World!: {}</h1>'.format(time_now)

if __name__== "__main__":
    app.run(host="0.0.0.0")
