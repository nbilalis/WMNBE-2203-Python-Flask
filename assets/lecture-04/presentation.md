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

# Flask #1

### Intro | Setup | Routing

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- Εισαγωγή
- Εγκατάσταση
  - `venv`
  - `pip`
  - `Flask`
- Πρώτα βήματα
  - `Routing`

---
template: section

## Flask

---
layout: true
template: chapter

### Flask

---

#### Γενικά

Το `Flask` είναι ένα _micro WSGI web application framework_, σχεδιασμένο για το γρήγορο και εύκολο "στήσιμο" του κομματιού _back-end_ μιας web εφαρμογής.

Βασίζεται πάνω στα εργαλεία `Werkzeug` και `Jinja` και είναι ένα από τα πιο δημοφιλή _frameworks_ ανάπτυξης web εφαρμογών.

---
layout: true
template: chapter

### Εγκατάσταση

---

#### `Python`

Για την εγκατάσταση, θεωρούμε δεδομένο ότι υπάρχει ήδη εγκατεστημένη η έκδοση _3.x_ της `Python`.

```bash
> python --version
Python 3.10.4

```

Δημιουργούμε ένα φάκελο και "σετάρουμε" το `venv`.

```bash
$ mkdir flask_app
$ cd flask_app
$ python3 -m venv .venv

```

```powershell
> python -m venv .venv

```

---
class: long-text

#### `venv`

Το εργαλείο `venv` είναι για τη δημιουργία ενός εικονικού περιβάλλοντος για τη φάση της ανάπτυξης μιας εφαρμογής.

Σε αυτό το περιβάλλον έχουμε πλήρη έλεγχο στα εργαλεία που είναι εγκατεστημένα και, πιο σημαντικό, στις εκδόσεις τους.

Πριν ξεκινήσουμε τη δουλειά σε ένα project, φροντίζουμε να ενεργοποιήσουμε το περιβάλλον αυτό.

```bash
$ . .venv/bin/activate
(.venv) $ _
```

```powershell
> .venv\Scripts\activate
(.venv) > _
```

---

#### `pip`

Άλλο ένα εργαλείο που θα μας χρειαστεί στην εγκατάσταση είναι ο _package installer_ της `Python`.

Μπορούμε να δούμε την έκδοση που υπάρχει ήδη (εγκαθίσταται μαζί με την `Python`) και προαιρετικά να αναβαθμίσουμε στην τελευταία.

```bash
$ python3 --version
$ python3 -m pip install --upgrade pip
```

```powershell
> python --version
> python -m pip install --upgrade pip
```

---

#### Flask module

Ενώ βρισκόμαστε στο _virtual environment_ που δημιουργήσαμε, εκτελούμε το παρακάτω:

```bash
(.venv) $ pip install Flask

```

---
template: section

## Πρώτα βήματα

---
layout: true
template: chapter

### Πρώτα βήματα

---

#### Hello world!

`hello.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

```

---

#### Εκτέλεση

Για να "τρέξει" η εφαρμογή θα πρέπει να ορίσουμε το αρχείο το οποίο είναι το _entry point_.

Μιας και το `Flask` είναι ένα _micro framework_, μπορεί όλη η εφαρμογή να βρίσκεται σε ένα και μοναδικό αρχείο.

```bash
(.venv) $ export FLASK_APP=hello.py
(.venv) $ flask run

```

```powershell
(.venv) > $env:FLASK_APP = "hello.py"
(.venv) > flask run

```

---

#### Debug mode

Με την εντολή `flask run` ξεκινά ένας τοπικός _development server_ αλλά κάθε φορά που γίνεται μία αλλαγή στον κώδικα, θα πρέπει ο _server_ να επανεκκινείται.

ΓΙα το λόγο αυτό, όσο είμαστε στο στάδιο της ανάπτυξης, να ορίζουμε την παρακάτω ρύθμιση:

```bash
(.venv) $ export FLASK_ENV=development
(.venv) $ flask run

```

```powershell
(.venv) > $env:FLASK_ENV = "development"
(.venv) > flask run

```

---

#### Debug mode

Τι κάνει η ρύθμιση αυτή, σύμφωνα με το [documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode);

> - it activates the debugger
> - it activates the automatic reloader
> - it enables the debug mode on the Flask application.

---
layout: true
template: chapter

### Routing

---

#### Γενικά

Σε μία σύγχρονη _web_ εφαρμογή, συχνά αναφερόμαστε στα `URLs` ως `pretty` / `clean`, `meaningful` και `hackable`.

Για να επιτύχουμε όλα αυτά τα χαρακτηριστικά, χρειαζόμαστε τη βοήθεια των `routes`.

H δήλωση ενός `route` γίνεται με τη χρήση ενός _decorator_ (που μας παρέχει το `Flask`) πάνω σε συναρτήσεις.

```python
@app.route('/url-segment')
def function_to_be_called_when_above_route_is_hit():
  statements

```

---

#### Παράδειγμα

```python
@app.route('/')
def index():
    return '<h1>Home page</h1>'


@app.route('/hello')
def hello():
    return 'Hello, World'

```

---

#### Variables

Ένα `route` μπορεί να περιέχει και μεταβλητά τμήματα. Κάθε ένα από αυτά τα τμήματα θα πρέπει να αντιστοιχεί σε μία παράμετρο της _decorated_ συνάρτησης.

```python
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

```

---

#### Default values

Η δήλωση περισσότερων του ενός `routes` πάνω σε μία συνάρτηση, είναι αποδεκτή. Σε αυτή την περίπτωση βοηθά και η δήλωση _default_ τιμών για τις παραμέτρους.

```python
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='World'):
    return f'Hello, {name}!'

```

---
class: long-text

#### Variable rules

Στη δήλωση των μεταβλητών αυτών μπορεί να προστεθεί και ένας `converter`, όπου ορίζεται ο τύπος της μεταβλητής.

Ένας `converter` λειτουργεί παράλληλα και ως περιορισμός.

| Converter |                                            |
| :-------- | :----------------------------------------- |
| `string`  | (default) accepts any text without a slash |
| `int`     | accepts positive integers                  |
| `float`   | accepts positive floating point values     |
| `path`    | like string but also accepts slashes       |
| `uuid`    | accepts UUID strings                       |

---

#### Παράδειγμα

```python
@app.route('/product/<int:id>')
def product_details(id):
    # Get product details by it's id
    # id is already an int, no need to use int(id)
    return f'Show product details for product {id}: ...'

```

---
template: list

### Χρήσιμα links

- ![favicon](https://www.google.com/s2/favicons?domain=palletsprojects.com) Flask | The Pallets Projects https://palletsprojects.com/p/flask/
- ![favicon](https://www.google.com/s2/favicons?domain=palletsprojects.com) Welcome to Flask — Flask Documentation (2.1.x) https://flask.palletsprojects.com/en/2.1.x/
- ![favicon](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Installation — Flask Documentation (2.1.x) https://flask.palletsprojects.com/en/2.1.x/installation/
- ![favicon](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Quickstart — Flask Documentation (2.1.x) https://flask.palletsprojects.com/en/2.1.x/quickstart/

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=code.visualstudio.com) Python and Flask Tutorial in Visual Studio Code https://code.visualstudio.com/docs/python/tutorial-flask
- ![](https://www.google.com/s2/favicons?domain=hackersandslackers.com) The Art of Routing in Flask https://hackersandslackers.com/flask-routes/

---
template: section

## Thank You!
