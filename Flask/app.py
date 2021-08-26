from flask import Flask, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    time_now = datetime.now().strftime("%H:%M:%S")
    menu = f'''
    Go <a href="{ url_for('dodawanie', a = 5, b = 3)}">here</a> to substract 5 and 3<br>
    Go <a href="{ url_for('another')}">here</a> to another tab<br>
    Go <a href="{ url_for('addition')}">here</a> to add custom numbers tab<br>
    '''

    return f'<h1>Hello World!: {time_now}</h1><br>{menu}'


@app.route('/dodawanie/<a>/<b>', methods =['POST'])
def dodawanie(a, b):
    a = int(a)
    b = int(b)
    wynik = str(a + b)
    return wynik


@app.route('/addition', methods =['GET', 'POST'])
def addition():

    if request.method == 'GET':
        body = f'''
            <form id="addition_form" action="{url_for("addition")}" method="POST">
                <label for="a">Liczba A</label>
                <input type="text" id="a" name='a' value="5"<br>
                <label for="b">Liczba B</label>
                <input type="text" id="a" name='b' value="4"<br>
                <input type="submit" value="Send">
            </form>
        '''
        return body
    else:
        a = "5"
        if "a" in request.form:
            a = request.form['a']

        b = "7"
        if "b" in request.form:
            b = request.form['b']
    body = f'{a} and {b} addition'
    return body


@app.route('/another')
def another():
    body = """
    <h1>Just another tab</h1>
    """
    return body


if __name__ == "__main__":
    app.run(host="0.0.0.0")
