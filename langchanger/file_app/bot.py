import json

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from langchanger.settings import BOT_TOKEN


def get_chat(chat_title='test'):
    with open('static/bot_chats.json', 'r') as f:
        chats = json.load(f)

    if chat_title in chats:
        chat_id = chats[chat_title]
        return chat_id
    else:
        test_chat_id = chats['test']
        return test_chat_id


def do_start(update: Update):
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


def send_image(image, chat):
    chat_id = get_chat(chat)

    message = bot.send_photo(
        chat_id=chat_id,
        photo=image
    )

    image_hash = message.photo[-1].file_id
    return image_hash


def send_file(document, chat):
    chat_id = get_chat(chat)

    message = bot.send_document(
        chat_id=chat_id,
        document=document
    )

    file_hash = message.document.file_id
    return file_hash


def get_file(file_hash):
    file_object = bot.get_file(file_hash)

    return file_object.file_path


bot = Bot(
    token=BOT_TOKEN,
)
