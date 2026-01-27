import telebot

# توکن بات شما
TOKEN = "8266741632:AAE8odmzY5ZZj_TQdXgsI_OSDVkKyvJX3Ik"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 قربان، سیستم با موفقیت از طریق سرورهای گیت‌هاب فعال شد!")

if __name__ == "__main__":
    bot.polling()
