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

# Flask #6

### Data Persistence - SQLAlchemy

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- Object-Oriented Programming (OOP) basics
  - Class
  - Attributes
  - Constructor / Methods
  - Inheritance
  - Properties
- SQLAlchemy
  - Session
  - Model / Column
  - Relationships

---
template: section

## OOP basics

---
layout: true
template: chapter

### OOP basics

---

#### `Python` & `OOP`

Η `Python` υποστηρίζει αρκετές διαφορετικές προσεγγίσεις προγραμματισμού. Ο _Αντικειμενοστρεφής Προγραμματισμός_ είναι μία από αυτές.

Στον _Αντικειμενοστρεφή Προγραμματισμό_ (`OOP`) τα πρωτεύοντα δομικά στοιχεία του προγράμματος είναι τα δεδομένα, από τα οποία δημιουργούνται, με κατάλληλη μορφοποίηση, τα αντικείμενα (`objects`).

Στόχος του είναι η δημιουργία ευέλικτου και επαναχρησιμοποιούμενου κώδικα.

---

#### `class`

Στην καρδιά του `OOP` είναι η κλάση (`class`). Η κλάση είναι το "προσχέδιο", βάσει του οποίου φτιάχνονται τα αντικείμενα.

Συχνά, μία κλάση έχει το ρόλο μιας _user-defined_ δομής δεδομένων (_data-structure_), που βασίζεται στους απλού τύπους δεδομένων της γλώσσας.

Αλλά μια κλάση, εκτός από τα χαρακτηριστικά (_attributes_), ορίζει και τη συμπεριφορά (_behavior_) των αντικειμένων.

```python
class Person:
    pass

```

---

#### `attributes`

Τα βασικότερα στοιχεία μίας κλάσης είναι τα χαρακτηριστικά της.

Στην `Python` τα χαρακτηριστικά μιας κλάσης μπορεί να είναι, είτε στο επίπεδο της κλάσης (_class attributes_), είτε στο επίπεδο των αντικειμένων / στιγμιότυπων (_instance attributes_).

Τα _class attributes_ ορίζονται ως μεταβλητές στο σώμα της κλάσης, ενώ τα _instance attributes_ ορίζονται μέσα στη μέθοδο κατασκευαστή (_constructor_).

---

#### `class` vs `instance` `attributes`

- _instance attributes_: Χαρακτηριστικά στα οποία κάθε αντικείμενο / στιγμιότυπο κρατά τις δικές του τιμές.
- _class attributes_: Χαρακτηριστικά με κοινές τιμές για όλα τα αντικείμενα / στιγμιότυπα της κλάσης, **εκτός αν** κάποιο αντικείμενο ορίσει δικές του τιμές για αυτά.

  Χρήσιμα για σταθερές ή για προκαθορισμένες (_default_) τιμές σε `attributes`.

---

#### `constructor`

Το ρόλο του `constructor` μιας κλάσης εξυπηρετεί η _dunder_ μέθοδος `__init__`.

```python
class Person:
    def __init__(self):
        pass

```

Πρώτο όρισμα της μεθόδου αυτής είναι μία αναφορά στο ίδιο το αντικείμενο.

Το όρισμα αυτό μπορεί να έχει οποιοδήποτε όνομα, αλλά συνηθίζεται το όνομα `self`.

---

#### Παράδειγμα

```python
class Person:
    # class attribute
    origin = 'Earth'

    def __init__(self, fn, ln):
        # instance attributes
        self.firstname = fn
        self.lastname = ln

```

---

#### Instantiation

Ένα αντικείμενο (_object_) είναι ένα στιγμιότυπο (_instance_) της κλάσης.

Έχει τις δικές του τιμές για κάθε ένα από τα χαρακτηριστικά που ορίζονται στην κλάση στην οποία ανήκει.

Τα αντικείμενα δημιουργούνται, κυρίως, καλώντας τη μέθοδο κατασκευαστή (_constructor_).

```python
p1 = Person('Guido', 'Van Rossum')
p2 = Person('Armin', 'Ronacher')

```

---
class: long-text

#### `methods`

Όπως ειπώθηκε και νωρίτερα, δεν είναι μόνο τα _attributes_ που χαρακτηρίζουν μία κλάση, αλλά και οι μέθοδοι της (`methods`).

Οι μέθοδοι είναι συναρτήσεις που ανήκουν στην κλάση και έχουν πρόσβαση στα χαρακτηριστικά ενός αντικειμένου, μέσω του ειδικού ορίσματος `self`, όπως και ο `constructor`.

