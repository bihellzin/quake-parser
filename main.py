from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from game import Game

import models
from models import Games
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
  try:
    db = SessionLocal()
    return db
  
  finally:
    db.close()

@app.get("/")
def home(request: Request):
  """
  return the index.html template
  """
  return templates.TemplateResponse('index.html', {"request":request})


@app.get("/{game_id}")
async def show_game_info(request: Request, game_id: int):
  """
  Access the database and return the result of the game passed through the URL
  """
  db = get_db()
  game_info = db.query(Games).filter(Games.id == game_id).first()
  return templates.TemplateResponse('game.html', {"request": request, "game_info": game_info})