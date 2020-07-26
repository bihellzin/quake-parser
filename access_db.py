from database import SessionLocal

def get_db():
  """
  Starts a connection to the database
  """
  try:
    db = SessionLocal()
    return db
  
  finally:
    db.close()