import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.dispatcher.filters import Text, Command
 
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
@dp.message_handler(Text(equals=['🔙 Вернуться в меню']))
async def send_main_menu(message: types.Message, state: FSMContext):
    kb_main_menu = [
        [
            types.KeyboardButton(text="📊 Презентации"),
            types.KeyboardButton(text="📁 Кейсы"),
            types.KeyboardButton(text="📞 Контакты")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_main_menu, resize_keyboard=True)
 
    # await message.reply("Привет!\n\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)
    await message.answer_photo(photo=LOGO_URL, caption="Привет!👋\n\nЭто стартовое сообщение. Выберите вариант из меню", reply_markup=keyboard)

urlkb_pres = InlineKeyboardMarkup(row_width=1)
urlButton1_pres = InlineKeyboardButton(text='📄 Общая презентация (разработка музеев и выставок)', url='https://appollopro.ru/razrabotka-muzeev-i-vystavok/')
urlButton2_pres = InlineKeyboardButton(text='💻 Для разработчиков (ПО для шлемов VR/AR/MR)', url='https://appollopro.ru/po-dlya-shlemov-vr-mr/')
urlButton3_pres = InlineKeyboardButton(text='🛠️ Для агентств (Интерактивное оборудование)', url='https://appollopro.ru/interactive/')
urlkb_pres.add(urlButton1_pres, urlButton2_pres, urlButton3_pres)

urlkb_keys = InlineKeyboardMarkup(row_width=1)
urlButton1_keys = InlineKeyboardButton(text='🎨 Интерактивная выставка Музея Военной Формы "Суворовцы и Нахимовцы"', url='https://appollopro.ru/cases/interaktivnaya-vystavka-muzeya-voennoj-formy-suvorovczy-i-nahimovczy/')
urlButton2_keys = InlineKeyboardButton(text='🕶️ VR приложение ACUVUE', url='https://appollopro.ru/cases/vr-prilozhenie-dlya-kompanii-acuvue/')
urlButton3_keys = InlineKeyboardButton(text='🖼️ Интерактивная выставка в Музее Военной Формы "Охотники и собиратели"', url='https://appollopro.ru/cases/interaktivnaya-vystavka-v-muzee-voennoj-formy/')
urlkb_keys.add(urlButton1_keys, urlButton2_keys, urlButton3_keys)

urlkb_contacts = InlineKeyboardMarkup(row_width=1)
urlButton1_contacts = InlineKeyboardButton(text='📞 Позвонить', callback_data='call_contact')
urlButton2_contacts = InlineKeyboardButton(text='🌐 Наш сайт', url='https://appollopro.ru/')
urlButton3_contacts = InlineKeyboardButton(text='📱 Телеграмм', url='https://telegram.me/Appollo_digital_bot')
urlButton4_contacts = InlineKeyboardButton(text='✉️ Почта', callback_data='call_email')
urlkb_contacts .add(urlButton1_contacts , urlButton2_contacts , urlButton3_contacts )

@dp.callback_query_handler(lambda c: c.data == 'call_contact')
async def process_callback_call_contact(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "📞 Позвонить по номеру: +74952150494")

@dp.callback_query_handler(lambda c: c.data == 'call_email')
async def process_callback_call_contact(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "✉️ Написать на почту: info@appollopro.ru")

kb_back= [
        [
            types.KeyboardButton(text="🔙 Вернуться в меню"),
        ],
    ]
keyboard_back = types.ReplyKeyboardMarkup(keyboard=kb_back, resize_keyboard=True)

# @dp.message_handler(commands='presents')
@dp.message_handler(Text(equals=['📊 Презентации']))
async def url_command(message: types.Message, state: FSMContext):
   await message.answer('Выберете вариант презентации:', reply_markup=urlkb_pres)
   await message.answer('Или нажмите "Назад", чтобы вернуться в меню.', reply_markup=keyboard_back)

@dp.message_handler(Text(equals=['📁 Кейсы']))
async def url_command(message: types.Message, state: FSMContext):
   await message.answer('Наши кейсы:', reply_markup=urlkb_keys)
   await message.answer('Или нажмите "Назад", чтобы вернуться в меню.', reply_markup=keyboard_back)

@dp.message_handler(Text(equals=['📞 Контакты']))
async def url_command(message: types.Message, state: FSMContext):
   await message.answer('Адрес производства: Электролитный пр., 3, стр. 2. \n\nОфис в Калининграде: Красносельская ул., 18 \n\n+7(495)215-04-94 \ninfo@appollopro.ru')
   await message.answer('Наши контакты:', reply_markup=urlkb_contacts)
   await message.answer('Нажмите "Назад", чтобы вернуться в меню.', reply_markup=keyboard_back)

@dp.message_handler()
async def echo(message: types.Message, state: FSMContext):
    # await message.answer(message.text)
   await message.answer("Такого варианта нет. Выберете вариант из меню")
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)