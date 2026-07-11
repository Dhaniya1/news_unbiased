from datetime import datetime

from pydantic import BaseModel


class Article_info(BaseModel):
    title: str
    link: str
    published: datetime
    content: str
