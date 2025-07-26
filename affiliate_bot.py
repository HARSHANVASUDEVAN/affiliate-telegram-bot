import requests
import telebot
import time

BOT_TOKEN = "8052570613:AAHfx4n3btoXbDaaUhseXUFUW37nbYWgh-4"
CHANNEL_ID = "@CartGoofferdeals"

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
        bot.send_photo(CHANNEL_ID, p['image'], caption=text)
        time.sleep(5)

while True:
    post_products()
    time.sleep(3600 * 6)
