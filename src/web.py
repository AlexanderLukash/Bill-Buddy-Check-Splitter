from aiohttp import web
from src.api.internal.router import router as internal_router
from src.bot.bot import init_dispatcher
from src.bot.view import TelegramWebhookView
from src.core.configs import settings


async def init_app() -> web.Application:
    app = web.Application()

    app.router.add_routes(internal_router)
    bot, dispatcher = await init_dispatcher()
    app.router.add_route(
        "*",
        settings.TELEGRAM_WEBHOOK_PATH,
        TelegramWebhookView(dispatcher=dispatcher, bot=bot),
        name="telegram_webhook_handler",
    )
    return app
