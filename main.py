from sqlalchemy import create_engine, select, insert
from fastapi import FastAPI


app = FastAPI()
engine = create_engine("postgresql+psycopg2://postgres:Minolta@localhost:5432/marketplace")

@app.get("db_select")
def get_db():
    with engine.connect() as conn:
        stmt = select()
        res = conn.execute(stmt)

@app.get("db_insert")
def get_db():
    ...
    # with engine.connect() as conn:
    #     stmt = insert()
    #     res = conn.execute(stmt)
