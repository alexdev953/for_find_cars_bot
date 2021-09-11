import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import API_TOKEN
from db_func import DBFunc


memory_storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=memory_storage)


@dp.message_handler(lambda message: DBFunc().check_user(message),
                    commands=['start'])
async def take_start(message: types.Message):
    about_bot = await bot.get_me()
    await message.answer(
        f"Привіт, {message.from_user.first_name}!\nЯ - <b>{about_bot['first_name']}</b>")


@dp.message_handler(regexp='^[A-Za-z]{2}[0-9]{4}[A-Z a-z]{2}|%$')
async def take_numberplate(message: types.Message):
    number_plate = message.text
    DBFunc().get_info_by_number_plate(number_plate)

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