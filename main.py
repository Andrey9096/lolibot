import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1819449909:AAGXFeRV4KulEdSO4fEMZQxq2M6EoAta-qg'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_msg(message: types.Message):
    await message.reply("Hello")

@dp.message_handler(content_types=["new_chat_members"])
async def new_member(message):
    user_name = message.new_chat_members[0].first_name
    await  bot.send_message(message.chat.id, "Добро пожаловать, {0}! Правило одно - не мамкоебить!".format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)