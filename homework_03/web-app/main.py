from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def Pong():
    return {"message": "pong"}