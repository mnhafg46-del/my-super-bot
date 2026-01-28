import telebot
import os

# اطلاعات تو که از عکس‌ها برداشتم
BOT_TOKEN = "8425468959:AAE8dCNjvlVdO--KrbKi2jScutUJGKldn7s"
ADMIN_ID = 8425468959 

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "🚀 سیستم نفوذ و کنترل فعال شد!\n\nدستورات:\n📸 /photo (عکس)\n🎙 /voice (صدا)\n📱 /info (سیستم)")

@bot.message_handler(commands=['photo'])
def ask_photo(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "📸 در حال تلاش برای دسترسی به دوربین...")
        # در اینجا متد ارسال عکس قرار می‌گیرد

print("Bot is running...")
bot.infinity_polling()
