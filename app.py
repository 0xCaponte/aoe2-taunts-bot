import asyncio
import logging
import os
import secrets
import string

import telebot
from aiohttp import web

from telebot import types
from telebot.async_telebot import AsyncTeleBot

from taunts import get_validated_taunt_tuple, search_for_taunt_tuple


WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
WEBHOOK_PORT = os.environ.get('WEBHOOK_PORT')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
SECRET_TOKEN = ''.join(secrets.choice(string.ascii_letters) for i in range(15))

# Telegram Bot
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = AsyncTeleBot(BOT_TOKEN)

@bot.inline_handler(lambda query: True)
async def inline_taunts(inline_query):
    """
       given a taunt number, searches for the corresponding taunt text and audio url
       """

    query: str = inline_query.query

    if not query:
        return

    if query.isdigit():
        taunt_tuple = get_validated_taunt_tuple(query)
    else:
        taunt_tuple = search_for_taunt_tuple(query)

    if taunt_tuple:
        result = types.InlineQueryResultAudio('1', audio_url=taunt_tuple[3], title=taunt_tuple[1])
        await bot.answer_inline_query(inline_query.id, [result])


@bot.message_handler(regexp='^\s*\/?\s*\d+\s*$') # Single number with optional white spaces
async def taunt(message):
    """
       checks all one word messages or commands send to the bot or group. If it is a valid
       AoE2 taunt number (1..105) the bot will reply with the audio file for that
       taunt.
       """

    text = message.text
    text= text.strip()

    if text[0] == '/':
        text = text[1:]

    taunt_tuple = get_validated_taunt_tuple(text)

    if taunt_tuple:
        await bot.send_audio(chat_id= message.chat.id, title=taunt_tuple[1],
                                     audio=open(taunt_tuple[2], "rb"))


async def webhook_handler(request):
    """ Gets and processes the updates from telegram via Webhooks
        """

    if request:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        asyncio.ensure_future(bot.process_new_updates([update]))
        return web.Response()
    else:
        return web.Response(status=403)


# Remove webhook and closing session before exiting
async def cleanup(app):
    """ Closes the connections created by the bot initialization
        """
    logger.info('Removing webhook')
    await bot.remove_webhook()

    logger.info('Closing bot session')
    await bot.close_session()

async def setup():
    """ Configures the webapp and starts the bot's webhook with telegram.
        """

    # Webhook Set-Up
    logger.info('Removing old webhook')
    await bot.remove_webhook()

    logger.info('Setting new webhook')
    await bot.set_webhook(url=WEBHOOK_URL,secret_token=SECRET_TOKEN)

    # WebApp Set-Up
    app = web.Application()
    app.router.add_post('', webhook_handler)
    app.on_cleanup.append(cleanup) # Clean Up
    return app

if __name__ == '__main__':

    web.run_app(
        setup(),
        host='127.0.0.1',
        port=WEBHOOK_PORT
    )

