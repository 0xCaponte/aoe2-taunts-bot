import os

from telegram import Update, InlineQueryResultAudio
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, InlineQueryHandler

from taunts import get_validated_taunt_tuple


async def taunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
       checks all messages  and commands send to the bot or group and if it is a valid
       AoE2 taunt number (1..105) the bot will reply with the audio file for that
       taunt.
       """
    message = update.message.text

    if message[0] == '/':
        message = update.message.text[1:]

    taunt_tuple = get_validated_taunt_tuple(message)

    if taunt_tuple:
        await context.bot.send_audio(chat_id=update.message.chat_id, title=taunt_tuple[1],
                                     audio=open(taunt_tuple[2], "rb"))


async def inline_taunts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
       given a taunt number, searches for the corresponding taunt text and audio url
       """

    query = update.inline_query.query

    if not query:
        return

    taunt_tuple = get_validated_taunt_tuple(query)

    if taunt_tuple:
        results = [
            InlineQueryResultAudio(id, title=taunt_tuple[1], audio_url=taunt_tuple[3])
        ]

        await context.bot.answer_inline_query(update.inline_query.id, results)


if __name__ == "__main__":
    token = os.environ.get('BOT_TOKEN')

    application = (
        ApplicationBuilder()
            .token(token)
            .build()
    )

    text_handler = MessageHandler(filters.TEXT | filters.COMMAND, taunt)  # for messages and commands
    inline_taunts_handler = InlineQueryHandler(inline_taunts)

    application.add_handler(inline_taunts_handler)
    application.add_handler(text_handler)

    application.run_polling()
