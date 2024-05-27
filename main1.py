from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('Отправить фота кота')
button_2 = KeyboardButton('Перейти на следующую клавиатуру')
keyboard.add(button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
button_3 = KeyboardButton('Отправить фота собаки')
button_4 = KeyboardButton('Вернутьтя на 1 клавиатуру')
keyboard.add(button_3, button_4)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Отправить фота кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://vsegda-pomnim.com/uploads/posts/2022-04/1649126536_4-vsegda-pomnim-com-p-koti-na-prirode-foto-7.jpg', caption='Вот тебе кот!!!')

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://vsegda-pomnim.com/uploads/posts/2022-04/1649126536_4-vsegda-pomnim-com-p-koti-na-prirode-foto-7.jpg', caption='Вот тебе кот!!!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)