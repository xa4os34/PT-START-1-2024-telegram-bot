from telegram import Update
from telegram.ext import ContextTypes
from commands.strings import HELP

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP)
