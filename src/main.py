import logging
from app import App
import sys
from dotenv import load_dotenv


def InitLogger():
    formatter = logging.Formatter(
        "%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s]: %(message)s")

    infoHandler = logging.StreamHandler(sys.stdout)
    infoHandler.setFormatter(formatter)
    infoHandler.setLevel("INFO")
    infoHandler.addFilter(lambda record: record.levelno <= logging.WARNING)

    errorHandler = logging.StreamHandler(sys.stderr)
    errorHandler.setFormatter(formatter)
    errorHandler.addFilter(lambda record: record.levelno >= logging.ERROR)

    logger = logging.getLogger()
    logger.setLevel("INFO")
    logger.addHandler(infoHandler)
    logger.addHandler(errorHandler)


if __name__ == "__main__":
    load_dotenv()
    InitLogger()
    try:
        app = App()
        app.run()
    except Exception as ex:
        logging.critical("Unhandled exception:", exc_info=ex)
        exit(1)
