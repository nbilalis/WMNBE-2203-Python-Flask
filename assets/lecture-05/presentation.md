name: common
layout: true
class: common

.logo-sae[![SAE Logo](img/logo-sae.png)]
.logo-web[![WEB logo](img/logo-web.png)]

.ruler.one[· · · · · · · ·]
.ruler.two[· · · · · · · ·]
.ruler.three[· · · · · · · ·]
.ruler.four[· · · · · · · ·]
.ruler.five[· · · · · · · ·]
.ruler.six[· · · · · · · ·]
.ruler.seven[· · · · · · · ·]

.footer[Nikos Bilalis - n.bilalis@sae.edu]

---
name: cover
layout: true
template: common
class: cover

---
name: section
layout: true
template: common
class: section, center, middle

---
name: section-details
layout: true
template: common
class: section-details, topbar-space

---
name: chapter
layout: true
template: common
class: chapter, topbar-space

---
name: list
layout: true
template: common
class: list, topbar-space

---
template: cover

## WMNBE-2203 | BACK-END DEVELOPMENT

# Flask #2

### Templates | Static assets

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- `Jinja2`
  - Control structures
  - Template Hierarchy
- `URL` generation
- Error pages

---
template: section

## Templates

---
layout: true
template: chapter

### Templates

---

#### `HTML` rendering

Αν και μπορούμε να επιστρέφουμε `HTML` απευθείας από τα _view functions_ του `Flask`, δεν είναι ιδιαίτερα πρακτικό.

```python
@app.route('/hello/<username>')
def hello(username):
  return f'''
    <html>
      <head>
        <title>Hello</title>
      </head>
      <body>
        <h1>Hello {username}!</h1>
      </body>
    <html>
  '''

```

---

#### Template engine

Το `Flask` κάνει χρήση της _template engine_ `Jinja2` η οποία ρυθμίζεται αυτόματα από το ίδιο το framework.

Για να γίνει _render_ ένα _template_ (πρότυπο) αρκεί να κληθεί η συνάρτηση `render_template()`.

```python
from flask import Flask, render_template
…
@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

```

---

#### Folder structure

Τα _templates_, για να μπορέσει να τα βρει η μηχανή, πρέπει να βρίσκονται σε φάκελο `templates` ο οποίος πρέπει να  βρίσκεται "δίπλα" στην _Flask_ εφαρμογή.

Ομοίως τα _static_ αρχεία πρέπει να βρίσκονται σε φάκελο `static`.

```
/app.py
/templates
  /hello.html
/static
  /css
    /style.css
  /js
    app.js

```

---
template: section

## `Jinja2`

---
layout: true
template: chapter

### `Jinja2`

---

#### `Jinja2`

Η μηχανή `Jinja2` είναι ιδιαίτερα δυνατή και έχει τη δική της σύνταξη, που στα περισσότερα σημεία θυμίζει `Python`.

```jinja2
<html>
  …
  <body>
    <h1>Hello
      {% if username %}
        {{ username }}!
      {% else %}
        world!
      {% endif %}
    </h1>
  </body>
<html>

```

---

#### Tags/Placeholders/Delimiters

Για την παρεμβολή "κώδικα" `Jinja2` μέσα στο πρότυπο, γίνεται χρήση των παρακάτω `tags`:

- `{% … %}` για εντολές
- `{{ … }}` για εκφράσεις (οι οποίες θα "τυπωθούν")
- `{# … #}` για σχόλια (μη ορατά στο τελικό αποτέλεσμα)

Παρόλο που μπορούμε να έχουμε αρκετά σύνθετες εκφράσεις και εντολές μέσα στα ίδια τα _templates_, καλό είναι να το αποφεύγουμε.

Κρατάμε στα _templates_ οτι έχει να κάνει με την εμφάνιση και τα υπόλοιπα ανήκουν μέσα στα _view functions_.

---
template: section

## Control structures

---
layout: true
template: chapter

### Control structures

---

#### `if`

Για τον έλεγχο περιπτώσεων

```jinja2
<div>
{% if user %}
  <span>{{ user.username }}</span>
{% else %}
  <a href="/login">login</a>
{% endif %}
</div>

```

---

#### `for`

Για βρόχο πάνω σε στοιχεία/αντικείμενα

```jinja2
<h1>Products</h1>
<ul>
{% for product in products %}
  <li>{{ product.title }}</li>
{% endfor %}
</ul>

```

---

