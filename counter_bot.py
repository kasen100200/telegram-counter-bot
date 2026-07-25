import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.environ.get("8968912026:AAHaqg4BS4c1h5FXP35NYHWETjlLQJ6UIOA")

COUNT_FILE = "count.txt"


def load_count():
    try:
        with open(COUNT_FILE, "r") as f:
            return int(f.read())
    except:
        return 0


def save_count():
    with open(COUNT_FILE, "w") as f:
        f.write(str(count))


count = load_count()


keyboard = [
    ["📊 查看总数", "🧹 清零"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"当前总数：{count}",
        reply_markup=reply_markup
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global count

    text = update.message.text.strip()

    if text == "📊 查看总数":
        await update.message.reply_text(
            f"📊 当前总数：{count}",
            reply_markup=reply_markup
        )
        return


    if text == "🧹 清零":
        count = 0
        save_count()

        await update.message.reply_text(
            "✅ 已清零\n当前总数：0",
            reply_markup=reply_markup
        )
        return


    try:
        number = int(text)

        count += number

        save_count()

        await update.message.reply_text(
            f"✅ 已更新\n当前总数：{count}",
            reply_markup=reply_markup
        )

    except:
        pass



app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))


app.run_polling()
