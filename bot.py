from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chat import chat

with open('token.txt', 'r') as f:
    token = f.read()

def start(update, context):
    "Start"
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hello! I'm NUS Stats Soc Bot!")

def reply(update, context):
    """Reply"""
    message = update.message.text
    # This is where the magic happens
    answer = chat(message)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=answer)

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
print("Running...")
updater.idle()