#### `macro`

Για την επαναχρησιμοποίηση τμημάτων

```jinja2
{% macro input(name, value='', type='text', size=20) %}
    <input type="{{ type }}" name="{{ name }}"
           value="{{ value }}" size="{{ size }}">
{% endmacro %}

<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>

```

---
template: section

## Filters

---
layout: true
template: chapter

### Filters

---
class: long-code

#### Built-in Filters

Μέσα σε ένα `Jinja2` _statement_ μπορούν να χρησιμοποιηθούν εντολές και μέθοδοι της `Python`, για να διαμορφώσουμε κατάλληλα το παραγόμενο αποτέλεσμα.

```jinja2
{{ page.title.capitalize() }}
{{ "Hello, {}!".format(name) }}

```

Παρόλα αυτά είναι προτιμότερη η χρήση των ενσωματωμένων φίλτρων, με τη χρήση του χαρακτήρα `|`, που είναι επαρκή για τις περισσότερες συνηθισμένες λειτουργίες.

```jinja2
{{ page.title|capitalize }}             {# This is nicer #}
{{ "%s, %s!"|format(greeting, name) }}  {# This one not so much #}

```

---
class: long-text

#### `HTML` Escaping

Δύο από τα πιο χρήσιμα φίλτρα, βρίσκονται στο _module_ `MarkupSafe`.

`e`: κάνει _escape_ το _string_ που θα του δοθεί, δηλαδή αντικαθιστά τους "ύποπτους" χαρακτήρες (`>`, `<`, `&`, `"`) με ασφαλείς.

`safe`: επισημαίνει ένα _string_ ως ασφαλή, ώστε να μην γίνουν σε αυτό αντικαταστάσεις χαρακτήρων.

Η χρήση του `e` είναι, κυρίως, για την αποφυγή επιθέσεων, όπως `XSS` κ.λπ. Είναι αναγκαίο μόνο αν έχει ενεργοποιηθεί το `manual escaping`.

To `safe` χρησιμοποιείται όταν κάποια έκφραση παράγει, με βεβαιότητα, ασφαλή κώδικα `HTML` και θέλουμε να εμφανίσουμε το περιεχόμενο ως έχει.

---

#### Custom Filters

Η χρησιμότητα των φίλτρων φαίνεται, ιδιαίτερα, στη δυνατότητα ορισμού custom φίλτρων.

```python
def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'el_GR')
    return locale.currency(value,
                           symbol=True,
                           grouping=True)

filters.FILTERS["format_currency"] = format_currency

```

```jinja2
<span>{{ product.price|format_currency }}</span>

```

---
template: section

## Template Hierarchy

---
layout: true
template: chapter

### Template Hierarchy

---

#### `block`

Για την καλύτερη οργάνωση των _templates_, συχνά χρειαζόμαστε ένα βασικό πρότυπο στο οποίο θα βασίζονται κάποια από/όλα τα υπόλοιπα.

Σε αυτό θα βρίσκονται τα κοινά στοιχεία μεταξύ των διαφόρων _views_ ώστε να μην επαναλαμβάνονται.

Για να το επιτύχουμε αυτό χρησιμοποιούμε το _tag_ `block` και την "εντολή" `extends`.

---

#### `block`

Στο βασικό _template_ ορίζουμε περιοχές στις οποίες μπορούν τα υπόλοιπα _templates_ να παρεμβάλουν το δικό τους περιεχόμενο.

Αυτές οι περιοχές μπορούν να περιέχουν ήδη κάποιο _default_ περιεχόμενο ή και όχι.

Ένα `block` μπορεί να οριστεί και ως `required`.

---

#### Base Template

```jinja2
<html>
<head>
    <title>{% block title %}{% endblock %} - Site</title>
</head>
<body>
    <div id="main">
      {% block main required %}{% endblock %}
    </div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright {{ year }}.
        {% endblock %}
    </div>
</body>
</html>

```

---

#### Child Template

```jinja2
{% extends "base.html" %}

{% block title %}Home page{% endblock %}

{% block main %}
  <h1>This is the home page</h1>
{% endblock %}

```

---

#### `include`

Στην οργάνωση των _templates_ βοηθά και η χρήση της εντολής `include`.

Ο ρόλος της είναι προφανής, μας επιτρέπει την ενσωμάτωση άλλων αρχείων στο _template_.

```jinja2
<body>
  {% include "_header.html" %}
  {% block main required %}{% endblock %}
  {% include "_footer.html" %}
</body>

```

