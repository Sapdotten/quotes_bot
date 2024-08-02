import asyncio
import logging
import pytz
import datetime

logging.basicConfig(level=logging.INFO)

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from utils.settings import Settings

from database import init
from database import user_manager as um

from handlers.quote import register_bot
from handlers import quote

from giga_module import giga

moscow_tz = pytz.timezone('Europe/Moscow')


def register_routers(dp):
    dp.include_routers(quote.router)


async def daily_task(bot: Bot):
    while True:
        now = datetime.datetime.now(moscow_tz)
        target_time = now.replace(hour=4, minute=00, second=0, microsecond=0)

        # Если сейчас время после 6 утра, установим цель на следующий день
        if now > target_time:
            target_time += datetime.timedelta(days=1)

        # Время до следующего запуска задачи
        wait_time = (target_time - now).total_seconds()

        # Ждем до следующего запуска
        await asyncio.sleep(wait_time)
        
        # Выполнение твоей задачи
        logging.info("start of emailing")
        users = await um.get_all_users()
        for user in users:
            await bot.send_message(chat_id=user[0], text="Доброе утро, котенок!")
            text = giga.get_morning_quote(user[1])
            await bot.send_message(chat_id=user[0], text=text)
        logging.info("end of emailing")
            
        # Здесь ты можешь добавить выполнение твоей конкретной задачи

async def main() -> None:
    """
    Entry point
    """
    # load_environ()
    await init.init_models()
    
    Settings.load_data_from_file()
    
    session = AiohttpSession()
    bot = Bot(Settings.get_token(), session=session)
    register_bot(bot)
    dp = Dispatcher()
    register_routers(dp)
    
    bot_task = dp.start_polling(bot)
    daily_task_coro = daily_task(bot)
    try:
        await bot.delete_webhook()
        await asyncio.gather(bot_task, daily_task_coro)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    asyncio.run(main())