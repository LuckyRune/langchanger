from django.core.management.base import BaseCommand

import json

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler
from telegram.utils.request import Request

from langchanger.settings import BOT_TOKEN


def do_start(update: Update, bot: Bot):
    message = update.message
    if message.chat.type == 'group':
        chat_title = message.chat.title
    else:
        chat_title = message.chat.type + message.from_user

    with open('static/bot_chats.json', 'r') as f:
        chats = json.load(f)

    with open('static/bot_chats.json', 'w') as f:
        chats[chat_title] = message.chat_id
        json.dump(chats, f)

    bot.send_message(
        chat_id=message.chat_id,
        text='Chat added',
    )


class Command(BaseCommand):
    help = 'tg bot'

    def handle(self, *args, **options):
        request = Request(connect_timeout=0.5, read_timeout=1.0)
        bot = Bot(request=request, token=BOT_TOKEN)

        updater = Updater(bot=bot, use_context=True)

        start_handler = CommandHandler('start', do_start)

        updater.dispatcher.add_handler(start_handler)

        updater.start_polling()
        updater.idle()

