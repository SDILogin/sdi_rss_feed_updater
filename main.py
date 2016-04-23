import bot
from rss import updater

if __name__ == '__main__':
    bot.send_updates(updates = updater.get_new_entries())
