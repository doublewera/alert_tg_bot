from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F

import asyncio
from asgiref.sync import sync_to_async
from secret import TOKEN

from ffmpeg.asyncio import FFmpeg

async def convert(file1, file2):  # for example: ogg to mp3
    ffmpeg = (
        FFmpeg()
        .input(file1)
        .output(file2)
    )

    await ffmpeg.execute()

import speech_recognition
@sync_to_async
def speech_to_text(filename):
    result = ' но не понял'
    r = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(filename) as source:
        audio = r.record(source)
    try:
        result = r.recognize_google(audio)
    except Exception as e:
        print("Exception: " + str(e))
    return result


dp = Dispatcher()
bot = Bot(token=TOKEN)

@dp.message(F.voice)
async def voice_message_handler(message: Message):
    path_to_file = 'C:\\Users\\alisa\\Downloads\\%s' % message.voice.file_id

    await bot.download(
        message.voice,
        destination=path_to_file + '.ogg'
    )
    await convert(path_to_file + '.ogg', path_to_file + '.wav')

    message_as_text = await speech_to_text(path_to_file + '.wav')
    await message.answer('Я услышал ' + message_as_text)

asyncio.run(dp.start_polling(bot))
