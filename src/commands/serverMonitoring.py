from ssh import SshClient, SshError, SshResult
from telegram import Update
from telegram.ext import ContextTypes
from commands.strings import UNEXPECTED_ERROR

def _getMessageFromResult(result: SshResult):
    return UNEXPECTED_ERROR if result.hasError else result.data

async def GetRelease(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("uname -r")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetUname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("uname")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetUptime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("uptime")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetDf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("df")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetFree(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("free")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetMpstat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("mpstat")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetW(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("w")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetPs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("ps")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetSs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand("ss -A inet")
    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetAuths(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand(
            "cat /var/log/auth.log | \
             grep -iE '(Accepted|Invalid User)' | \
             tail | cut -b1-19,56-")

    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetCritical(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand(
            "journalctl -p crit -n 10 --no-pager")

    message = _getMessageFromResult(result)
    await update.message.reply_text(message)


async def GetAptList(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = "apt list --installed | cut -d/ -f1"

    if len(context.args) > 0:
        command = "apt show"

    result = SshClient().ExecuteCommand(
            command, context.args)

    message = _getMessageFromResult(result)
    messages = [message[i:i + 4096] for i in range(0, len(message), 4096)]
    for msg in messages:
        await update.message.reply_text(msg)


async def GetServices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = SshClient().ExecuteCommand(
            "service --status-all")

    message = _getMessageFromResult(result)
    await update.message.reply_text(message)
