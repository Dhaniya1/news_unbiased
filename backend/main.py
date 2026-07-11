from urllib.parse import quote

import feedparser
from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
def search(query: str):

    rss_url = f"https://news.google.com/rss/search?q={quote(query)}"

    feed = feedparser.parse(rss_url)

    articles = []

    for article in feed.entries:
        articles.append(
            {
                "title": article.title,
                "url": article.link,
                "published": article.published,
            }
        )

    return articles
