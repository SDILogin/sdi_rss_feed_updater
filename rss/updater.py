import time
import feedparser
import rss.sources as sources

# in seconds
MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
WEEK = DAY * 7

# show only fresh entries
is_entry_ok = lambda creation_time : abs(time.mktime(time.localtime()) - time.mktime(creation_time)) <= DAY

def get_new_entries():
    new_entries = []
    for source in sources.rss_feeds:
       new_entries += [{source['title'] : get_entries_since_yesterday(source['url'])}]
    return new_entries

def get_entries_since_yesterday(url):
    rss = feedparser.parse(url)
    if rss['status'] >= 200 and rss['status'] < 300 and len(rss['entries']) > 0:
        return [entry for entry in rss['entries'] if is_entry_ok(entry['published_parsed'])]
