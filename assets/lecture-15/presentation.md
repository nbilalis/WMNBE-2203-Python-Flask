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

# Flask #9

### Blueprints / Web APIs

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- Blueprints
- Web APIs
  - REST

---
template: section

## Blueprints

---
layout: true
template: chapter

### Blueprints

---

#### Modularity

Με τη χρήση των `Blueprint`, μπορούμε να κάνουμε την εφαρμογή μας πιο _modular_, δηλαδή να χωρίσουμε το project σε μικρότερα τμήματα.

Κάθε τέτοιο τμήμα μπορεί να συνοδεύεται και από το δικό του `URL prefix`.

---

#### Instantiation

Ένα `Βlueprint` χρησιμοποιείται σχεδόν με τον ίδιο τρόπο όπως και ένα `Flask app`, χωρίς όμως να είναι ένα ολοκληρωμένο `app`.

Είναι στην ουσία μια συλλογή από επί μέρους στοιχεία που μπορούν να ενσωματωθούν σε μία εφαρμογή.

```python
bp = Blueprint('main', __name__, url_prefix='/')

@bp.get('/')
def home():
    return 'Hello from a Blueprint!'

```

---

#### Registration

Για να ενσωματώσουμε ένα `Blueprint` σε μία εφαρμογή αρκεί να το εγγράψουμε σε αυτή.

```python
app.register_blueprint(bp)

```

Από την έκδοση _2.0_ του `Flask` και μετά υποστηρίζονται και εμφωλευμένα `Blueprint`.

```python
parent = Blueprint('parent', __name__, url_prefix='/parent')
child = Blueprint('child', __name__, url_prefix='/child')
parent.register_blueprint(child)
app.register_blueprint(parent)

```

---

#### URLs

Μια αλλαγή που πρέπει να κάνουμε, σε περίπτωση που μετατρέψουμε μία εφαρμογή μας ώστε να χρησιμοποιεί `Blueprint`, είναι η εξής.

Πρέπει στη μέθοδο `url_for` να συμπεριλαμβάνουμε και το όνομα του `Blueprint`.

```python
url_for('main.home')

```

---
template: section

## Web APIs

---
layout: true
template: chapter

### Web APIs

---

#### What is it?

Ένα _Web API_ (_Application Programming Interface_) είναι μια διεπαφή που επιτρέπει σε συστήματα να επικοινωνούν μεταξύ τους, μέσω του προτοκόλλου `HTTP` / `HTTPS`.

Επιτρέπει τη διαλειτουργικότητα μεταξύ εφαρμογών, κυρίως μέσω `JSON` ή `XML`.

Πολλές γνωστές εφαρμογές (_Google_, _Facebook_, _Twitter_), παρέχουν κάποιου είδους `Web API` (πολύ συχνά αναφέρεται απλά ως `API`).

---

#### What is it meant for?

- Για να παρέχουμε πρόσβαση στα δεδομένα της εφαρμογής μας σε τρίτους.
- Για την επικοινωνία διακριτών συστημάτων μεταξύ τους.
- Για το backend κομμάτι μιας _SPA_ ή _mobile_ εφαρμογής.

---

#### REST

Ένα _Web API_ μπορεί να δομηθεί με ποικίλους τρόπους και συχνά χρειάζεται ένα σύνολο οδηγιών / καλών πρακτικών για να αναπτυχθεί σωστά.

Μια δημοφιλής αρχιτεκτονική, για το σκοπό αυτό, είναι η αρχιτεκτονική _REST_ (_Representational state transfer_).

Ένα _Web API_ χαρακτηρίζεται ως _RESTful_ όταν ακολουθεί τις οδηγίες αυτές.

---
class: long-text

#### REST

Σύμφωνα με τη διατριβή του _Roy Fielding_ (όπου πρωτοπαρουσιάστηκε η ιδέα του REST):

An application or architecture considered RESTful or REST-style is characterized by:

- State and functionality are divided into distributed resources
- Every resource is uniquely addressable using a uniform and minimal set of commands (typically using HTTP commands of GET, POST, PUT, or DELETE over the Internet)
- The protocol is client/server, stateless, layered, and supports caching

