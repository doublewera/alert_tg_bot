import asyncio
from aiogram import Bot, Dispatcher
from secret import TOKEN
dp = Dispatcher()
bot = Bot(token=TOKEN)
@dp.channel_post()
async def channel_post_handler(channel_post):
    await channel_post.answer('Я понял: ' + channel_post.text)
asyncio.run(dp.start_polling(bot))