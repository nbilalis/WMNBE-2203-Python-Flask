from flask import Flask
from os import environ
from markupsafe import escape
from math import pi

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <h1>Hello World!</h1>
    '''


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='World'):
    return f'Hello, {escape(name)}!'


@app.route('/product/<int:id>')
def product_details(id):
    return f'Product #{id}'


@app.route('/download/<path:path>')
def download_file(path):
    return f'Downloading file @ {path}'


@app.route('/circle/<float:r>')
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
