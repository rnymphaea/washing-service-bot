import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook

import config
from handlers import admin, common

TOKEN = config.get("TOKEN")
ADMIN_SECRET = config.get("ADMIN_SECRET")

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат сообщения
    handlers=[
        logging.StreamHandler(),  # Вывод в консоль
        # logging.FileHandler("bot.log", encoding="utf-8")  # Запись в файл
    ]
)

logger = logging.getLogger(__name__)


async def main():
    logger.info("Bot started")
    dp.include_routers(admin.router, common.router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