---
template: section

## `URL` generation

---
layout: true
template: chapter

### `URL` generation

---

#### `url_for()`

Μέσα στα  _templates_, αλλά και στα _view functions_, συχνά αναφερόμαστε σε _URLs_ που αφορούν, είτε σε κάποιο _route_/_view function_, είτε σε κάποιο _static asset_.

Αν και μπορούμε να ορίσουμε αυτά τα _URLs_ εμείς, καλό είναι να τα δημιουργούμε μέσω της κατάλληλης _function_ του `Flask`.

```python
# for view functions
url_for('view_function_name', param1=value1, …)

# for static assets
url_for('static', filename='…')

```

---
class: long-code

#### Παράδειγμα

```jinja2
<html>
  <head>
    …
    <link rel="stylesheet"
          href="{{ url_for('static', filename='css/style.css') }}">
  </head>
  <body>
    …
    <ul>
      {% for key, product in products.items() %}
      <li>
        <a href="{{ url_for('product_details', sku=key) }}">
          {{ product.title }}
        </a>
      </li>
      {% endfor %}
    </ul>
  </body>
</html>

```

---

#### `redirect`

Στα πλαίσια ενός _view function_ η `url_for` είναι χρήσιμη στην περίπτωση που πρέπει να γίνει ανακατεύθυνση σε άλλη διεύθυνση.

Για την ανακατεύθυνση θα γίνει χρήση της συνάρτησης `redirect`.

_Προσοχή_ η redirect χρησιμοποιείται "πάντα" με την εντολή `return`, όλες οι _view function_ **πρέπει** να επιστρέφουν κάτι.

```python
return redirect(url_for('view_function_name',
                param1=value1,
                …))

```

---

#### Παράδειγμα

```python
@app.route('/products/<sku>')
def product_details(sku):
    products = get_products()
    product = products.get(sku, None)

    if product is not None:
        return render_template('products/details.html',
                                product=product)
    else:
        return redirect(url_for('product_list'))

```

---
template: section

## Error pages

---
layout: true
template: chapter

### Error pages

---

#### `abort`

Πέρα από την ανακατεύθυνση σε άλλο _view_ μπορούμε, με κώδικα, να ανακατευθύνουμε το χρήστη σε σελίδα σφάλματος.

Σε αυτή την περίπτωση θα γίνει χρήση της συνάρτησης `abort`.

Η συνάρτηση `abort` του `Flask` _module_ δέχεται, ως όρισμα, το κατάλληλο _HTTP status code_.

```python
return abort(error_code)

```

---

#### Παράδειγμα

```python
@app.route('/profile/<username>')
def profile(username):
    user = get_user(username)

    if user is not None:
        return render_template('users/profile.html',
                                user=user)
    else:
        return abort(404)

```

---

#### `errorhandler`

Τι είναι πιο σωστό, να εμφανίσω ένα σφάλμα, π.χ. `404`, ή να ανακατευθύνω σε μια _custom_ σελίδα λάθους;

Μπορούν να γίνουν και τα δύο, με τη συνάρτηση `abort()` επιστρέφω το επιθυμητό σφάλμα και με τον _decorator_ `errorhandler` αναθέτω τη διαχείριση των σφαλμάτων σε κατάλληλα _views_.

```python
@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug(e)
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404

```

---
template: list

### Χρήσιμα links

- ![](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Quickstart — Flask Documentation (2.1.x) https://flask.palletsprojects.com/en/2.1.x/quickstart/
- ![](https://www.google.com/s2/favicons?domain=jinja.palletsprojects.com) Template Designer Documentation — Jinja Documentation (3.1.x) https://jinja.palletsprojects.com/en/3.1.x/templates/
- ![](https://www.google.com/s2/favicons?domain=realpython.com) Primer on Jinja Templating – Real Python https://realpython.com/primer-on-jinja-templating/
- ![](https://www.google.com/s2/favicons?domain=ttl255.com) Jinja2 Tutorial - Part 1 - Introduction and variable substitution | https://ttl255.com/jinja2-tutorial-part-1-introduction-and-variable-substitution/

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=en.wikipedia.org) List of HTTP status codes - Wikipedia https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
- ![](https://www.google.com/s2/favicons?domain=jinja.palletsprojects.com) List of Builtin Filters — Jinja Documentation (3.1.x) https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters

---
template: section

## Thank You!
