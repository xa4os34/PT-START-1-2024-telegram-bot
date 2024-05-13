from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
import utils

GET_TEXT = 0


async def findEmailStart(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Send text to find emails")

    return GET_TEXT


async def findEmail(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):

    emailList = utils.findEmails(update.message.text)

    if len(emailList) <= 0:
        await update.message.reply_text("No emails in this text.")
        return ConversationHandler.END

    emails = ""
    for email in emailList:
        emails += email + "\n"

    await update.message.reply_text("Emails: \n" + emails)

    return ConversationHandler.END


findEmailConversation = ConversationHandler(
    entry_points=[CommandHandler("find_email", findEmailStart)],
    states={
        GET_TEXT: [MessageHandler(filters.TEXT, findEmail)]
    },
    fallbacks=[])
