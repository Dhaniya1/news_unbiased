from typing import Annotated

from database import sessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
