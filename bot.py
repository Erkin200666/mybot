import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# MAǴLIWMATLAR
API_TOKEN = '8233547910:AAE9wT0MsoRtP3MzbJSlZTM1OdLMXqYplR8'
USER_ID = 8328765581 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")

# SABAQ KESTESI
lessons = {
    0: "Dúyshembi:\n1. 08:30 Jasalma intellekt (309)\n2. 10:00 Differenciallıq teńlemeler (329)",
    1: "Sheshembi:\n1. 08:30 Python (318)\n2. 10:00 Itimallıq (323)\n3. 11:30 Aǵartıwshılıq (331)",
    2: "Sárshembi:\n1. 10:00 Python (318)\n2. 11:30 Itimallıq (323)",
    3: "Piyshembi:\n1. 08:30 Itimallıq (323)\n2. 10:00 Kiberqáwipsizlik (318)\n3. 11:30 Jasalma intellekt (318)",
    4: "Juma:\n1. 08:30 Python (318)\n2. 10:00 Kiberqáwipsizlik (318)",
    5: "Shembi:\n1. 08:30 Jasalma intellekt (323)\n2. 10:00 Differenciallıq teńlemeler (331)"
}

async def send_msg(text):
    try:
        await bot.send_message(USER_ID, text)
    except Exception as e:
        print(f"Qáte: {e}")

async def evening_reminder():
    tomorrow = (datetime.now().weekday() + 1) % 7
    msg = lessons.get(tomorrow, "Erteń dem alıs kúni!")
    await send_msg(f"🌙 Keshki saat 9 boldı. Erteńgi keste:\n\n{msg}")

def setup_jobs():
    scheduler.add_job(send_msg, 'cron', hour=7, minute=0, args=["☀️ Qalaysiz Qutibaev Erkinbay, jaqsi dem aldinizba? Turin oqiwga kesh qalasiz!"])
    scheduler.add_job(evening_reminder, 'cron', hour=21, minute=0)
    scheduler.add_job(send_msg, 'cron', hour=0, minute=0, args=["🌕 Erkinbay uyqilan bold erten oqiw tura almaysiz!"])

async def main():
    setup_jobs()
    scheduler.start()
    print("Bot iske tústi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
