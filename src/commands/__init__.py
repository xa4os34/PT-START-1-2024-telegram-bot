from telegram import Update
from telegram.ext import ContextTypes
from telegram.helpers import escape_markdown
from commands.strings import PM_START_TEXT

from commands.help import *
from commands.findPhoneNumber import findPhoneNumbersConversation
from commands.findEmail import findEmailConversation
from commands.verifyPassword import verifyPasswordConversation
from commands.serverMonitoring import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name

    reply = PM_START_TEXT.format(
        escape_markdown(first_name),
        escape_markdown(context.bot.first_name))

    await update.effective_message.reply_text(reply)
