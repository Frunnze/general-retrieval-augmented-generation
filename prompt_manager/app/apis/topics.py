from fastapi import APIRouter
import json
import os

topics_router = APIRouter()

@topics_router.post("/add_topic")
async def add_topic(topic: str):
    try:
        topics = []
        if os.path.exists("topics.json"):
            with open("topics.json", "r") as file:
                topics = json.loads(file.read())
                if topic in topics:
                    return {"msg": "Topic already exists!"}, 409

        with open("topics.json", "w") as file:
            topics.append(topic)
            file.write(json.dumps(topics))
            return {"msg": "Topic added!"}
    except Exception as e:
        print(e)
        return {"msg": "Server Error"}, 500