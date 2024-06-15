# Creating a router instance
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.bot.keyboards.inline import inline_test_keyboard_button


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}",
        reply_markup=inline_test_keyboard_button,
    )
