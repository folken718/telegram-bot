from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters

# Import decorators
from custom_decorators.typing_decorator import send_typing_action


@send_typing_action
def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


@send_typing_action
def unknown(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# handlers to add to the dispatcher
start_handler = CommandHandler('start', start)
unknown_handler = MessageHandler(Filters.command, unknown)