```python
class Person:
    …
    def say_hello(self):
        print(f"Hi, I'm {self.firstname}!")

```

---
class: long-text, long-code

#### `class methods`

Μιας και η _dunder_ μέθοδος `__init__` είναι μοναδική ανά κλάση, σε περίπτωση που χρειάζονται παραπάνω από ένας τρόποι δημιουργίας ενός αντικειμένου, μπορεί να χρησιμοποιηθεί ο _decorator_ `@classmethod`.

Μία μέθοδος "διακοσμημένη" με το `@classmethod`, δέχεται ως πρώτο όρισμα μια αναφορά στην κλάση.

```python
class Person:
    …
    @classmethod
    def from_full_name(cls, name):
        fn, ln = name.split(' ')
        return cls(fn, ln)      # cls(*name.split(' '))

```

---
class: long-text

#### `static methods`

Όπως και οι `class methods`, μία `static` μέθοδος δεν έχει αναφορά σε συγκεκριμένο αντικείμενο, για αυτό και απουσιάζει και εδώ η παράμετρος `self`.

Χρησιμοποιείται για _utility_ μεθόδους και γενικά για μεθόδους που αφορούν στην ίδια την κλάση, χωρίς όμως να μπορούν να τροποποιήσουν το _state_ της.

```python
class Person:
    …
    @staticmethod
    def get_definition():
        return 'A person (plural people or persons) is …'

```

---
class: long-text

#### Inheritance

Η _κληρονομικότητα_ είναι ένα από τα πιο δυνατά χαρακτηριστικά του `OOP`, που βοηθά, μεταξύ άλλων, στο να μειωθεί ο επαναλαμβανόμενος κώδικας.

Μέσω της κληρονομικότητας μία κλάση "κληρονομεί" όλα τα χαρακτηριστικά της κλάσης γονέα.

Στην `Python` αυτό γίνεται ως εξής:

```python
class BaseClass:
    <base class code>

class DerivedClass(BaseClass):
    <derived class code>

```

---
class: long-code

#### Παράδειγμα

```python
class Person:
    def __init__(self, fn, ln):
        self.first_name = fn        # instance attribute
        self.last_name = ln         # instance attribute

    def say_hello(self):
        print(f"Hi, I'm {self.first_name} {self.last_name}!")

    def __repr__(self):
        return f'<Person {self.first_name=}, {self.last_name=}>'

class Student(Person):
    def __init__(self, fn, ln, rn):
        super().__init__(fn, ln)    # Calling Person's constructor

        self.registration_number = rn

    def __repr__(self):
        return f'<Student {self.registration_number=}>'

```

---
class: extra-long-text

#### Properties

Αν χρειαζόμαστε περισσότερο έλεγχο στον τρόπο που προσπελαύνονται τα `attributes` μίας κλάσης, μπορούσε να χρησιμοποιήσουμε τον _decorator_ `@property`, μαζί με τους:

`@<property-name>.setter` ή/και `@<property-name>.deleter`.

Με τον `@property`, ορίζουμε μία μέθοδο η οποία θα καλείται όταν ζητηθεί η τιμή ενός `property`. Το `property` αυτό θα έχει το ίδιο όνομα με τη μέθοδο.

Με τους `@<property-name>.setter` και `@<property-name>.deleter` ορίζουμε τις μεθόδους που θα κληθούν όταν προσπαθήσουμε να αλλάξουμε τιμή ή να διαγράψουμε το `property`, αντίστοιχα.

Η τιμή του `property` αποθηκεύεται σε ένα `instance attribute` το οποίο, από παραδοχή, έχει ως πρόθεμα ένα ή δύο `_`.

---
class: extra-long-code

#### Παράδειγμα

```python
class Student(Person):
    def __init__(self, rn):
        self.registration_number = rn
        self.__grades = []

    @property
    def grades(self):   # Getter
        return self.__grades

    @grades.setter      # Setter
    def grades(self, value):
        if len(self.__grades) == 0:
            self.__grades = value
        else:
            raise AttributeError('You cannot re-set the grades')

s = Student('12345')
s.grades = [1, 2, 3]    # Setter
print(s.grades)         # Getter
s.grades = [4, 5, 6]    # Error
```

---
template: section

## `SQLAlchemy`

---
layout: true
template: chapter

### SQLAlchemy

---

#### `SQL Toolkit` and `ORM`

