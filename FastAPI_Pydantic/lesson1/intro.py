from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

# Example 1:
@app.get("/name")
#def read_api():
#    return {'Welcome': 'Emmanuel'} 
def read_api(name: str):
    return {"Welcome": f'Hello {name}, welcome to the Book API!'}