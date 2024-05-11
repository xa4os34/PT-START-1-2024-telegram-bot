import logging
import commands
from telegram.ext import Application, CommandHandler
from os import getenv



class App:
    def __init__(self):
        token = getenv("TOKEN")
        self.tgApp = Application.builder().token(token).build()
        self.tgApp.add_handler(CommandHandler("start", commands.start))

    def run(self):
        logging.info("Application starting.")

        self.tgApp.run_polling()

        logging.info("Application stoped.")
