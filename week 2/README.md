# Week 2 — Object-Oriented Python

Three command-line apps I built while learning **classes and objects** — the
core idea of Object-Oriented Programming. Instead of loose functions and data,
each project bundles data and the actions on it together into classes like
`Book`, `Account`, and `Question`. Everything runs on plain **Python 3**.

---

## Projects

### 1. Library Management — `Library.py`
A small library system. Add books, search by title or author, borrow and return
books, and see what's available. Built with a `Book` class (one book) and a
`Library` class (holds all the books and the actions on them).

**Features**
- Add a book
- Show all books
- Search by title or author
- Borrow a book (blocked if it's already borrowed)
- Return a book

**Run**
```bash
python3 Library.py
```

---

### 2. Bank Account System — `Bank.py`
A simple bank. Create accounts, deposit, withdraw, transfer money between
accounts, and view each account's transaction history. Built with an `Account`
class (one person's balance and history) and a `Bank` class (holds all accounts
and handles transfers).

**Features**
- Create an account
- Deposit money
- Withdraw money (blocked if there isn't enough balance)
- Transfer money between accounts
- Print transaction history

**Run**
```bash
python3 Bank.py
```

---

### 3. Quiz App — `Quiz.py`
A multiple-choice quiz that loads its questions from a JSON file, asks them one
by one, tracks your score, and saves every attempt. Built with a `Question`
class that stores a question, its options, and the correct answer.

**Features**
- Loads questions from `questions.json`
- Asks each question in the terminal
- Tracks the score
- Shows the final result
- Saves each attempt (name, score, date) to `attempts.json`

**Run**

Keep `Quiz.py` and `questions.json` in the same folder, then:
```bash
python3 Quiz.py
```

---

## What I learned
- Defining classes with `__init__` and `self`
- Storing data inside objects (a book's status, an account's balance)
- Methods that act on an object's own data
- One class holding many objects of another class (a Library of Books, a Bank of Accounts)
- Loading JSON data and turning it into objects

## Tech
- Python 3 (no external libraries required)
