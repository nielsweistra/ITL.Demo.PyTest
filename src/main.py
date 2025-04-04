# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def read_root():
    return {"message": "OK"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