---
class: long-text

#### Super simple `Web API` with `Flask`

Για να δημιουργήσουμε ένα απλό `Web API` με `Flask`, χωρίς τη χρήση κάποιας επέκτασης, θα ακολουθήσουμε τις παρακάτω οδηγίες:

- Σε ξεχωριστό `Blueprint`, με δικό του _URL Prefix_, ορίζουμε τα `routes` / `endpoints` του _API_.
  - Μέσα στο _prefix_, καλό είναι να υπάρχει και πρόβλεψη για versioning.
- Με κατάλληλη διαχείριση των `HTPP Verbs / Methods` εκτελούμε τις λειτουργίες `CRUD`.
- Ένα _view function_ αρκεί να επιστρέξει ένα `Dictionary` ώστε αυτό να μετατραπεί σε _JSON_.
  - Αν θέλουμε να επιστρέψουμε μία λίστα από στοιχεία, χρησιμοποιούμε τη μέθοδο `jsonify`.

---

#### Παράδειγμα

```python
from flask import Blueprint, jsonify

…

bp = Blueprint('api', __name__, url_prefix='/api/v1')

users = [
  { 'username': 'alice', 'Firstname': 'Alice' },
  { 'username': 'bob', 'Firstname': 'Bob' }
]

@bp.route('/users/', methods=['GET'])
def get_users():
    return jsonify(users)

```

---
template: list

### Χρήσιμα links

- ![favicon](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Blueprints and Views — Flask Documentation (2.2.x) https://flask.palletsprojects.com/en/2.2.x/tutorial/views/
- ![favicon](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Modular Applications with Blueprints — Flask Documentation (2.2.x) https://flask.palletsprojects.com/en/2.2.x/blueprints/
- ![favicon](https://www.google.com/s2/favicons?domain=programminghistorian.org) Creating Web APIs with Python and Flask | Programming Historian https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
- ![favicon](https://www.google.com/s2/favicons?domain=www.service-architecture.com) Representational State Transfer (REST) https://www.service-architecture.com/articles/web-services/representational-state-transfer-rest.html
- ![favicon](https://www.google.com/s2/favicons?domain=www.codecademy.com) What is REST? | Codecademy https://www.codecademy.com/articles/what-is-rest
- ![favicon](https://www.google.com/s2/favicons?domain=developer.mozilla.org) HTTP request methods - HTTP | MDN https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- ![favicon](https://www.google.com/s2/favicons?domain=restfulapi.net) HTTP Status Codes https://restfulapi.net/http-status-codes/

---
template: list

### Extra info

- ![favicon](https://www.google.com/s2/favicons?domain=smartbear.com) Understanding SOAP vs REST: Basics And Differences https://smartbear.com/blog/soap-vs-rest-whats-the-difference/
- ![favicon](https://www.google.com/s2/favicons?domain=flask-restful.readthedocs.io) Flask-RESTful — Flask-RESTful 0.3.8 documentation https://flask-restful.readthedocs.io/en/latest/
- ![favicon](https://www.google.com/s2/favicons?domain=flask-marshmallow.readthedocs.io) Flask-Marshmallow: Flask + marshmallow for beautiful APIs — Flask-Marshmallow 0.14.0 documentation https://flask-marshmallow.readthedocs.io/en/latest/#flask_marshmallow.sqla.SQLAlchemyAutoSchema
- ![favicon](https://www.google.com/s2/favicons?domain=marshmallow.readthedocs.io) marshmallow: simplified object serialization — marshmallow 3.17.1 documentation https://marshmallow.readthedocs.io/en/stable/
- ![favicon](https://www.google.com/s2/favicons?domain=betterprogramming.pub) Building Restful APIs With Flask and SQLAlchemy (Part 1) | by Babatunde Koiki | Better Programming https://betterprogramming.pub/building-restful-apis-with-flask-and-sqlalchemy-part-1-b192c5846ddd
- ![favicon](https://www.google.com/s2/favicons?domain=realpython.com) Python REST APIs With Flask, Connexion, and SQLAlchemy – Real Python https://realpython.com/flask-connexion-rest-api/

---
template: section

## Thank You!
