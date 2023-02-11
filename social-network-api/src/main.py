from src.services.follower_service import FollowerService
from src.services.post_service import PostService
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class PostMessage(BaseModel):
    content: str

class FollowMessage(BaseModel):
    follow: str
    follower: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def root():
    return {"message": "pong"}

@app.post("/publication")
async def publish(msg: PostMessage):
    post_service = PostService()
    post_service.publish_post(msg)
    return msg

@app.post("/follower")
async def follower(msg: FollowMessage):
    follower_service = FollowerService()
    follower_service.publish(msg)
    return msg
