from database import Base
from sqlalchemy import Column, Integer, String


class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link = Column(String)
    published = Column(String)
    content = Column(String)
