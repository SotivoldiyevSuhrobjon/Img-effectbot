import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils.exceptions import BotBlocked

from database.connections import get_all_users
from loader import bot
from data.config import ADMINS
from states.AllStates import AdminStates


async def start_admin_handler(message: Message):
    user_id = message.from_user.id
    if user_id in ADMINS:
        await message.answer("Xabaringizni yozing adminjon")
        await AdminStates.get_message.set()


async def get_admin_message_state(message: Message, state: FSMContext):
    text = message.text
    users = await get_all_users()
    sent = 0
    error = 0
    for user in users:
        try:
            await bot.send_message(chat_id=user['user_id'], text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except BotBlocked:
            error += 1
            continue
    await message.answer(f"Yuborildi: {sent}\nBlock userlar: {error}")
    await state.finish()


def register_admins_py(dp: Dispatcher):
    dp.register_message_handler(start_admin_handler, commands=['admin'])
    dp.register_message_handler(get_admin_message_state, state=AdminStates.get_message)
