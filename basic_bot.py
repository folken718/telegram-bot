import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Import available handlers
from custom_handlers.command_handlers import start_handler, unknown_handler

# Setting up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading .env variables
load_dotenv()

# Getting .env variables
TOKEN = os.getenv('BOT_TOKEN')


def main() -> None:
    """
    Main function to run the bot
    """

    # Setting basic handlers
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(start_handler)

    # Unknown handler -- needs to be last
    dispatcher.add_handler(unknown_handler)

    # Starting the bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
