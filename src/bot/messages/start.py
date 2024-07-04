from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from src.bot.messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    text = (
        "👋 Welcome to our bot for splitting checks between friends!"
        "This bot will help you and your friends easily split bills in restaurants, cafes and bars, "
        "so that everyone knows how much and what they pay for. \n\n"
        "Choose what you want to do"
    )
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Add a friend", callback_data="friend"),
                InlineKeyboardButton(text="Add a check", url="https://ya.ru"),
            ],
        ],
        # resize_keyboard=True,
    )
