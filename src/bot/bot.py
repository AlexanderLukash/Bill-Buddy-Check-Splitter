from aiogram import (
    Bot,
    Dispatcher,
)
from src.bot.handlers import user_commands
from src.core.configs import settings


async def init_dispatcher():
    bot = Bot(token=settings.TELEGRAM_API_KEY)
    await bot.set_webhook(settings.telegram_web_hook)

    dispatcher = Dispatcher()

    dispatcher.include_routers(
        user_commands.router,
    )

    return bot, dispatcher
