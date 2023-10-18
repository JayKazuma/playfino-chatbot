import telebot
from telebot import types
  # Ensure you have this import statement

# Replace 'YOUR_BOT_TOKEN' with the actual token you obtained from BotFather
TOKEN = '6313560946:AAFF6uYJ3jeiFpeTA2n1Mmd4ZltkXdRvkUI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user

    welcome_message = (
        "Welcome to PLAYFINO community. The best slot games in the Philippines that offer you a source of income with no capital.\n\n"
        "Playfino offers you 30-40% COMMISSION + BONUSES.\n\n"
        "JOIN US IN OUR CIRCLE AND TEST YOUR LUCK WITH THE BEST ONLINE CASINO."
    )
    
    with open('PlayfinoVid2.mp4', 'rb') as video:
        bot.send_video(message.chat.id, video, caption=welcome_message, parse_mode='Markdown')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    facebook_button = types.KeyboardButton("Playfino Official Facebook")
    agent_button = types.KeyboardButton("Apply as Agent")
    player_link_button = types.KeyboardButton("Player Link")
    master_agent_button = types.KeyboardButton("Apply as Master Agent")
    send_to_admin_button = types.KeyboardButton("Send to Admin")
    markup.row(facebook_button, agent_button)
    markup.row(player_link_button, master_agent_button)
    markup.row(send_to_admin_button)

    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_response = message.text.lower()

    if user_response == 'playfino official facebook':
        bot.reply_to(message, "Visit our Facebook page at: [Playfino Official Facebook](https://www.facebook.com/profile.php?id=61552378563393&mibextid=ZbWKwL)")

    elif user_response == 'apply as agent':
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton("Apply as Agent", url="https://playfinooc.vip/ar/Playfinoofficial01")
        markup.add(url_button)

        bot.send_message(message.chat.id, "Click the button below to apply as an agent:", reply_markup=markup)

    elif user_response == 'player link':
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton("Player Link", url="https://playfinooc.vip/r/Playfinoofficial/reg")
        markup.add(url_button)

        bot.send_message(message.chat.id, "Click the button below for Player Link:", reply_markup=markup)

    elif user_response == 'apply as master agent':
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton("Apply as Master Agent", url="https://playfinooc.vip/ar/zfa_Nataraki22")
        markup.add(url_button)

        bot.send_message(message.chat.id, "Click the button below to apply as a Master Agent:", reply_markup=markup)
        bot.send_message(message.chat.id, "After clicking the button, please send your username to the admin for account activation.")

    elif user_response == 'send to admin':
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton("Send Email to Admin", url="https://t.me/Playfinoofficial0")
        markup.add(url_button)

        bot.send_message(message.chat.id, "Click the button below to send a message to the admin:", reply_markup=markup)

    else:
        bot.reply_to(message, "I'm sorry, I didn't understand. Please choose an option from the buttons.")

if __name__ == '__main__':
    bot.polling()
