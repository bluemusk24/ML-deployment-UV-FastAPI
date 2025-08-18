from fastapi import FastAPI
import uvicorn

app = FastAPI(title="ping")

@app.get("/ping")
def ping():
    return "PONG"

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=9696)  --> you can run this too


def main():
    uvicorn.run(app, host="0.0.0.0", port=9696)
if __name__ == "__main__":
    main()