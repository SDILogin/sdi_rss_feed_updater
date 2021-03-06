import time
import feedparser
import rss.sources as sources
import data_storage

# show only fresh entries
is_new_entry = lambda creation_time : time.mktime(creation_time) >= data_storage.get_last_updated_time()

def get_new_entries(rss_feeds = sources.rss_feeds):
    new_entries = []
    for source in rss_feeds:
       new_entries += [{source['title'] : get_entries_since_last_update(source['url'])}]
    data_storage.save_last_updated_time()
    return new_entries

def get_entries_since_last_update(url):
    rss = feedparser.parse(url)
    if rss['status'] >= 200 and rss['status'] < 300 and len(rss['entries']) > 0:
        return [entry for entry in rss['entries'] if is_new_entry(entry['published_parsed'])]

def get_local_file_storage_updates():
    result = []
    chanel_feed_pairs = sources.configure_rss_feeds_for_local_storage()
    for channel, rss_feed in chanel_feed_pairs:
        result.append(("@"+channel, get_new_entries(rss_feed)))
    return result