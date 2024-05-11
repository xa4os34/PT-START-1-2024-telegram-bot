from telegram import Chat, ChatMember, Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from telegram.helpers import escape_markdown
from commands.strings import PM_START_TEXT


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        first_name = update.effective_user.first_name

        reply = PM_START_TEXT.format(
            escape_markdown(first_name),
            escape_markdown(context.bot.first_name))

        await update.effective_message.reply_text(reply)
