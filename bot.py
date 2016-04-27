import telegram
import config

def send_updates(updates):
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
            bot.sendMessage(chat_id=config.telegram_channel_name, text= author + message)
