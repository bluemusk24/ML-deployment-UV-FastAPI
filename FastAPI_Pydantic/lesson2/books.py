# RESTFUL API with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()
BOOK = []

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

# Get method
@app.get("/")
def read_api():
    return BOOK


# Post method
@app.post("/")
def create_book(book: Book):
    BOOK.append(book)
    return book

# Add Put method to update existing book. Also HHTP errors handling is need here, so import above HTTPException from fastapi
@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOK:
        counter += 1
        if x.id == book_id:
            BOOK[counter - 1] = book
            return BOOK[counter - 1]
    raise HTTPException(
        status_code=404,
        detail=f"Book with id {book_id} not found"
    )

# Add Delete method to delete existing book
@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0

    for x in BOOK:
        counter += 1
        if x.id == book_id:
            del BOOK[counter - 1]
            return f"Book with id {book_id} has been deleted"
    raise HTTPException(
        status_code=404,
        detail=f"Book with id {book_id} not found"
    )