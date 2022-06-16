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

# Databases #1

### RDBMSs

---
template: section

## Περιεχόμενα

---
layout: true
template: section-details

### Περιεχόμενα

---

- RDBMs
  - Γενικά
  - DB Structure
  - DB Elements
  - Relationships
- SQL
  - DDL
  - DML
  - DQL

---
template: section

## Databases

---
layout: true
template: chapter

### Databases

---

#### Γενικά

- Βάση δεδομένων χαρακτηρίζουμε ένα σύστημα οργάνωσης και αποθήκευσης δεδομένων.
- Σε μια βάση δεδομένων έχουμε τη δυνατότητα να αποθηκεύσουμε διαφορετικού τύπου δεδομένα τα οποία σχετίζονται με κάποιο τρόπο.
- Πίσω από κάθε δυναμικό website κρύβεται μια database.

---
layout: true
template: chapter

### RDBMSs

---

#### Relational Database Management Systems

Οι πιο "παραδοσιακές" βάσεις δεδομένων είναι οι σχεσιακές βάσεις.

- `MS SQL Server`
- `MS Access`
- `MySQL` / `MariaDB`
- `Oracle DB`
- `PostgreSQL`
- `SQLite`

---

#### Database Structure

![Database Structure](assets/lecture-08/img/structure.png)

---

#### Database Elements

Σε μια σχεσιακή βάση δεδομένων:

- `Tables` - Τα δεδομένα της βάσης οργανώνονται σε πίνακες (_relations_). Κάθε πίνακας κρατά (συνήθως) τα στοιχεία που αναφέρονται σε μια συγκεκριμένη οντότητα της εφαρμογής μας.
- `Records` - Κάθε πίνακας αποτελείται από γραμμές (_rows_) ή αλλιώς εγγραφές (_records_), όπου η κάθεμία από αυτές αναγνωρίζεται από ένα μοναδικό στοιχείο κλειδί.

---

#### Database Elements

Σε μια σχεσιακή βάση δεδομένων:

- `Columns` - Κάθε εγγραφή χωρίζεται σε στήλες (_records_) ή πεδία (_fields_). Κάθε πεδίο αντιστοιχεί σε μία ιδιότητα της οντότητας που αντιπροσωπεύει ο πίνακας ή έχει κάποιο βοηθητικό ρόλο (κλειδιά, ευρετήρια κ.λπ).
- `Data/Values` - Τα πεδία κρατούν τιμές. Κάθε πεδίο έχει τύπο που υπαγορεύει της τιμές που μπορεί να δεχθεί. Μια τιμή μπορεί να είναι υποχρεωτική ή και όχι.

---

#### Field Types

Οι τύποι για πεδία πινάκων είναι κυρίως:

- `Int`, `Bigint`
- `Decimal`, `Float`, `Double`
- `Char`, `Varchar`, `Text`
- `Boolean`
- `Date`, `DateTime`

---
template: section

## Relationships

---
layout: true
template: chapter

### Relationships

---

#### Primary Key

- Κάθε πίνακας "πρέπει" να έχει ένα πεδίο που θα παίρνει την ιδιότητα του _πρωτεύοντος κλειδιού_.
- Είναι ένα πεδίο που δέχεται μοναδικές τιμές (ανά πίνακα), ώστε κάθε εγγραφή να προσδιορίζεται μοναδικά.
- Μπορεί να είναι μια ιδιότητα της οντότητας (π.χ. το ΑΦΜ ενός πελάτη) ή μπορεί να είναι ένα αναγνωριστικό κατασκευασμένο από εμάς (π.χ. κωδικός πελάτη).

---

#### Foreign Key

- Όταν αναφερόμαστε σε μια εγγραφή από άλλον πίνακα, κάνουμε χρήση των _δευτερευόντων κλειδιών_.
- Ένα δευτερεύον κλειδί αναφέρεται στο πρωτεύον κλειδί ενός άλλου πίνακα.
- Με τα δευτερεύοντα κλειδιά εκφράζουμε τις σχέσεις μεταξύ των οντοτήτων της εφαρμογής μας.

---

#### Relationship Types

![Relations](assets/lecture-08/img/relationships.png)

---
template: section

## Relationship Types

---
layout: true
template: chapter

### Relationship Types

---

#### Κατηγορίες

- `1-1`: μια εγγραφή από τον πίνακα Α έχει σχέση μόνο με μια εγγραφή από τον πίνακα Β
- `1-Many`: μια εγγραφή από τον πίνακα Α έχει σχέση με πολλές εγγραφές του πίνακα Β
- `Many-Many`: πολλές εγγραφές του πίνακα Α έχουν σχέση με πολλές εγγραφές του πίνακα Β

