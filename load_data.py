
import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

def load_csv_to_db(csv_path):
    db: Session = SessionLocal()
    data = pd.read_csv(csv_path)
    for _, row in data.iterrows():
        user = models.User(username=row['username'])
        db.add(user)
    db.commit()
    db.close()

# load_csv_to_db('yourfile.csv')
