import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Crypto Bot запущений!\n\n"
        "Доступні команди:\n"
        "/start — головне меню\n"
        "/price — ціна криптовалюти\n"
        "/analyze — технічний аналіз\n"
        "/portfolio — мій портфель\n"
        "/alert — встановити алерт"
    )


async def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN не встановлений")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Crypto Bot запущений...")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
