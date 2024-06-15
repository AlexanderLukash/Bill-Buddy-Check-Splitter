from aiohttp import web
from src.api.internal.views.probes import healthcheck_view


router = (web.get("/api/internal/healthcheck", healthcheck_view),)
