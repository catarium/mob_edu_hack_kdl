import asyncio
import logging

from bot.misc import database_init, dp, bot, setup

# import aioschedule as schedule

logger = logging.getLogger(__name__)


async def main():
    # await notifier.enable()
    setup()
    database_init()
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")