import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from read import start_db,fetch_movies,save_movies


TOKEN = '7174049083:AAFN783IuT063TWinJ2o-ZCb36M7JKwt2cA'


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)} siz yangi kino qidiring!")

# @dp.message(F.text.lower() == "salom")
# async def Info(message:Message):
#     text = message.text
#     await message.reply(f"{html.bold(message.from_user.full_name)} >>> Xabar yozing men ma'lumot beraman!")

@dp.message(F.text)
async def wikipediaBot(message:Message):
    text = message.text

    
        
    
@dp.message()
async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
   
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    