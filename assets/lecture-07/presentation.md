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

# Flask #4

### Requests | Sessions

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- `HTTP` methods
  - `methods` argument
  - `app.get()` & `app.post()`
  - `request` object
- Sessions
  - `session` object
  - `app.secret_key`
  - `flash()`
  - `get_flashed_messages()`

---
template: section

## `HTTP` methods

---
layout: true
template: chapter

### `HTTP` methods

---

#### `methods` argument

Ένα `route` στο `Flask` "απαντά" μόνο σε `GET` `requests`, εκτός και αν οριστεί διαφορετικά.

Αν θέλουμε κάποιο `route` / `view function` να διαχειρίζεται και `GET` αλλά και `POST` `requests`, πρέπει να δώσουμε κατάλληλη τιμή στην παράμετρο `methods` του `route` _decorator_:

```python
@app.route('/route', methods=['GET', 'POST'])
def view_function():
  …

```

---

#### `methods` argument

Προφανώς, μπορούμε να έχουμε και `view functions` που διαχειρίζονται μόνο `POST` `requests`.

```python
@app.route('/route', methods=['POST'])
def view_function():
  …

```

Αν κάποιος επιχειρίσει να ζητήσει ένα `route` με μέθοδο που δεν έχει οριστεί στην παράμετρο `methods`, το `Flask` επιστρέφει ένα _405 Method not allowed_ σφάλμα.

---

#### `app.get()` & `app.post()`

Στην έκδοση _2.x_ του `Flask` έχουμε έναν νέο τρόπο να ορίσουμε ποιες μεθόδους διαχειρίζεται πoιο `view function`.

```python
@app.get('/register')
def show_registration_form():
  return render_template('registration_form.html')

@app.post('/register')
def register_user():
  ...

```

---

#### `request` object

To `Flask` δίνει πρόσβαση σε όλες τις πληροφορίες ενός `request`, μέσα από το `request` object.

Από εκεί, μπορεί να δει κάποιος πληροφορίες όπως `method`, `path` κ.α.

```python
from flask import Flask, request

…

@app.route('/route')
def view_function():
  app.logger.debug(request.path)    # /route
  app.logger.debug(request.method)  # GET | POST
  …

```

---

#### `request.args`

Μέσα από το `request` object μπορώ να έχω πρόσβαση και στις _querystring_ παραμέτρους.

```python
# /products/search?query=pants

@app.get('/products/search')
def search():
  query = request.args.get('query')
  …

```

… αν και η λογική των _clean / friendly URLs_ καθιστά τη χρήση των παραμέτρων αυτών, πλέον, σπάνια.

---

#### `request.form`

Τα _form data_ είναι, επίσης, διαθέσιμα από αντίστοιχο `dictionary`.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login-form.html')
  elif request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    …

```

---
template: section

## Sessions

---
layout: true
template: chapter

### Sessions

---

#### `session` object

Μιας και το `HTTP` πρωτόκολλο είναι _stateless_, συχνά χρειαζόμαστε κάποιο μηχανισμό που να επιτρέπει την αποθήκευση στοιχείων, για κάθε χρήστη ξεχωριστά.

Στο `Flask`, όπως και σε όλα τα δημοφιλή web frameworks, υπάρχει η έννοια του `session` object.

Το `session` object λειτουργεί παρόμοια με ένα `dictionary`, όπου μπορούν να αποθηκευτούν _key-value pairs_.

---

#### `session` _id_ & _cookie_

Για να επιτευχθεί η λειτουργικότητα αυτή, ο server δημιουργεί ένα ψηφιακά υπογεγραμμένο `session` _cookie_, που καταστρέφεται αυτόματα μόλις κλείσει το παράθυρο του browser, με κάποιο <nobr>`session` _id_</nobr>.

Αυτό αποστέλλεται από τον client σε κάθε `request` και "ταυτοποιεί" τον client στον οποίο "ανήκει" το `session`.

Αν ο χρήστης δεν υποβάλει κάποιο `request` για κάποιο διάστημα (συχνά είναι στα _20_ λεπτά) το `session` στο server, για το συγκεκριμένο χρήστη, καταστρέφεται.

---

#### `app.secret_key`

Για να μπορέσει κάποιος να χρησιμοποιήσει το `session` object, αρκεί να ορίσει το `secret_key` κάτω από το `Flask` αντικείμενο.

```python
# Set the secret key to some random bytes.
# Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

