from aiohttp import web


async def healthcheck_view(request):
    return web.json_response({"status": "ok"})
