import random
from telegram.ext import Application, CommandHandler, ContextTypes

WORDS = [
    "ктулху", "мандаринка", "шаверма", "пенис", "крабик", 
    "биба", "боба", "пончик", "залупа", "пельмень",
    "тапок", "чукча", "вафля", "помидор", "верблюд",
    "таракан", "бульдог", "попкорн", "красотка", "динозавр", "бурмалда", "попа", "https://t.me/FazergamesFazer", "газан", "ъ", "да", "пр", "ок", "откажусь", "@danek_pr", "бульба"
]

async def random_word(update, context):
    word = random.choice(WORDS)
    await update.message.reply_text(word)

async def start(update, context):
    await update.message.reply_text("пиши /word канал автора : https://t.me/FazergamesFazer")

def main():
    app = Application.builder().token("8848325697:AAHDELTivhfzneFSqVu5ymtXtXZ_vzm_R78").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", random_word))
    app.run_polling()

if __name__ == "__main__":
    main()