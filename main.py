import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import BoundFilter
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


@dp.message_handler(commands=['rights'])
async def myrights(message: types.Message):
    member = await bot.get_chat_member(message.chat.id, API_TOKEN.split(":")[0])




#async def my_filter(message: types.Message):
#    return {'растер' : 'пидар'}
#
#
#
#@dp.message_handler(my_filter)
#async def my_message_handler(message: types.Message):
#    await message.reply()
#




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)