Το `SQLAlchemy` είναι μία σουίτα εργαλείων για τη σύνδεση και επικοινωνία μιας εφαρμογής `Python` με μία ή και περισσότερες βάσεις δεδομένων.

Το πιο γνωστό κομμάτι της σουίτας αυτής είναι το κομμάτι του `Object-Relational Mapper` (`ORM`), το οποίο υλοποιεί το `data mapper` μοτίβο.

Με αυτό γίνεται αντιστοίχιση κλάσεων της εφαρμογής με τα στοιχεία της βάσης.

---
class: long-text, long-code

#### `session`

Στην καρδιά του `SQLAlchemy` βρίσκεται το `session`. Μέσω αυτού γίνεται όλη η διαχείριση της επικοινωνίας με τη βάση με τη βάση.

Προσοχή να μη συγχέεται με το `session` μιας web εφαρμογής. Tο `session` εδώ παίζει, λίγο ή πολύ, το ρόλο του `connection`.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/app.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

```

---
class: long-code

#### `Flask-SQLAlchemy`

Μιας και ο τρόπος διαχείρισης ενός `session` είναι, συχνά, συγκεκριμένος σε μια web εφαρμογή, συνιστάται η χρήση του `Flask-SQLAlchemy` module.

Το `Flask-SQLAlchemy` μπορεί να αναλάβει τη διαχείρισή του `session` αυτόματα, με ελάχιστες ρυθμίσεις.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/app.db'
db = SQLAlchemy(app)

```

---
class: long-text, long-code

#### `Model`

Για να γίνει η σύνδεση με τη βάση, χρειάζεται να ορίσουμε κλάσεις που θα αντιπροσωπεύουν τα στοιχεία της και συνήθως αντιστοιχούν 1:1 με τους πίνακές της.

Οι κλάσεις αυτές πρέπει να κληρονομούν από την κλάση `Model` του `SQLAlchemy`.

```python
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username=}>'

```

---
class: long-text

#### `Column`

Τα _attributes_, των κλάσεων αυτών, αντιστοιχούν με τα πεδία των πινάκων. <nobr>Η αντιστοίχιση</nobr> γίνεται μέσω της κλάσης `Column`.

Το όνομα της στήλης θα είναι ίδιο με το όνομα του _attribute_. Αν θέλουμε να διαφέρει πρέπει να το περάσουμε ως πρώτο όρισμα στον κατασκευαστή της `Column`.

Μία στήλη μπορεί να οριστεί ως `primary_key`, `unique`, `nullable`, `autoincrement` με αντίστοιχα _optional_ ορίσματα.

Παραπάνω από μία στήλες μπορούν να οριστούν ως `primary_key` στον ίδιο πίνακα.

---
class: long-text

#### `Column` types

Ο τύπος κάθε στήλης ορίζεται μέσω του πρώτου ορίσματος της `Column` (ή του δεύτερου, αν έχει δοθεί και όνομα).

Οι πιο συνηθισμένοι τύποι είναι οι εξής:

| Τύπος        | Περιγραφή                                                                    |
|--------------|------------------------------------------------------------------------------|
| Integer      | an integer                                                                   |
| String(size) | a string with a maximum length (optional in some databases)                  |
| Text         | some longer unicode text                                                     |
| DateTime     | date and time expressed as Python datetime object                            |
| Float        | stores floating point values                                                 |
| Boolean      | stores a boolean value                                                       |

---
class: long-text, long-code

#### `ForeignKey`

Οι απλές σχέσεις (`1:1`, `1:Ν`) ορίζονται, κυρίως, μέσω της κλάσης `ForeignKey`.

Στη δήλωση του `FK`, κατά την κλήση του κατασκευαστή της `Column`, περνάμε ως όρισμα το `db.ForeignKey('<table>.<pk>')`.

Όπου `<table>.<pk>` τα ονόματα του πίνακα, από την "άλλη πλευρά" της σχέσης, και του πεδίου (συνήθως το `PK`).

```python
class Article(db.Model):
    …
    category_id = db.Column(db.Integer,
        db.ForeignKey('category.id'),
        nullable=False)

```

---
class: long-text, long-code

#### `relationship`

Πέρα από τη δήλωση του `ForeignKey`, μπορούμε με τη μέθοδο `relationship` να δημιουργήσουμε _attributes_ που αφορούν στα συσχετιζόμενα αντικείμενα.

Η κλήση της `relationship` μπορεί να βρίσκεται από οποιαδήποτε "πλευρά" της σχέσης και μπορεί να δημιουργήσει _attributes_ και στα δύο "άκρα" ταυτόχρονα, με τη βοήθεια του ορίσματος `backref`.

