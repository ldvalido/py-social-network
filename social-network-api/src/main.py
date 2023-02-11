from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def root():
    return {"message": "pong"}

@app.post("/publication")
async def root():
    return {"message": "new publication"}

@app.post("/follower")
async def root():
    return {"message": "new follower"}
