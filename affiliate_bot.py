import requests
import telebot
import time

BOT_TOKEN = "8052570613:AAHfx4n3btoXbDaaUhseXUFUW37nbYWgh-4"
CHANNEL_ID = "-1002112548033"

AMAZON_TAG = "harshanvasu24-21"
EARNKARO_ID = "3263020"

bot = telebot.TeleBot(BOT_TOKEN)

def get_amazon_products():
    return [
        {
            "title": "Best Amazon Deal Example",
            "price": "₹999",
            "image": "https://m.media-amazon.com/images/I/51l5XzLq4cL.jpg",
            "link": f"https://www.amazon.in/dp/B0XXXXXX?tag={AMAZON_TAG}"
        }
    ]

def get_earnkaro_products():
    return [
        {
            "title": "Flipkart/Myntra Deal Example",
            "price": "₹499",
            "image": "https://rukminim2.flixcart.com/image/832/832/kcxpbww0/shirt/h/g/j/m-men-regular-fit-shirt-example.jpeg",
            "link": f"https://earnkaro.com/deal/{EARNKARO_ID}"
        }
    ]

def post_products():
    products = get_amazon_products() + get_earnkaro_products()
    for p in products:
        text = f"🔥 {p['title']}\n💰 Price: {p['price']}\n👉 Buy Here: {p['link']}"
       import requests

for p in products:
    text = f"🔥 {p['title']}\n💰 Price: {p['price']}\n👉 Buy Here: {p['link']}"
    try:
        response = requests.get(p['image'])
        if response.status_code == 200:
            bot.send_photo(CHANNEL_ID, response.content, caption=text)
        else:
            bot.send_message(CHANNEL_ID, text + "\n⚠️ Image not available")
    except:
        bot.send_message(CHANNEL_ID, text + "\n⚠️ Error loading image")
    time.sleep(5)

        time.sleep(5)

while True:
    post_products()
    time.sleep(3600 * 6)
