from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom 👋 Bot ishlayapti!")

app = ApplicationBuilder().token("8226108395:AAHltktOTXPztHTDy826ernq2JZrDZRt5Qo").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
