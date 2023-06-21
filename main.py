import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5758456770:AAHr6S-MCN_Nqfg7ppvOePHoUuMmYmrFXoo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nI'm TESTBot!\nPowered by aiogram.")


@dp.message_handler(text="test")
async def echo(message: types.Message):
    await message.answer_poll(
        question="Mars IT schoolning nechta filiyali bor?",
        options=["1", '2', '3'],
        correct_option_id=2,
        type="quiz",
        is_anonymous=False,
        open_period=10
    ),
    await asyncio.sleep(10)
    await message.answer_poll(
        question="Mars IT schoolda BACK-351DA nechta o'quvchi bor?",
        options=["10", '6', '17'],
        correct_option_id=1,
        type="quiz",
        is_anonymous=False,
        open_period=10
    ),
    await asyncio.sleep(10)
    await message.answer_poll(
        question="Mars IT da nechta kurs bor?",
        options=["bekent", 'frontent', 'stater', 'Hammasi bor'],
        correct_option_id=3,
        type="quiz",
        is_anonymous=False,
        open_period=10
    ),
    await asyncio.sleep(10)
    await message.answer_poll(
        question="Mars IT da necta coinga keyboard olasiz?",
        options=["150", '350', '500'],
        correct_option_id=1,
        type="quiz",
        is_anonymous=False,
        open_period=10
    )



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Any text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)