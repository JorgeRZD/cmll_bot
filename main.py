from typing import Final
from telegram import Update
from datetime import datetime
from dotenv import load_dotenv
import os
from card_retriever import card_retrieve
from telegram.ext import (
    filters,
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
)

load_dotenv()

TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = "@lucha_cmll_bot"


# Comandos del bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola. Gracias por usar el lucha_cmll_bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Algún día este comando tendrá información de como usar el bot. Sin embargo hoy no es el día"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.rep


# Respuestas
def handle_response(text: str) -> str:
    processed_text: str = text.lower()

    if "hola" in processed_text:
        return "Hola borola"

    if "luchador favorito" in processed_text:
        return "Puro Hechicero ALV"

    if "buenos días" in processed_text and datetime.now().hour == 11:
        return "Ya casi tardes"
    elif "buenos días" in processed_text and datetime.now().hour != 11:
        return "Buenas las tenga, caballero"

    if "cartelera" in processed_text:
        return card_retrieve()

    return "No entiendo lo que me quieres decir"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print(f"{BOT_USERNAME} answered: " + response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("+++++ STARTING THE BOT +++++")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("+++++ POLLING... +++++")
    app.run_polling(poll_interval=3)
