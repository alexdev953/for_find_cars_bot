import asyncio
from translator import Cyrillic
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from db_func import DBFunc
from bot_utils import FormatMessage


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(lambda message: DBFunc().check_user(message),
                    commands=['start'])
async def take_start(message: types.Message):
    about_bot = await bot.get_me()
    await message.answer(
        f"Привіт, {message.from_user.first_name}!\nЯ - <b>{about_bot['first_name']}</b>")


@dp.message_handler(lambda message: DBFunc().check_user(message), regexp='^[A-Za-z]|[А-ЯҐЄІЇ]{2}[0-9]{4}[A-Z a-z]|[А-ЯҐЄІЇ]{2}|%$')
async def take_numberplate(message: types.Message):
    number_plate = Cyrillic().transliterate(message.text).upper()
    data_lp = DBFunc().get_info_by_number_plate(number_plate)
    message_list = FormatMessage().format_msg_lp(data_lp, number_plate)
    if isinstance(message_list, list):
        for text, inline_key in message_list:
            await message.answer(text=text, reply_markup=inline_key)
            await asyncio.sleep(0.5)
    else:
        await message.answer(message_list)


@dp.callback_query_handler(text_startswith=['v@'])
async def take_vin_id(query: types.CallbackQuery):
    await bot.answer_callback_query(query.id, '🔭 Шукаю по VIN')
    vin_id = query.data.split('@')[1]
    data_list = DBFunc().get_info_by_vin_id(vin_id)
    answer_list = FormatMessage().format_msg_vin(data_list)
    for text in answer_list:
        await query.message.answer(text)
        await asyncio.sleep(0.5)


@dp.errors_handler()
async def send_admin(update: types.Update, error):
    """
    Take error in bot and send to admin and user
    """
    if not isinstance(error, TimeoutError):
        name_error = f'{error}'.replace('<', '').replace('>', '')
        message_to_admin = f"""Сталася помилка в боті:\n{name_error}\nПри запиті:\n{update}"""
        await bot.send_message(379210271, message_to_admin)
        if update.message:
            await update.message.answer('Сталася загальна помилка')
        elif update.callback_query:
            await update.callback_query.message.answer(f'Сталася загальна помилка: {error}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
