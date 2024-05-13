from ssh import SshClient, SshError
from telegram import Update
from telegram.ext import ContextTypes


async def GetRelease(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("uname -r")
    await update.message.reply_text(result.data)
