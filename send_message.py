import asyncio
from aiogram import Bot
from secret import TOKEN
bot = Bot(token=TOKEN)
from secret import space_events_id
asyncio.run(
    bot.send_message(
        space_events_id,
        "Я сплю!"))

# Unclosed client session
# client_session: <aiohttp.client.ClientSession object at 0x000002770FEE5FD0>        
# Unclosed connector
# connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x000002770FEEFE90>, 7885.5956881)])']
# connector: <aiohttp.connector.TCPConnector object at 0x000002770FEE5BE0>