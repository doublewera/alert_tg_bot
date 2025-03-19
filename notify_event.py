import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from datetime import datetime

from secret import TOKEN, space_events_id

dp = Dispatcher()
bot = Bot(token=TOKEN)

async def check_db() -> None:
    while True:
        await asyncio.sleep(10)
        await bot.send_message(
            space_events_id,
            "Я проснулся! %s" % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Я веду канал космических событий! https://t.me/n_esse")

# Run the bot
async def main() -> None:
    tasks = []
    async with asyncio.TaskGroup() as tg:
        tasks.append(
            tg.create_task(check_db()))
        tasks.append(
            tg.create_task(dp.start_polling(bot)))


if __name__ == "__main__":
    asyncio.run(main())
          