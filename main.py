import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
 
API_TOKEN = '7806447433:AAGCKqa34JjmpV3mwuv9IZ4abMZ_lOr76fc'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class InputStates(StatesGroup):
    mainMenu = State()
    presents = State()
    keyses = State()
    contacts = State()
 
# URL логотипа
LOGO_URL = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd-BLVf0ssQt6PEu4v7FU9wX3ZfQ0cUWcLTQ&s'  # Замените на URL вашего логотипа

# @dp.message_handler(commands=['start'], state=InputStates.mainMenu)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message, state: FSMContext):
    kb = [
        [
            types.KeyboardButton(text="Презентации"),
            types.KeyboardButton(text="Кейсы"),
            types.KeyboardButton(text="Контакты")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
 
#    await message.reply("Привет!\n\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)
    await message.answer_photo(photo=LOGO_URL, caption="Привет!\n\n это страртовое сообщение. Выберите варивант из меню")

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Общая презентация (разработка музеев и выставок)', url='https://appollopro.ru/razrabotka-muzeev-i-vystavok/')
urlButton2 = InlineKeyboardButton(text='Для разработчиков (ПО для шлемов VR/AR/MR)', url='https://appollopro.ru/po-dlya-shlemov-vr-mr/')
urlButton3 = InlineKeyboardButton(text='Для агенств (Интерактивное оборудование)', url='https://appollopro.ru/interactive/')
urlkb.add(urlButton, urlButton2, urlButton3)

# @dp.message_handler(commands='presents')
@dp.message_handler(commands='presents')
async def url_command(message: types.Message, state: FSMContext):
   await message.answer('Выберете вариант презентации:', reply_markup=urlkb)


@dp.message_handler(commands=['start'], state=InputStates.mainMenu)
async def send_welcome(message: types.Message, state: FSMContext):
   kb = [
       [
           types.KeyboardButton(text="Презентации"),
           types.KeyboardButton(text="Кейсы"),
           types.KeyboardButton(text="Контакты")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
 
   await message.reply("Привет!\n\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)

@dp.message_handler()
async def echo(message: types.Message, state: FSMContext):
    # await message.answer(message.text)
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)