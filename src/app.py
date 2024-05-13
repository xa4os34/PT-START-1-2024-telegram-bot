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
        self.tgApp.add_handler(CommandHandler("get_uname", commands.GetUname))
        self.tgApp.add_handler(CommandHandler("get_uptime", commands.GetUptime))
        self.tgApp.add_handler(CommandHandler("get_df", commands.GetDf))
        self.tgApp.add_handler(CommandHandler("get_free", commands.GetFree))
        self.tgApp.add_handler(CommandHandler("get_mpstat", commands.GetMpstat))
        self.tgApp.add_handler(CommandHandler("get_w", commands.GetW))
        self.tgApp.add_handler(CommandHandler("get_auths", commands.GetAuths))
        self.tgApp.add_handler(CommandHandler("get_critical", commands.GetCritical))
        self.tgApp.add_handler(CommandHandler("get_ps", commands.GetPs))
        self.tgApp.add_handler(CommandHandler("get_ss", commands.GetSs))
        self.tgApp.add_handler(CommandHandler("get_apt_list", commands.GetAptList))
        self.tgApp.add_handler(CommandHandler("get_services", commands.GetServices))

    def run(self):
        logging.info("Application starting.")

        self.tgApp.run_polling()

        logging.info("Application stoped.")
        self.tgApp.add_handler(CommandHandler("help", commands.help))
