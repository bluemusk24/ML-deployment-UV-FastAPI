import uvicorn


if __name__ == "__main__":
    #uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)
    #uvicorn.run('lesson1.intro:app', host='0.0.0.0', port=8000, reload=True)       
    #uvicorn.run('lesson2.books:app', host='0.0.0.0', port=8000, reload=True)       
    #uvicorn.run('lesson3_sqlite.books:app', host='0.0.0.0', port=8000, reload=True)       
    uvicorn.run('lesson5_PostgreSQL.quiz:app', host='0.0.0.0', port=8000, reload=True)       

