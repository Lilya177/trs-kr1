from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel      
from models import User              


my_app = FastAPI()


feedbacks = []


class Feedback(BaseModel):
    name: str
    message: str


user = User(name="Кадаева Лилия", id=1)




@my_app.get("/", response_class=HTMLResponse)
def read_html():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()


@my_app.get("/users")
def get_user():
    return user


@my_app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)          
    return {"message": f"Feedback received. Thank you, {feedback.name}."}