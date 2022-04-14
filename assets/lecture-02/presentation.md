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

# Python #2

### Basics

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- Βασικά στοιχεία
- Μεταβλητές
- Εκφράσεις
- Είσοδος / Έξοδος
- Συναρτήσεις
- Μορφοποίηση

---
template: section

![](https://i.imgflip.com/556zxh.jpg)

---
template: section

## Βασικά στοιχεία

---
layout: true
template: chapter

### Βασικά στοιχεία

---

#### Δομή

H `Python` είναι μία γλώσσα με στόχο την απλότητα και την υψηλή αναγνωσιμότητα του κώδικα.

Εστω και μία απλή εντολή σε `Python` μπορεί να εκτελεστεί ως αυτόνομο πρόγραμμα, ένα χαρακτηριστικό γενικά των διερμηνευόμενων γλωσσών.

---

#### Δομή

Ακολουθεί τον κανόνα _off-side_ (football pun), σύμφωνα με τον οποίο τα blocks καθορίζονται από τη στοίχιση (_indentation_) του κώδικα.

Τα σχόλια στην `Python` ορίζονται με το χαρακτήρα `#`.

---
template: section

## Μεταβλητές

---
layout: true
template: chapter

### Μεταβλητές

---

#### Τύποι δεδομένων / μεταβλητών

Οι μεταβλητές, σε ένα πρόγραμμα, αναφέρονται σε περιοχές στη μνήμη, όπου το πρόγραμμά μας αποθηκεύει τα δεδομένα του.

Οι βασικοί τύποι μεταβλητών στην `Python` είναι οι εξής:

- `int` - ακέραιες τιμές
- `float` - αριθμοί κινητής υποδιαστολής
- `str` - αλφαριθμητικά
- `bool` - λογικές τιμές

---

#### Ονοματολογία

Το όνομα μιας μεταβλητής:

- αποτελείται μόνο από γράμματα (`a-z` & `A-Z`),
  <nobr>ψηφία (`0-9`)</nobr> και την κάτω παύλα (`_`).
- είναι _case sensitive_.
- δεν μπορεί να ξεκινά με ψηφίο (`0-9`)
- δεν μπορεί να είναι δεσμευμένη λέξη

---
class: long-text

#### Εκχώρηση / Ανάθεση

Η `Python` είναι μία δυναμική γλώσσα. Ο τύπος μιας μεταβλητής δε δηλώνεται πριν χρησιμοποιηθεί και μπορεί να αλλάξει κατά τη διάρκεια του προγράμματος.

Η εκχώρηση / ανάθεση τιμής γίνεται με το σύμβολο της ισότητας `=`.

Μπορεί να γίνει ταυτόχρονη ανάθεση, σε παραπάνω από μία μεταβλητές

```python
var1 = <value>
var1 = var2 = … = varn = <value>
```

---

#### Παράδειγμα

```python
a = 3                 # int
a = 3.14              # float

b = 'Python'          # str
b = "Python's great"  # str

b = """This is
a multiline
string"""             # str

c = True              # bool

e = f = 'We have the same value'

```

---
template: section

## Εκφράσεις

---
layout: true
template: chapter

### Εκφράσεις

---

#### Αριθμητικοί Τελεστές

| Τελεστής | Πράξη |
| --- | :-- |
| `+` | Πρόσθεση |
| `-` | Αφαίρεση |
| `*` | Πολλαπλασιασμός |
| `/` | Διαίρεση |
| `//` | Ακέραια διαίρεση |
| `%` | Modulo |
| `**` | Ύψωση σε δύναμη |

---

#### Τελεστές και `str`

| Τελεστής | Λειτουργία | Παράδειγμα |
| --- | :-- | :-- |
| `+` | Συνένωση | `'a' + 'b' => 'ab'` |
| `*` | Επανάληψη | `'a' * 3 => 'aaa'`  |

---

#### Ανάθεση & Τελεστής

| Τελεστής | Χρήση | Ισοδύναμα |
| --- | :-- | :-- |
| `+=` | `x += y` | `x = x + y` |
| `-=` | `x -= y` | `x = x - y` |
| `*=` | `x *= y` | `x = x * y` |
| `/=` | `x /= y` | `x = x / y` |
| `//=` | `x //= y` | `x = x // y` |
| `%=` | `x %= y` | `x = x % y` |
| `**=` | `x **= y` | `x = x ** y` |

---

#### Συγκριτικοί / Σχεσιακοί Τελεστές

| Τελεστής | Πράξη |
| --- | :-- |
| `==` | Ίσο με |
| `!=` | Διάφορο από |
| `>` | Μεγαλύτερο από |
| `<` | Μικρότερο από |
| `>=` | Μεγαλύτερο ή ίσο με |
| `<=` | Μικρότερο ή ίσο με |

---

#### Λογικοί Τελεστές

| A | B | A and B | A or B | not A |
| --- | --- | --- | --- | --- |
| `True` | `True` | `True` | `True` | _False_ |
| `True` | _False_ | _False_ | `True` | _False_ |
| _False_ | `True` | _False_ | `True` | `True` |
| _False_ | _False_ | _False_ | _False_ | `True` |

---

#### Ιεραρχία

1. Αριθμητικοί
    1. `**`
    1. `*`, `/`, `//`, `%`
    1. `+`, `-`
1. Συγκριτικοί
1. Λογικοί
    1. `not`
    1. `and`
    1. `or`

---
template: section

## Είσοδος / Έξοδος

---
layout: true
template: chapter

### Είσοδος / Έξοδος

---

#### Είσοδος

Για την είσοδο δεδομένων από το πληκτρολόγιο χρησιμοποιούμε τη συνάρτηση `input()`, η οποία παίρνει ως όρισμα το μήνυμα προτροπής που θα εμφανιστεί στην οθόνη.

Ανεξάρτητα από το τι θα πληκτρολογηθεί, η συνάρτηση επιστρέφει πάντα συμβολοσειρά `str` (στην έκδοση _3.x_). Αν θέλουμε να μετατραπεί σε κάτι άλλο, η μετατροπή αυτή πρέπει να γίνει με τις συναρτήσεις `int()`, `float()`, `bool()`.

Για λόγους πληρότητας, να αναφέρουμε και τη `str()`, που είναι χρήσιμη σε άλλες περιπτώσεις.

---

#### Παράδειγμα

```python
>>> x = input('Please enter a value: ')
Please enter a value: 10
>>> x
'10'
>>> x = int(x)
>>> x
10
>>> y = float(input('Amount: '))
>>> z = input('Enter your name: ')

```

---

#### Έξοδος

Για την εμφάνιση ενός ή περισσότερων στοιχείων στην οθόνη, χρησιμοποιούμε τη συνάρτηση `print()` (έκδοση _3.x_). Η εμφάνιση των στοιχείων μπορεί να παραμετροποιηθεί με τα ορίσματα `sep` (_separator char_) και `end` (_end char_).

##### Σύνταξη

```python
print(στοιχεία, sep=' ', end='\n')

```

`sep`: διαχωριστής,
`end`: τερματικός χαρακτήρας

---

#### Παράδειγμα

```python
>>> a = 3
>>> b = 8
>>> print(a)
3
>>> print(a, b)
3 8
>>> print(a, b, sep=', ', end='.')
3, 8.

```

---
template: section

## Συναρτήσεις

---
layout: true
template: chapter
name: functions

### Συναρτήσεις

---

#### Βασικές ενσωματωμένες συναρτήσεις

| Συνάρτηση | Λειτουργία |
| --- | :-- |
| `abs(x)` | Απόλυτη τιμή του `x` |
| `pow(a,n)` | Ύψωση του `a` στη `n` |
| `divmod(x,y)` | Ακέραια διαίρεση & modulo (πλειάδα) |
| `round(a,n)` | Στρογγυλοποίηση του `a` με ακρίβεια `n` |

---

#### Παράδειγμα

```python
>>> abs(-9)
9
>>> pow(3, 3)
27
>>> divmod(15, 6)
(2, 3)
>>> round(3.5, 0)
4.0
>>> round(4.5, 0)
4.0

```

---
#### Μαθηματικές συναρτήσεις

Άλλες μαθηματικές συναρτήσεις είναι διαθέσιμες μέσω της βιβλιοθήκης `math`.

```python
>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.floor(4.9)
4
>>> math.ceil(4.9)
5
>>> math.sqrt(9)
3.0

```

---

#### Μαθηματικές βιβλιοθήκες

Επίσης χρήσιμη είναι και η βιβλιοθήκη `random`.

```python
>>> import random
>>> random.randint(1, 8)
7
>>> random.random()
0.3031134844827079

```

---
layout: true
template: functions

#### Συναρτήσεις συμβολοσειρών

---

| Συνάρτηση | Λειτουργία |
| :-- | :-- |
| `len(s)` | Μήκος συμβολοσειράς |
| `ord(a)` | Μετατροπή του χαρακτήρα `a` σε _unicode_ |
| `chr(n)` | "Αντίστροφη" λειτουργία από τη `ord` |

---

| Συνάρτηση | Λειτουργία |
| :-- | :-- |
| `s.isalpha()` | Αποτελείται μόνο από γράμματα; |
| `s.isdigit()` | Αποτελείται μόνο από ψηφία; |
| `s.islower()` | Αποτελείται μόνο από πεζά; |
| `s.upper()` | Μετατροπή σε κεφαλαία |
| `s.lower()` | Μετατροπή σε πεζά |
| `s.capitalize()` | Μετατροπή του πρώτου χαρακτήρα σε κεφαλαίο |

---
class: long-text

| Συνάρτηση | Λειτουργία |
| :-- | :-- |
| `s.count(key,start=0,end=len(s))` | Πόσες φορές υπάρχει το `key` |
| `s.find(key,start=0,end=len(s))` | Αναζήτηση για το `key` |
| `s.startswith(key,start=0,end=len(s))` | Έλεγχος αν ξεκινά με `key` |
| `s.replace(old,new[,max])` | Αντικατάσταση |
| `s.strip(chr=' ')` | Αφαίρεση χαρακτήρων από τα άκρα |

---

| Συνάρτηση | Λειτουργία |
| :-- | :-- |
| `s.decode(encoding='UTF-8', errors='strict')` | Κωδικοποίηση |
| `s.encode(encoding='UTF-8', errors='strict')` | Αποκωδικοποίηση |

---

| Συνάρτηση | Λειτουργία |
| :-- | :-- |
| `sep.join(s)` | Συνένωση |
| `s.split(sep="", max=s.count(sep))` | Διαχωρισμός |

---
template: section

## Μορφοποίηση

---
layout: true
template: chapter

### Μορφοποίηση

---

#### string `%` operator

Μια παλαιότερη τεχνική, ήταν η μορφοποίηση με τη χρήση του τελεστή `%`

```python
>>> print('Bought %d %s for €%.2f' % (2, 'BTC', 50102.24))
Bought 2 BTC for €50102.24

```

Θυμίζει `C` και θεωρείται, πλέον, παρωχημένος τρόπος μορφοποίησης.

---

#### `.format()` method

Νεότερη τεχνική είναι η χρήση της μεθόδου `.format()` του `str`, είτε με _positional arguments_…

```python
>>> print('Bought {0} {1} for €{2:,.2f}'
      .format(2, 'BTC', 100204.48))
Bought 2 BTC for €100,204.48

```

Προσοχή στην προσθήκη του `,` στο `{2:,.2f}`

Μη βασίζεστε στην στρογγυλοποίηση μέσω του `{2:,.2f}`!

---

#### `.format()` method

… είτε με _keyword arguments_.

```python
>>> print('Bought {n} {coin} for €{cost:,.2f}'
      .format(n=2, coin='BTC', cost=100204.48))
Bought 2 BTC for €100,204.48

```

---

#### `f-strings`

Από την έκδοση _3.6_ και μετά, υπάρχει και η δυνατότητα μορφοποίησης με _formatted string literal_ ή αλλιώς _f-strings_.

```python
>>> n = 2
>>> coin = 'BTC'
>>> cost = 100204.48
>>> print(f'Bought {n} {coin} for €{cost:,.2f}')
Bought 2 BTC for €100,204.48

```

---

#### `f-strings`

Στα `f-strings` τα _placeholders_ δεν είναι απλά _keyword arguments_, αλλά μπορούν να δεχθούν οποιαδήποτε έκφραση.

```python
>>> n = 2
>>> coin = 'BTC'
>>> cost_each = 50102.24
>>> print(f'Bought {n} {coin} for €{(cost_each * n):.2f}')
Bought 2 BTC for €100204.48

```

---
template: section

## Homework

---
template: chapter

### Homework #1

#### Στοιχεία κύκλου

Γράψτε ένα πρόγραμμα σε `Python` το οποίο να ζητά την ακτίνα ενός κύκλου και να εμφανίζει την περίμετρο και το εμβαδόν του.

> _Περίμετρος_: circumference = 2· π· R
>
> _Εμβαδόν_: area = π· R<sup>2</sup>

---
template: chapter

### Homework #2

#### Μετατροπή νομίσματος

Σε κάποιο σύστημα τα ποσά εμφανίζονται σε λάθος μορφή, λόγω κάποιου software bug. Γράψτε ένα πρόγραμμα σε `Python` το οποίο να μετατρέπει ένα ποσό, από τη μορφή `$12,345.67` στη μορφή `€12.345,67`, με τα εξής βήματα:

1. να αφαιρεί τυχόν κενά από την αρχή και το τέλος του `string`
1. να αντικαθιστά την `.` με `,` και το ανάποδο (προσοχή, είναι λίγο δυσκολότερο από ότι φαίνεται αρχικά).
1. να αντικαθιστά το `$` με `€`.

---
template: list

### Χρήσιμα links

- ![](https://www.google.com/s2/favicons?domain=python.org) 3.x Documentation https://docs.python.org/3/
- ![](https://www.google.com/s2/favicons?domain=python.org) The Python Standard Library https://docs.python.org/3/library/
- ![](https://www.google.com/s2/favicons?domain=w3schools.com) Python Data Types https://www.w3schools.com/python/python_datatypes.asp
- ![](https://www.google.com/s2/favicons?domain=python.org) Built-in Functions https://docs.python.org/3/library/functions.html#bool
- ![](https://www.google.com/s2/favicons?domain=python.org) Numeric and Mathematical Modules https://docs.python.org/3/library/numeric.html
- ![](https://www.google.com/s2/favicons?domain=pyhurry.readthedocs.io) Strings — Python in a Hurry https://pyhurry.readthedocs.io/en/latest/strings.html
- ![](https://www.google.com/s2/favicons?domain=tutorialspoint.com) Python - Strings - Tutorialspoint https://www.tutorialspoint.com/python/python_strings.htm
- ![](https://www.google.com/s2/favicons?domain=realpython.com) A Guide to the Newer Python String Format Techniques – Real Python https://realpython.com/python-formatted-output/

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=en.wikipedia.org) Off-side rule - Wikipedia https://en.wikipedia.org/wiki/Off-side_rule
- ![](https://www.google.com/s2/favicons?domain=quora.com) Why doesn't 0.1+0.2-0.3 equal 0.0 in Python? - Quora https://www.quora.com/Why-doesnt-0-1-0-2-0-3-equal-0-0-in-Python
- ![](https://www.google.com/s2/favicons?domain=stackoverflow.com) Exponentials in python: x**y vs math.pow(x, y) - Stack Overflow https://stackoverflow.com/questions/20969773/exponentials-in-python-xy-vs-math-powx-y
- ![](https://www.google.com/s2/favicons?domain=learnbyexample.org) Python round() Function - Learn By Example https://www.learnbyexample.org/python-round-function/
- ![](https://www.google.com/s2/favicons?domain=stackabuse.com) How to Format Number as Currency String in Python https://stackabuse.com/format-number-as-currency-string-in-python/

---
template: section

## Thank You!
