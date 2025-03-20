import asyncio
from aiogram import Bot, Dispatcher
from secret import TOKEN
dp = Dispatcher()
bot = Bot(token=TOKEN)
asyncio.run(dp.start_polling(bot))