from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F

import asyncio
from secret import TOKEN

dp = Dispatcher()
bot = Bot(token=TOKEN)

@dp.message(F.voice)
async def voice_message_handler(message: Message):
    path = "C:\\Users\\alisa\\Downloads\\"

    await bot.download(
        message.voice,
        destination=path + "%s.ogg" % message.voice.file_id
    )

asyncio.run(dp.start_polling(bot))