---

### Relationship Types

#### Παραδείγματα

- `1-1`: Κάθε προϊόν το παραγγέλνουμε από έναν συγκεκριμένο προμηθευτή & αυτός ο προμηθευτής μας δίνει μόνο αυτό το προϊόν.
- `1-Many`: Κάθε προϊόν το παραγγέλνουμε από έναν προμηθευτή ο οποίος μας φέρνει περισσότερα από ένα προϊόντα.
- `Many–Many`: Πολλά προϊόντα τα παραγγέλνουμε από πολλούς προμηθευτές (διαφορετικούς) και αντίστοιχα κάθε προμηθευτής μας δίνει πολλά προϊόντα.

---

#### Παραδείγματα

- Διαχειρίζεστε ένα eshop με είδη για υπολογιστές.
  - Ποιοι είναι οι απαραίτητοι πίνακες;
  - Τι πεδία έχει κάθε πίνακας;
- Διαχειρίζεστε ένα εστιατόριο που κάνει delivery
  - Ποιοι είναι οι απαραίτητοι πίνακες;
  - Τι πεδία έχει κάθε πίνακας;
- Διαχειρίζεστε ένα μαγαζί με ρούχα
  - Ποιοι είναι οι απαραίτητοι πίνακες;
  - Τι πεδία έχει κάθε πίνακας;

---
template: section

## SQL

---
layout: true
template: chapter

### SQL

---

#### `Structured Query Language`

- Η `SQL` είναι η γλώσσα που μας επιτρέπει να διαχειριστούμε μια βάση δεδομένων.
- `SQL` μπορούμε να γράψουμε είτε κατευθείαν στον κώδικά μας είτε σε κάποιο Database Manager λογισμικό.
- Υπάρχουν διάφορες εκδόσεις/διάλεκτοι/επεκτάσεις της `SQL`, `T-SQL`, `PL/SQL`, κ.α.

---

#### Κατηγορίες

Η `SQL` έχει εντολές που χωρίζονται στις εξής κατηγορίες:

- `DDL` – Data Definition Language
- `DQL` – Data Query Language
- `DML` – Data Manipulation Language
- `DCL` – Data Control Language

---
template: section

## DDL

---
class: long-text

#### Basic `DDL`

| Explanation  | Querry |
| - | - |
| Create Database | `CREATE DATABASE DatabaseName;` |
| Delete Database | `DROP DATABASE DatabaseName;` |

---

#### Δημιουργία πίνακα

Κατά τη δημιουργία ενός πίνακα, δηλώνουμε τη λίστα των πεδίων του, μαζί με τον τύπο του, το μέγεθός τους καθώς και τη δυνατότητα να παραμείνουν κενά ή όχι.

Στο τέλος της λίστας αναφέρεται και το _πρωτεύον κλειδί_ του πίνακα.

```sql
CREATE TABLE customers (
    id INT NOT NULL,
    name VARCHAR (20) NOT NULL,
    Age INT NOT NULL,
    PRIMARY KEY (Id)
);

```

---

#### Διαγραφή πίνακα

```sql
DROP TABLE customers;

```

---
class: long-text

#### Τροποποίηση πίνακα

| Query | Explanation |
| - | - |
| `ALTER TABLE table_name ADD column_name datatype` | Add Column to table |
| `ALTER TABLE table_name DROP COLUMN column_name` | Delete column from table |
| `ALTER TABLE table_name ALTER COLUMN column_name datatype` | Alter column from table |
| `DROP TABLE table_name` | Delete table from Database |

---
template: section

## DML

---

#### Εισαγωγή Δεδομένων

```sql
-- Με λίστα των πεδίων
INSERT INTO table_name (column1, column3,...)
VALUES (value1, value3,...);

-- Χωρίς να δηλωθεί η λίστα των πεδίων,
-- θέλει προσοχή στη σειρά
INSERT INTO table_name VALUES (value1, value2, value3,...);

```

---

#### Ενημέρωση δεδομένων

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2,
    …
WHERE some_column = some_value;

```

---

#### Διαγραφή Δεδομένων

```sql
-- Διαγραφή εγγραφής με δεδομένο κλειδί
DELETE FROM products
WHERE id = 10;

-- Διαγραφή όλω των στοιχείων του πίνακα
-- Προσοχή!
DELETE FROM products;

