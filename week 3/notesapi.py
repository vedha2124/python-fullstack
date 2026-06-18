# Week 3 - notes API
# CRUD for little notes, each one has a title, content and a tag you can filter by
# run:  uvicorn notesapi:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Notes API")


class NoteIn(BaseModel):
    title: str
    content: str
    tag: str


notes = []   # was accidentally inside the class before - has to be out here


def get_next_id():
    highest = 0
    for note in notes:
        if note["id"] > highest:
            highest = note["id"]
    return highest + 1


@app.get("/")
def home():
    return {"message": "Welcome! Open /docs to try the API."}


@app.post("/notes")
def create_note(note: NoteIn):
    new_note = {
        "id": get_next_id(),
        "title": note.title,
        "content": note.content,
        "tag": note.tag,
    }
    notes.append(new_note)
    return new_note


@app.get("/notes")
def get_notes(search: str = None, tag: str = None):
    # search looks in the title, tag has to match exactly
    result = []
    for note in notes:
        if search is not None and search.lower() not in note["title"].lower():
            continue
        if tag is not None and note["tag"].lower() != tag.lower():
            continue
        result.append(note)
    return result


@app.put("/notes/{note_id}")
def edit_note(note_id: int, updated: NoteIn):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = updated.title
            note["content"] = updated.content
            note["tag"] = updated.tag
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Note deleted"}
    raise HTTPException(status_code=404, detail="Note not found")
