import bot
from rss import updater

if __name__ == '__main__':
    all_updates = updater.get_local_file_storage_updates()
    for chanel_name, updates in all_updates:
        bot.send_updates(updates, chat_id=chanel_name)
        print("updated: " + chanel_name)

    bot.start_bot()
