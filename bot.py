import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ خطأ: لم يتم العثور على BOT_TOKEN في متغيرات البيئة.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! البوت يعمل 🚀")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ البوت جاهز ويعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()
