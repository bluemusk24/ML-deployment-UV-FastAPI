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
om fastapi import FastAPI

app = FastAPI()

text_posts = {}

@app.get("/posts")
def get_all_posts():
    return text_posts

# open the FASTAPI URL
http://localhost:8000/docs
```

