from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client, Data
import os
a = os.getenv('a') #ADAFRUIT_IO_USERNAME
b = os.getenv('b') #ADAFRUIT_IO_KEY
c = 'os.getenv('c')
def turnoff(bot,update):
  chat_id=update.message.chat_id
  bot.send_photo(chat_id,photo='https://www.batteriesplus.com/content/images/product/large/443078.jpg')
  bot.send_message(chat_id,text="The BULB is OFF")
  aio = Client(a,b)
  value=Data(value=0)
  value_send=aio.create_data('botpubgbot',value)


def turnon(bot,update):
  chat_id=update.message.chat_id 
  bot.send_photo(chat_id,photo='https://www.christmaslightsetc.com/p/G40-E12-Clear-Globe-Replacement-Lamps--18769.htm#')
  bot.send_message(chat_id,text="the BULB is ON")
  aio = Client(a,b)
  value=Data(value=1)
  value_send=aio.create_data('botpubgbot',value)

def messagein(bot,update):
  mess_text=update.message.text
  if mess_text=='Turn on':
    turnon(bot,update)

  elif mess_text=='Turn off':
    turnoff(bot,update)  


u=Updater(c)
dp=u.dispatcher
dp.add_handler(CommandHandler('turnoff',turnoff))
dp.add_handler(CommandHandler('turnon',turnon))
dp.add_handler(MessageHandler(Filters.text&(~Filters.command),messagein))
u.start_polling()
u.idle()
