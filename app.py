import os

from telegram import Update, InlineQueryResultAudio, InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler

from taunts import get_validated_taunt_tuple


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
       echo checks all messages send to the bot/group and if the message is a valid
       AoE2 taunt number (ex: 1..105). The bot will reply with the audio file for that
       taunt.
       """

    message = update.message.text
    taunt_tuple = get_validated_taunt_tuple(message)

    if taunt_tuple:
        await context.bot.send_audio(chat_id=update.message.chat_id, title=taunt_tuple[1],
                                     audio=open(taunt_tuple[2], "rb"))


async def inline_taunts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
       inline_taunts given a taunt number, functions as a search for the corresponding taunt text.
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

    # Handlers
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    inline_taunts_handler = InlineQueryHandler(inline_taunts)

    application.add_handler(inline_taunts_handler)
    application.add_handler(echo_handler)

    application.run_polling()
