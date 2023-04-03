from aiogram import Bot, Dispatcher
import os
import dotenv
dotenv.load_dotenv()

# token

TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