Σε σχέσεις `1:1` αρκεί να προστεθεί το όρισμα `uselist=False`.

```python
class Post(db.Model):
    …
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref='posts', lazy=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

```

---
class: long-text

#### `lazy`

Η παράμετρος `lazy` καθορίζει τον τρόπο και τη στιγμή που το `SQLAlchemy` θα φορτώσει από τη βάση τα σχετιζόμενα δεδομένα.

| Τιμή             | Περιγραφή                                                                                  |
|------------------|--------------------------------------------------------------------------------------------|
| `select`/`True`  | (_default_) will load the data as necessary in one go using a standard `select` statement. |
| `joined`/`False` | load the relationship in the same query as the parent using a `join` statement.            |
| `subquery`       | works like `joined` but will use a `subquery` statement.                                   |
| `dynamic`        | will return another query object which you can further refine before loading the items.    |

---
class: long-text

#### `table`

Στις `1:N` και `1:1` σχέσεις, σε κάθε άκρο τους υπάρχει μία οντότητα. Στις `N-N` σχέσεις, από την άλλη, υπάρχει ένα ενδιάμεσος, βοηθητικός, πίνακας.

Για να οριστούν τέτοιου είδους σχέσεις και να περιγραφούν οι ενδιάμεσοι αυτοί πίνακες, πρέπει να χρησιμοποιηθεί η μέθοδος `table`.

Με τη μέθοδο `table` θα μπορούσαν να οριστούν όλοι οι πίνακες της βάσεις, ώστε οι κλάσεις / μοντέλα να μην περιέχουν (όσο είναι δυνατό) <nobr>`database-related`</nobr> κώδικα.

Aυτό, όμως, αποτελεί μια διαφορετική προσέγγιση, που δεν θα καλυφθεί εδώ.

---
class: long-code

#### Παράδειγμα

```python
book_authors = db.Table('book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    authors = db.relationship('Author',
                              secondary=book_authors,
                              backref='books')

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

```

---
template: list

### Χρήσιμα links

- ![](https://www.google.com/s2/favicons?domain=realpython.com) Object-Oriented Programming (OOP) in Python 3 – Real Python https://realpython.com/python3-object-oriented-programming/
- ![](https://www.google.com/s2/favicons?domain=www.programiz.com) Python Object Oriented Programming - Programiz https://www.programiz.com/python-programming/object-oriented-programming
- ![](https://www.google.com/s2/favicons?domain=flask.palletsprojects.com) SQLAlchemy in Flask — Flask Documentation (2.0.x) https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/
- ![](https://www.google.com/s2/favicons?domain=medium.com) Under the Hood of Flask-SQLAlchemy | by Kelly Foulk | Analytics Vidhya | Medium https://medium.com/analytics-vidhya/under-the-hood-of-flask-sqlalchemy-793f7b3f11c3
- ![](https://www.google.com/s2/favicons?domain=flask-sqlalchemy.palletsprojects.com) Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (2.x) https://flask-sqlalchemy.palletsprojects.com/en/2.x/

- ![](https://www.google.com/s2/favicons?domain=docs.sqlalchemy.org) SQLAlchemy ORM — SQLAlchemy 1.4 Documentation https://docs.sqlalchemy.org/en/14/orm/index.html
- ![](https://www.google.com/s2/favicons?domain=realpython.com) Data Management With Python, SQLite, and SQLAlchemy – Real Python https://realpython.com/python-sqlite-sqlalchemy/#creating-a-database-structure

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=www.geeksforgeeks.org) class method vs static method in Python - GeeksforGeeks https://www.geeksforgeeks.org/class-method-vs-static-method-python/
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - How do I know if I can disable SQLALCHEMY_TRACK_MODIFICATIONS? - Stack Overflow https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications/33790196#33790196
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - How to define two relationships to the same table in SQLAlchemy - Stack Overflow https://stackoverflow.com/questions/7548033/how-to-define-two-relationships-to-the-same-table-in-sqlalchemy
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - SQLAlchemy default DateTime - Stack Overflow https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - SQLAlchemy: cascade delete - Stack Overflow https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) python - Sqlite / SQLAlchemy: how to enforce Foreign Keys? - Stack Overflow https://stackoverflow.com/questions/2614984/sqlite-sqlalchemy-how-to-enforce-foreign-keys

---
template: section

## Thank You!
