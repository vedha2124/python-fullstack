# Week 1 — Python Core

Three command-line apps I built while learning the fundamentals of Python:
variables, loops, functions, dictionaries, file handling, JSON, and error
handling. No external libraries — everything runs on plain **Python 3**.

---

## Projects

### 1. Student Marks Manager — `StudentMarks.py`
Add students and their marks, and the program works out each student's total,
average, and whether they passed or failed. All data is saved to a JSON file so
it stays between runs.

**Features**
- Add a student with marks for any number of subjects
- Calculates total and average automatically
- Shows PASS / FAIL (pass mark = 35 in every subject)
- Saves all data to `students.json`

**Run**
```bash
python3 StudentMarks.py
```

---

### 2. Expense Tracker — `ExpenseTracker.py`
Record what you spend (amount, category, date), then view your total for any
month and how much went to each category. Expenses are saved to a JSON file.

**Features**
- Add an expense
- Show all expenses
- Total for a chosen month
- Spending broken down by category
- Saves all data to `expenses.json`

**Run**
```bash
python3 ExpenseTracker.py
```
Dates are typed as `YYYY-MM-DD` (e.g. 2026-06-14) and a month as `YYYY-MM`.

---

### 3. File Organizer — `FileOrganiser.py`
Tidies a messy folder by moving every file into a subfolder based on its type
(Images, PDFs, Documents, Videos, Music, Others) and writing a log of what moved.

**Features**
- Sorts files into folders by type
- Creates the type folders automatically
- Skips the log file and any `.py` files
- Writes every move to `log.txt`

**Run**
```bash
python3 FileOrganiser.py
```
Then paste the full path of the folder you want to organize.

> ⚠️ This script actually **moves** your files. Test it on a copy/junk folder first.

---

## What I learned
- Variables, loops, and functions
- Lists and dictionaries
- Reading and writing JSON files
- Basic error handling with `try` / `except`
- Working with files and folders using `os` and `shutil`

## Tech
- Python 3 (no external libraries required)
