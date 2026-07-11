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

    for article in feed.entries:
        db_article = Articles(
            title=article.title,
            link=article.link,
            published=article.published,
            content=article.summary,
        )
        db.add(db_article)

    db.commit()

    return {"articles_saved": len(feed.entries)}
