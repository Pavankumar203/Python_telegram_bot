from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Data
import os
x = os.getenv('x') #ADAFRUIT_IO_USERNAME
y = os.getenv('y') #ADAFRUIT_IO_KEY
z = os.getenv('z') #bot's API token


def turnoff(bot,update):
  chat_id=update.message.chat_id
  bot.send_photo(chat_id,photo='https://www.batteriesplus.com/content/images/product/large/443078.jpg')
  bot.send_message(chat_id,text="The BULB is OFF")
  aio = Client(x,y)
  value=Data(value=0)
  value_send=aio.create_data('botpubgbot',value)


def turnon(bot,update):
  chat_id=update.message.chat_id 
  bot.send_photo(chat_id,photo='https://www.christmaslightsetc.com/p/G40-E12-Clear-Globe-Replacement-Lamps--18769.htm#')
  bot.send_message(chat_id,text="the BULB is ON")
  aio = Client(x,y)
  value=Data(value=1)
  value_send=aio.create_data('botpubgbot',value)


u=Updater(z)
dp=u.dispatcher
dp.add_handler(CommandHandler('turnoff',turnoff))
dp.add_handler(CommandHandler('turnon',turnon))
u.start_polling()
u.idle()
   
