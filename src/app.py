import logging
import commands
from telegram.ext import Application, CommandHandler
from os import getenv


class App:
    def __init__(self):
        token = getenv("TOKEN")
        self.tgApp = Application.builder().token(token).build()
        self.tgApp.add_handler(CommandHandler("start", commands.start))
        self.tgApp.add_handler(CommandHandler("help", commands.help))
        self.tgApp.add_handler(commands.findPhoneNumbersConversation)
        self.tgApp.add_handler(commands.findEmailConversation)
        self.tgApp.add_handler(commands.verifyPasswordConversation)
        self.tgApp.add_handler(CommandHandler("get_release", commands.GetRelease))

    def run(self):
        logging.info("Application starting.")

        self.tgApp.run_polling()

        logging.info("Application stoped.")
        self.tgApp.add_handler(CommandHandler("help", commands.help))
