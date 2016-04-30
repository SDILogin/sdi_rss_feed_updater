import telegram
from telegram.ext import Updater
import config
import local_file_storage_manager

def send_updates(updates, chat_id = config.telegram_channel_name):
    # init bot
    bot = telegram.Bot(token=config.telegram_bot_token)

    # update channel
    for update in updates:
        author, entries = list(update.items())[0]
        if not entries:
            continue

        # configure message
        message = ""
        for ind, entry in enumerate(entries):
            message += '\n\n%d) %s' % (ind + 1, entry['title'])
            message += '\n' + entry['link']

        # post message
        if message != "":
            bot.sendMessage(chat_id=chat_id, text= author + message)


def start_handler(bot, update):
    print(update)


def add_handler(bot, update):
    command = update.message.text[len('/add'):].strip().split(' ')
    local_file_storage_manager.add_rss_feed_to_channel(command[0], ' '.join(command[1:-1]), command[-1])
    bot.sendMessage(chat_id=update.message.chat_id, text="\n".join(local_file_storage_manager.get_enumerated_list_feed(command[0])))


def list_handler(bot, update):
    command = update.message.text[len('/list'):].strip().split(' ')
    bot.sendMessage(chat_id=update.message.chat_id, text="\n".join(local_file_storage_manager.get_enumerated_list_feed(command[0])))


def remove_handler(bot, update):
    command = update.message.text[len('/remove'):].strip().split(' ')
    local_file_storage_manager.remove_rss_feed_from_channel(command[0], int(command[1]))
    bot.sendMessage(chat_id=update.message.chat_id, text="\n".join(local_file_storage_manager.get_enumerated_list_feed(command[0])))


def start_bot():
    updater = Updater(token=config.telegram_bot_token)
    dispatcher = updater.dispatcher
    dispatcher.addTelegramCommandHandler("start", start_handler)
    dispatcher.addTelegramCommandHandler("add", add_handler)
    dispatcher.addTelegramCommandHandler("list", list_handler)
    dispatcher.addTelegramCommandHandler("remove", remove_handler)
    updater.start_polling()

