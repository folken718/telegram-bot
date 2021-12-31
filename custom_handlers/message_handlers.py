import time
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters


# Import decorators
from custom_decorators.typing_decorator import send_typing_action


@send_typing_action
def mike(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Miike!")
    time.sleep(.500)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Miiiiike!!")
    time.sleep(.500)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Miiiiiiike!!!")


@send_typing_action
def unknown(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
mike_handler = MessageHandler(Filters.text & (
    ~Filters.command) & (Filters.regex(r'miike') | Filters.regex(r'Miike')), mike)
