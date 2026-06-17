# Week 3 — FastAPI Basics

Three web APIs I built while learning **FastAPI** — moving from command-line
programs to real web servers that respond to HTTP requests. Each project is a
working REST API you can open in the browser and test live.

> Note: data is stored in memory (a Python list), so it resets every time the
> server restarts. A real database is added in Week 4.

---

## Setup (once)

```bash
python3 -m pip install fastapi "uvicorn[standard]"
```

## Running any project

Go into the project's folder and start the server. The name before `:app` must
match the **filename** (without `.py`):

```bash
python3 -m uvicorn FILENAME:app --reload
```

Then open **http://127.0.0.1:8000/docs**. FastAPI auto-builds an interactive
page where every endpoint has a **"Try it out"** button — no Postman or curl
needed.

---

# 1. Todo API — `todoAPI.py`

A REST API to manage a todo list. You can create todos, read them, mark them
done, and delete them.

### How the data is stored
Everything lives in one Python list called `todos`. Each todo is a dictionary:

```json
{ "id": 1, "title": "Buy milk", "done": false }
```

- `id` — a unique number the API assigns automatically
- `title` — the text you send
- `done` — starts as `false`, becomes `true` when you complete it

When a new todo is created, a small helper `get_next_id()` loops through the
existing todos, finds the highest id, and adds 1 — so every todo gets a unique,
ever-increasing number even after deletions.

### Endpoints, step by step

**`POST /todos` — create a todo**
You send a body: `{ "title": "Buy milk" }`. The API builds a new todo with the
next id and `done` set to false, adds it to the list, and returns it.
- Response: `{ "id": 1, "title": "Buy milk", "done": false }`

**`GET /todos` — get all todos**
Returns the whole list as it is. If empty, you get `[]`.

**`GET /todos/{id}` — get one todo**
You put the id in the URL, e.g. `/todos/1`. The API loops through the list
looking for a matching id. If found, it returns that todo; if not, it returns a
**404 Not Found** with the message "Todo not found".

**`PUT /todos/{id}` — update a todo**
You send a body: `{ "title": "Buy almond milk", "done": true }`. The API finds
the todo by id and overwrites its title and done status, then returns the
updated todo. Returns 404 if the id doesn't exist.

**`DELETE /todos/{id}` — delete a todo**
Finds the todo by id, removes it from the list, and returns
`{ "message": "Todo deleted" }`. Returns 404 if the id doesn't exist.

### Run it
```bash
python3 -m uvicorn todoAPI:app --reload
```

**Teaches:** the four core actions (GET/POST/PUT/DELETE), path parameters
(`/todos/1`), request bodies, Pydantic validation, and 404 handling.

---

# 2. Notes API — `notesapi.py`

A REST API to manage notes. Each note has a title, some content, and a tag (like
"work" or "shopping"). On top of create/edit/delete, it can **search by title**
and **filter by tag**.

### How the data is stored
A Python list called `notes`, where each note is a dictionary:

```json
{ "id": 1, "title": "Groceries", "content": "milk, eggs, bread", "tag": "shopping" }
```

Ids are assigned the same way as the Todo API (a `get_next_id()` helper).

### Endpoints, step by step

**`POST /notes` — create a note**
You send `{ "title": "...", "content": "...", "tag": "..." }`. The API gives it
the next id, saves it, and returns it.

**`GET /notes` — list notes (with optional search and filter)**
This is the interesting one. It accepts two **optional query parameters**:
- `?search=milk` — keeps only notes whose **title contains** that word
- `?tag=shopping` — keeps only notes whose tag **exactly matches**

Here's how it works internally: the API starts an empty result list and loops
through every note. For each note it asks two questions — "if a search word was
given, does the title contain it?" and "if a tag was given, does it match?" If a
note fails either test, it's skipped; otherwise it's added to the results. Both
checks are case-insensitive.

So you can call it four ways:
- `/notes` — all notes
- `/notes?search=milk` — notes with "milk" in the title
- `/notes?tag=shopping` — notes tagged shopping
- `/notes?search=milk&tag=shopping` — both filters at once

**`PUT /notes/{id}` — edit a note**
Send the full note body. The API finds it by id and overwrites title, content,
and tag. Returns 404 if not found.

**`DELETE /notes/{id}` — delete a note**
Finds it by id, removes it, returns a confirmation message. 404 if not found.

### Run it
```bash
python3 -m uvicorn notesapi:app --reload
```

**Teaches:** query parameters, combining multiple optional filters, and
case-insensitive searching.

---

# 3. Product Catalog API — `productcatalog.py`

A REST API to manage a product catalog. You can add products, list them, search
by name, filter by category, update just the price, and delete products.

### How the data is stored
A Python list called `products`, where each product is a dictionary:

```json
{ "id": 1, "name": "Running Shoes", "category": "footwear", "price": 2999.0 }
```

Ids are assigned with the same `get_next_id()` helper.

### Endpoints, step by step

**`POST /products` — add a product**
You send `{ "name": "...", "category": "...", "price": 2999 }`. Pydantic checks
that `price` is actually a number (it rejects text). The API assigns the next id,
saves it, and returns it.

**`GET /products` — list products (with optional search and filter)**
Like the Notes API, it accepts two optional query parameters:
- `?search=shoe` — keeps products whose **name contains** that word
- `?category=footwear` — keeps products whose category **exactly matches**

It loops through every product and skips any that fail a given filter. Examples:
- `/products` — everything
- `/products?search=shoe` — products with "shoe" in the name
- `/products?category=footwear` — products in that category
- `/products?search=shoe&category=footwear` — both at once

**`PUT /products/{id}/price` — update only the price**
A focused endpoint. The URL points to a specific product (`/products/1/price`)
and the body carries just the new price: `{ "price": 2499 }`. The API finds the
product by id, changes its price, and returns the updated product. 404 if the id
doesn't exist. (Notice the URL itself describes the action — "the price of
product 1".)

**`DELETE /products/{id}` — delete a product**
Finds it by id, removes it, returns a confirmation. 404 if not found.

### Run it
```bash
python3 -m uvicorn productcatalog:app --reload
```

**Teaches:** mixing all three input styles in one API — **path** parameters
(`/products/1`), **query** parameters (`?category=footwear`), and **request
bodies** (the new price) — plus type validation.

---

## What I learned across all three
- Building web APIs with FastAPI and running them with Uvicorn
- The four HTTP methods: GET (read), POST (create), PUT (update), DELETE (remove)
- Three ways to send data: path parameters, query parameters, and request bodies
- Pydantic models that validate incoming data automatically
- Returning proper 404 errors when something isn't found
- The auto-generated interactive docs at `/docs`

## Tech
- Python 3
- FastAPI
- Uvicorn
