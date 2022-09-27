from telegram import Update
import telegram
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application, CallbackQueryHandler, ConversationHandler
from EzPass import *
async def start(update, context):
     await update.message.reply_text("For usage use /help command")

async def help(update, context):
    await update.message.reply_text("""
    Usage :
        /getpass [pass length] - To get random generated password
    """)

async def getpass(update,context):
    #await update.message.reply_text(context.args[0])

    password = convleet(getword(int(context.args[0])))
    await update.message.reply_text(password)
async def hello(update: Update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def hello(update: Update, context) :
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
def main():
    app = ApplicationBuilder().token([API-KEY]).build()
    app.add_handler(CommandHandler('help',help))
    app.add_handler(CommandHandler('hello',hello))
    app.add_handler(CommandHandler('getpass',getpass))



    app.run_polling()


main()
