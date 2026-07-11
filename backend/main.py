from urllib.parse import quote

import feedparser
from dependencies import get_db
from fastapi import Depends, FastAPI
from models import Articles
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/search")
def search(query: str, db: Session = Depends(get_db)):

    rss_url = f"https://news.google.com/rss/search?q={quote(query)}"

    feed = feedparser.parse(rss_url)

    articles = []

    for articles in feed.entries:
        db_article = Articles(
            title=articles.title,
            link=articles.link,
            published=articles.published,
            content=articles.summary,
        )
        db.add(db_article)
        db.commit()

    return articles
