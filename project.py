import feedparser
import random as random

# URL of the RSS feed
rss_url = "https://www.ratopati.com/feed"

# Parse the feed
feed = feedparser.parse(rss_url)

print(f"feed title:{feed.feed.title}")

# Iterate over entries and print titles and links
for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}")
    print(f"Summary: {entry.summary}")
    print("-" * 80)



# url ="http://rss.cnn.com/rss/edition.rss"

feed =feedparser.parse(rss_url)

for entry in feed.entries:
    date = entry.get("published")
    # title = (f"Title:{entry.title}")
    # summary = (f"Summary:{entry.summary}")
    title = entry.get("title")
    summary = entry.get("summary")
    guid = entry.get('id')

    # data = [{
    #     "DATE":date ,
    #     "Title":title,
    #     "summary":summary  
    #     }]
    
    print(guid)
    
