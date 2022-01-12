from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from apis.banxico_api import get_exchange_rate_today

# Import decorators
from custom_decorators.typing_decorator import send_typing_action


@send_typing_action
def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


@send_typing_action
def exchange(update: Update, context: CallbackContext) -> None:
    exchange_rate = get_exchange_rate_today()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f'Today exchange rate is : {exchange_rate}')


# handlers to add to the dispatcher
start_handler = CommandHandler('start', start)
