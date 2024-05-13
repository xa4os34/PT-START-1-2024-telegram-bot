from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
import utils

GET_TEXT = 0


async def findPhoneNumbersStart(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Send text to find phone numbers")

    return GET_TEXT


async def findPhoneNumbers(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE):

    phoneNumbersList = utils.findAllPhoneNumbers(update.message.text)

    if len(phoneNumbersList) <= 0:
        await update.message.reply_text("No phone numbers in this text.")
        return ConversationHandler.END

    phoneNumbers = ""
    for phoneNumber in phoneNumbersList:
        phoneNumbers += phoneNumber + "\n"

    await update.message.reply_text("Phone numbers: \n" + phoneNumbers)

    return ConversationHandler.END


findPhoneNumbersConversation = ConversationHandler(
    entry_points=[CommandHandler("find_phone_number", findPhoneNumbersStart)],
    states={
        GET_TEXT: [MessageHandler(filters.TEXT, findPhoneNumbers)]
    },
    fallbacks=[])