```

---

#### `app.secret_key`

Ένας καλός τρόπος να παράξει κάποιος ένα τέτοιο κλειδί είναι να εκτελέσει το ακόλουθο σε γραμμή εντολής

```bash
# Recommended by the Flask docs
$ python -c 'import secrets; print(secrets.token_hex())'

# for generating a string of random bytes
$ python -c 'import os; print(os.urandom(24))'

# or as hexadecimal, an appropriate form
# when storing the key in external files
$ python -c 'import os; print(os.urandom(24).hex())'

```

---

#### Persistent sessions

Αν θέλουμε για οποιοδήποτε λόγο το `session` _cookie_ να παραμείνει και μετά το κλείσιμο του παραθύρου του browser, μπορούμε να ορίσουμε τα εξής:

```python
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=3)
# Default: timedelta(days=31) (2678400 seconds)

@app.before_request
def make_session_permanent():
    session.permanent = True

```

---

#### Παράδειγμα

```python
from flask import session
from datetime import datetime

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get('/')
def home():
  if not session['timestamp']:
    session['timestamp'] = datetime.now()

```

---

#### `flash()`

Το μηχανισμό του `session` χρησιμοποιεί και μια ιδιαίτερα χρήσιμη λειτουργία του `Flask`, για την εμφάνιση ενημερωτικών μηνυμάτων στο χρήστη.

Me th χρήση της μεθόδου `flash(message)`, αποθηκεύεται ένα μήνυμα στο `session` μέχρι να χρησιμοποιηθεί.

```python
@app.post('contact')
def send_message():
  msg = request.form.get('message')
  …
  flash('Your message has been sent!')
  return redirect(url_for('home'))

```

---
class: long-code

#### `get_flashed_messages()`

Για να ανακτηθούν τα τυχόν υπάρχοντα μηνύματα σε ένα `template`, πρέπει να γίνει χρήση της συνάρτησης `get_flashed_messages()`.

Η συνάρτηση αυτή επιστρέφει όλα τα αποθηκευμένα μηνύματα, τα οποία θα διαγραφούν αμέσως αφού "χρησιμοποιηθούν".

```jinja2
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <div>Messages:</div>
        {% for message in messages %}
          <div>{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}

```

---

#### Παράδειγμα

```python
@app.post('/register')
def register_user():
    username = request.form.get('username')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    password = request.form.get('password')

    flash('Registration was successful')
    session['username'] = username

    return redirect(url_for('home'))

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('home'))

```

---
template: list

### Χρήσιμα links

- ![](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) The Request Object — Flask Documentation (2.1.x) https://flask.palletsprojects.com/en/2.1.x/quickstart/#the-request-object
- ![](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Sessions — Flask Documentation (2.01.x) https://flask.palletsprojects.com/en/2.1.x/quickstart/#sessions
- ![](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) Message Flashing — Flask Documentation (2.1.x) https://flask.palletsprojects.com/en/2.1.x/quickstart/#message-flashing

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=hackingandslacking.com) Configuring Your Flask Application | by Todd Birchard | Hackers and Slackers https://hackingandslacking.com/configuring-your-flask-application-4e5341d7affb
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - Where should I place the secret key in Flask? - Stack Overflow https://stackoverflow.com/questions/30873189/where-should-i-place-the-secret-key-in-flask
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - Where do I get a SECRET_KEY for Flask? - Stack Overflow https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - demystify Flask app.secret_key - Stack Overflow https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key

---
template: section

## Thank You!
