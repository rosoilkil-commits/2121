from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio 
from aiogram.filters import Command, CommandStart
bot = Bot(token='8701982171:AAHNr1yuhGqdVScICAug7xxt6Ozv2R7UdVM')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот!')

@dp.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer('Ви написали /help')

@dp.message(Command('settings'))
async def cmd_start(message: Message):
    await message.answer('Меню настройок')


@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)

async def main():
    await dp.start_polling(bot)

if __name__ ==  '__main__':
    try:

        asyncio.run(main())
    except KeyboardInterrupt:
        pass
