from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from src.bot.messages.base import BaseMessageBuilder


class AddFriendMessageBuilder(BaseMessageBuilder):
    text = "🤝 Okay, let's add a new friend. \n" "Select adding method:"
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Add manually", url="https://ya.ru"),
                InlineKeyboardButton(text="Send an invitation", url="https://ya.ru"),
            ],
        ],
        # resize_keyboard=True,
    )
