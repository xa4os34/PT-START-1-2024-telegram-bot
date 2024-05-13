from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters
)
import utils

GET_TEXT = 0


async def verifyPasswordStart(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Send password for verification")

    return GET_TEXT


async def verifyPassword(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):

    message = "Your password is not strong enough."

    if utils.checkPasswordStrength(update.message.text):
        message = "Your password is strong"

    await update.message.reply_text(message)

    return ConversationHandler.END


verifyPasswordConversation = ConversationHandler(
    entry_points=[CommandHandler("verify_password", verifyPasswordStart)],
    states={
        GET_TEXT: [MessageHandler(filters.TEXT, verifyPassword)]
    },
    fallbacks=[])
