from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# Import decorators
from custom_decorators.typing_decorator import send_typing_action


@send_typing_action
def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


# handlers to add to the dispatcher
start_handler = CommandHandler('start', start)
