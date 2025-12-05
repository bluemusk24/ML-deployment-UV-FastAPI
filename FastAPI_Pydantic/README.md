### Project Description:

This project showcases a production-grade ```FastAPI``` application built with a focus on scalability, security, and clean architecture. It includes core functionalities such as user authentication, database integration, and media management.

All image and video operations are handled using [ImageKit](https://imagekit.io/registration/?utm_source=youtube.com&utm_medium=cpc&utm_campaign=YTInfluencers_25Q3&utm_term=techwithtim&utm_content=fastpiimagekit_reglink)
 — an AI-powered Digital Asset Management (DAM) platform that provides APIs for optimized storage, transformation, and delivery of media assets.

### Project Requirements:
```bash
uv init
uv add fastapi python-dotenv fastapi-users[sqlalchemy] imagekitio uvicorn[standard] aiosqlite
uv sync
```
```.env``` file.

### Testing FASTAPI

* create [app_script](app\app.py) and with the test codes below:
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello-world')
def hello_world():
    return {"message": "Hello, World!"}


# main.py code
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)


# Run main.py
uv run main.py

# edited app.py
from fastapi import FastAPI

app = FastAPI()

text_posts = {}

@app.get("/posts")
def get_all_posts():
    return text_posts

# open the FASTAPI URL
http://localhost:8000/docs
```

## Lesson 1: Introduction
[intro_script](lesson1\intro.py)

* update [main.py](main.py) ---> ```uvicorn.run('lesson1.intro:app', host='0.0.0.0', port=8000, reload=True)```

```bash
uv run main.py          # or python main.py
``` 

## Lesson 2: Build Modern Restful APIs

[books_script](lesson2\books.py)

* update [main.py](main.py) --> ```uvicorn.run('lesson2.books:app', host='0.0.0.0', port=8000, reload=True)``` 

```bash
uv run main.py          # or python main.py
``` 

## Lesson 3: Connect FastAPI to a SQLite Database

[database_script](lesson3_sqlite\database.py)

[models.py](lesson3_sqlite\models.py)

[books_script](lesson3_sqlite\books.py)

* update [main.py](main.py) --> ```uvicorn.run('lesson3.books:app', host='0.0.0.0', port=8000, reload=True)``` 

```bash
uv run main.py          # or python main.py
``` 

## Lesson 4: Connect FastAPI to a NoSQL Database (MongoDB)

[https://www.mongodb.com/cloud/atlas/register](MongoDB Sign up) --> Cloud NoSql Database
* Watch Lecture video for more tutorial

## Lesson 5: Build a FastAPI app with PostgreSQL Relational Database (Creating a Question Answer Database)

* Watch Lecture video for more tutorial

```bash
uv add psycopg2-binary

# Install pgAdmin on root dir
uv pip install pgadmin4

# run this in working and input any email and password
pgadmin4
```
* Note: you should get the below when you start pgadmin4 
```Email address: admin@admin.com or any email```
```Password: <any pasword> ```
```Retype password:```
```Starting pgAdmin 4. Please navigate to http://127.0.0.1:5050 in your browser.```
 * Serving Flask app 'pgadmin'
 * Debug mode: off

* Note: if above pgadmin4 does not work, try using a ```docker-compose.yaml``` file to start both ```pgadmin``` and ```postgres``` containers.

[quiz_script](lesson5_PostgreSQL\quiz.py)
[database_script](lesson5_PostgreSQL\database.py)
[model_script](lesson5_PostgreSQL\models.py)    # Sqlalchemy Operation Relational Mapping (ORM) to connect to PostgreSQL database and fetch data.


* update [main.py](main.py) --> ```uvicorn.run('lesson5.quiz:app', host='0.0.0.0', port=8000, reload=True)``` 

```bash
uv run main.py          # or python main.py
``` 
* open Pgadmin to see created tables

## Lesson 6: FastAPI app with MySQL Relational Database (watch Video for more tutorial)

## Lesson 7: React + FastAPI

