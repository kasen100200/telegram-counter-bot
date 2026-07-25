from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters


TOKEN = "8968912026:AAHaqg4BS4c1h5FXP35NYHWETjlLQJ6UIOA"


count = 0


keyboard = [
    ["📊 查看总数", "♻️ 清零"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ 计数机器人启动\n\n"
        "使用方法：\n"
        "+数字 = 增加\n"
        "-数字 = 减少\n\n"
        "例如：\n"
        "+100\n"
        "-50",
        reply_markup=reply_markup
    )


async def count_number(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global count

    text = update.message.text.strip()


    if text.startswith("+") and text[1:].isdigit():

        num = int(text[1:])
        count += num

        await update.message.reply_text(
            f"➕ 增加：{num}\n"
            f"📊 当前总数：{count}",
            reply_markup=reply_markup
        )


    elif text.startswith("-") and text[1:].isdigit():

        num = int(text[1:])
        count -= num

        await update.message.reply_text(
            f"➖ 减少：{num}\n"
            f"📊 当前总数：{count}",
            reply_markup=reply_markup
        )


async def show_count(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"📊 当前总数：{count}",
        reply_markup=reply_markup
    )


async def reset_count(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global count

    count = 0

    await update.message.reply_text(
        "♻️ 已清零\n📊 当前总数：0",
        reply_markup=reply_markup
    )


app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler("start", start)
)


app.add_handler(
    MessageHandler(
        filters.Regex("^📊 查看总数$"),
        show_count
    )
)


app.add_handler(
    MessageHandler(
        filters.Regex("^♻️ 清零$"),
        reset_count
    )
)


app.add_handler(
    MessageHandler(
        filters.TEXT,
        count_number
    )
)


print("机器人运行中...")


app.run_polling()