```

---
template: section

## DQL

---

#### Ανάκτηση Δεδομένων

```sql
-- Ανάκτηση όλων των στοιχείων από πίνακα
SELECT *
FROM products;

-- Θα φέρει τις στήλες name και price
-- από όλες τις εγγραφές του πίνακα
SELECT name, price
FROM products;

```

---

#### Ανάκτηση Δεδομένων

```sql
-- Θα ανακτήσει το όνομα των προϊόντων
-- των οποίων η τιμή ισούται με 10
SELECT name
FROM products
WHERE price = 10;

-- Ανάκτηση των εγγραδών πίνακα
-- όπου το όνομα ξεκινά από A`
SELECT *
FROM products
WHERE name LIKE 'A%';

```

---

#### Wildcards & `LIKE` operator

- Ο τελεστής `LIKE` χρησιμοποιείται στο `WHERE` clause όταν δεν γνωρίζουμε ακριβώς το κριτήριο που αναζητάμε.
- Χρησιμοποιεί _wildcards_ (ειδικούς χαρακτήρες) που μας επιτρέπουν να ελέγχουμε τα αποτελέσματα που θα φέρει το SQL query.

---

#### Wildcards & `LIKE` operator

| Wildcard | Description |
|:-:| - |
| `%` | Περιγραφή οποιουδήποτε χαρακτήρα |
| `_` | Περιγραφή ενός μόνο χαρακτήρα |

---

#### `IN` operator

Ο τελεστής `IN` είναι χρήσιμος όταν θέλουμε να αναζητήσουμε για μια σειρά από τιμές

```sql
SELECT *
FROM customers
WHERE city IN ('Athens', 'Paris');

```

---

#### `BETWEEN` operator

Όταν μας ενδιαφέρει ένα εύρος τιμών, και όχι κάποιες συγκεκριμένες, μπορούμε να κάνουμε χρήση του τελεστή `BETWEEN`

```sql
SELECT *
FROM customers
WHERE age BETWEEN 20 AND 30;

```

---

#### Logical operators

Για πιο σύνθετα ερωτήματα, είναι δυνατή η προσθήκη των λογικών τελεστών `AND`, `OR` και `NOT`

```sql
SELECT * FROM customers
WHERE first_name = 'John' AND last_name = 'Doe';

SELECT * FROM customers
WHERE age > 18 OR name = 'Benjamin Button';

SELECT * FROM customers
WHERE country NOT LIKE 'United%'

```

---
template: section

## Homework

---
layout: true
template: chapter

### Homework

---

#### Homework

- Σχεδιάστε μια βάση δεδομένων για ένα website ειδήσεων.
- Το website θα πρέπει να αποθηκεύει τα παρακάτω δεδομένα σε πίνακες:
  - Νέα/Άρθρα χωρισμένα σε κατηγορίες (με ειδικό flag για τα hot news)
  - Συντάκτες των άρθρων/νέων που θα είναι συνδεδεμένοι με τα νέα
  - Επισκέπτες που θα μπορούν να σχολιάσουν τα νέα
  - Σχόλια των επισκεπτών

---

template: list

### Χρήσιμα links

- ![](https://www.google.com/s2/favicons?domain=www.tutorialspoint.com) SQL - RDBMS Concepts - Tutorialspoint https://www.tutorialspoint.com/sql/sql-rdbms-concepts.htm
- ![](https://www.google.com/s2/favicons?domain=www.geeksforgeeks.org) SQL | DDL, DQL, DML, DCL and TCL Commands - GeeksforGeeks https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/
- ![](https://www.google.com/s2/favicons?domain=www.w3schools.com) SQL Introduction https://www.w3schools.com/sql/sql_intro.asp

---
template: list

### Extra info

- ![](https://www.google.com/s2/favicons?domain=www.sqlite.org) Datatypes In SQLite Version 3 https://www.sqlite.org/datatype3.html
- ![](https://www.google.com/s2/favicons?domain=www.sqlite.org) Query Language Understood by SQLite https://www.sqlite.org/lang.html
- ![](https://www.google.com/s2/favicons?domain=www.sqlitetutorial.net) SQLite Tutorial - An Easy Way to Master SQLite Fast https://www.sqlitetutorial.net/
- ![](https://www.google.com/s2/favicons?domain=en.wikipedia.org) Database normalization - Wikipedia https://en.wikipedia.org/wiki/Database_normalization
- ![](https://www.google.com/s2/favicons?domain=www.ibm.com) ACID properties of transactions - IBM Documentation https://www.ibm.com/docs/en/cics-ts/5.4?topic=processing-acid-properties-transactions

---
template: section

## Thank You!
