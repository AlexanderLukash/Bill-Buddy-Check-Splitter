from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


inline_test_keyboard_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Test🩲",
                callback_data="test_callback",
            ),
        ],
    ],
)
