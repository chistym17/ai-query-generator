from fastapi import FastAPI, HTTPException, Depends,APIRouter
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()
router = APIRouter()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SQLQuery(BaseModel):
    sql: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/validate-sql/")
async def validate_sql(query: SQLQuery, db: Session = Depends(get_db)):
    try:
        result = db.execute(text(query.sql))

        columns = result.keys()

        rows = result.fetchall()

        result_dict = [dict(zip(columns, row)) for row in rows]  

        return {"data": result_dict}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
