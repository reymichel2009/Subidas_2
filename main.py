from telethon import TelegramClient, events, sync,Button
from telethon.events import NewMessage

bot_token = '5477880325:AAG4D9yuEljDKFmUb12aF2y6i2k-_rCDS3Q'
chat_id = '5068280913'

bot = telegram.Bot(token_bot=bot_token)
print(bot.getme())

bot.send_message(chat_id=chat_id, text='Hola, se bienvenido a la prueba del Bot de Michel')
