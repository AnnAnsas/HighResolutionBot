from aiogram import executor
from bot.main_bot import dp

executor.start_polling(dp, skip_updates=True)