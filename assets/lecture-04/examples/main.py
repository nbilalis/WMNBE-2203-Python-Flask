from flask import Flask
from math import pi
from os import environ

app = Flask(__name__)


@app.route('/')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name='World'):
    return f'''
    <html>
        <head>
            <title>Hello, {name.capitalize()}!</title>
        </head>
        <body>
            <h1>Hello, {name.capitalize()}!</h1>
        </body>
    </html>
    '''


@app.route('/circle/<int:r>')
def circle(r):
    circumference = 2 * pi * r
    area = pi * r ** 2
    return f'circumference: {circumference:.2f}, area: {area:.2f}'


@app.route('/words/<phrase>')
def words(phrase):
    lst = phrase.split(' ')
    return '<br>'.join(lst)


@app.route('/normalize/<input>')
def normalize(input):
    """
    The function performs the following conversion:
    '  $12,345,678.90  ' -> '€12.345.678,90'
    """

    # Strip spaces
    input = input.strip()
    # Split input with ',', leaving out the currency symbol
    lst = input[1:].split(',')
    # Replace the decimal point, only in the last list item
    lst[-1] = lst[-1].replace('.', ',')

    return f"€{'.'.join(lst)}"


if __name__ == '__main__':
    app.run(host='localhost', port=environ.get('SERVER_PORT', 5000), debug=True)
