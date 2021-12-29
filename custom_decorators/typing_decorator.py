from functools import wraps
import telegram
from telegram import ChatAction

# Typing animation to show to user to imitate human interaction


def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(*args, **kwargs):
            update, context = args
            context.bot.send_chat_action(
                chat_id=update.effective_message.chat_id, action=action)
            return func(update, context, **kwargs)
        return command_func
    return decorator


send_typing_action = send_action(ChatAction.TYPING)
