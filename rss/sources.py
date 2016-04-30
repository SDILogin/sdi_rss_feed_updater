import local_file_storage_manager


def configure_rss_feeds_for_local_storage():
    channels = local_file_storage_manager.get_channels()
    return [(channel, local_file_storage_manager.read_feeds_from_file(channel)) for channel in channels]


rss_feeds = [
    {
        'title': 'Android Weekly',
        'url' : 'http://us2.campaign-archive1.com/feed?u=887caf4f48db76fd91e20a06d&id=4eb677ad19'
    },

    {
        'title': 'Android Developers Blog',
        'url' : 'https://feeds.feedburner.com/blogspot/hsDu'
    },

    {
        'title': 'Java67',
        'url' : 'https://feeds.feedburner.com/Java67'
    },

    {
        'title': 'Android Architecture (Fernando Cejas)',
        'url' : 'http://fernandocejas.com/feed/'
    },

    {
        'title': 'AppTractor',
        'url' : 'http://apptractor.ru/feed'
    },

    {
        'title': 'Dan Lew Codes',
        'url' : 'http://blog.danlew.net/rss/'
    },

    {
        'title': 'Feedpresso',
        'url' : 'http://blog.feedpresso.com/feed.xml'
    },

    {
        'title': 'AndroidDev (Habr)',
        'url' : 'https://habrahabr.ru/rss/hub/android_dev/'
    },
]

