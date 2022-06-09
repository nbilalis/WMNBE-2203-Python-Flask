import re
import locale
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from datetime import datetime, timedelta
from os import environ

from products_service import get_product, get_products

app = Flask(__name__)

# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = environ.get('SECRET_KEY', b'_5#y2L"F4Q8z\n\xec]/')
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=3)


@app.before_request
def make_session_permanent():
    session.permanent = True

    if 'timestamp' not in session:
        session['timestamp'] = datetime.now()


@app.get('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session.get('username'))
    else:
        return render_template('home.html')


@app.get('/search')
def search_products():
    q = request.args.get('q', '').strip()

    q = q if len(q) > 0 else None
    products = get_products(q) if q else []

    return render_template('search.html', q=q, products=products)


@app.get('/product/<id>')
def product_details(id):
    product = get_product(id)

    if product is None:
        abort(404)

    return render_template('product.html', product=product)


@app.get('/register')
def register_form():
    return render_template('register.html')


@app.post('/register')
def register_user():
    username = request.form.get('username')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')

    app.logger.debug(username)
    app.logger.debug(firstname)
    app.logger.debug(lastname)

    errors = []

    if not username:
        errors.append({'field': 'username', 'msg': 'Username is required.'})
    elif re.search(r'^\w{3,8}$', username) is None:
        errors.append({
            'field': 'username',
            'msg': 'Username must include only latin chars, digits and _, and should be 3-8 characters long.'
        })

    if not firstname:
        errors.append({'field': 'firstname', 'msg': 'Firstname is required.'})
    elif len(firstname) < 3:
        errors.append({'field': 'firstname', 'msg': 'Firstname should be at least 3 chars long.'})

    if not lastname:
        errors.append({'field': 'lastname', 'msg': 'Lastname is required.'})
    elif len(lastname) < 3:
        errors.append({'field': 'lastname', 'msg': 'Lastname should be at least 3 chars long.'})

    app.logger.debug(errors)

    if (len(errors)):
        return render_template('register.html',
                               username=username,
                               firstname=firstname,
                               lastname=lastname,
                               errors=errors)
    else:
        session['username'] = username
        flash('Thank you for registering!')
        return redirect(url_for('home'))


@app.get('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug(dir(e))
    return render_template('errors/404.html', e=e), 404


@app.template_filter('currency')
def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'el_GR')
    return locale.currency(value, symbol=True, grouping=True)


# filters.FILTERS['format_currency'] = format_currency

if __name__ == '__main__':
    app.run(host='localhost', port=environ.get('SERVER_PORT', 5000), debug=True)
