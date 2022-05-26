import locale

from flask import Flask, render_template, abort
from os import environ

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/hello/')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', user=username)


@app.route('/products/')
def product_list():
    products = get_products()
    return render_template('products/list.html', products=products)


@app.route('/products/<sku>')
def product_details(sku):
    products = get_products()
    product = products.get(sku, None)
    app.logger.debug('product: %s', product)

    if product is not None:
        return render_template('products/details.html', product=product)
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug(e)
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404


@app.template_filter('currency')
def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'el_GR')
    return locale.currency(value, symbol=True, grouping=True)

# filters.FILTERS["format_currency"] = currency


if __name__ == '__main__':
    app.run(host='localhost', port=environ.get('SERVER_PORT', 5000), debug=True)


def get_products():
    return {
        '0001': {'sku': '0001', 'title': 'Awesome Product #1', 'description': 'Blah blah. ' * 50, 'price': 2.34},
        '0002': {'sku': '0002', 'title': 'Awesome Product #2', 'description': 'Blah blah. ' * 50, 'price': 3.45},
        '0003': {'sku': '0003', 'title': 'Awesome Product #3', 'description': 'Blah blah. ' * 50, 'price': 4.56},
    }
