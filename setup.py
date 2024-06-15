import logging

from aiohttp import web
from src.web import init_app


def main():
    app = init_app()
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)


if __name__ == "__main__":
    main()
