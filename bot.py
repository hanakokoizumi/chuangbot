#!/usr/bin/python3
# -*- coding:utf-8 -*-

from telegram import InputTextMessageContent, InlineQueryResultArticle, InlineQueryResultPhoto, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext

import os
import logging
import random
from uuid import uuid4

from config import *

pic_dir = './pic'

files = os.listdir(pic_dir)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG,
    filename='chuangbot.log'
)

def reply(update: Update, context: CallbackContext):
    with open(os.path.join(pic_dir, random.choice(files)), 'rb') as f:
        update.message.reply_photo(f, random.choice(data))

def inline(update: Update, context: CallbackContext):
    answers = []
    query = update.inline_query.query.strip()
    if query == '':
        answers = [(random.choice(data), random.choice(pictures)) for _ in range(5)]
    else:
        for s in data:
            if query.upper() in s.upper():
                answers.append((s, random.choice(pictures)))
    reply = [
        InlineQueryResultPhoto(
            id=uuid4(),
            title=message,
            photo_url=pic,
            thumb_url=pic,
            caption=message,
        ) for message, pic in answers
    ]
    reply.append(InlineQueryResultArticle(
        id=uuid4(),
        title='性感泥头车，在线创群友',
        description='随机挑选泥头车',
        input_message_content=InputTextMessageContent('今天被' + random.choice(chips) + '创')
    ))
    update.inline_query.answer(reply, cache_time=0, switch_pm_text='共返回 %s 条结果，支持搜索' % len(answers), switch_pm_parameter='result_summary')

def main():
    updater = Updater(token, request_kwargs=kwargs)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", reply, run_async=True))
    dispatcher.add_handler(CommandHandler("help", reply, run_async=True))
    dispatcher.add_handler(CommandHandler("chuang", reply, run_async=True))
    dispatcher.add_handler(InlineQueryHandler(inline, run_async=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
