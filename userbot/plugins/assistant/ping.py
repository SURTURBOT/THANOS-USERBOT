import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

THANOSBOT_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

THANOS = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ Lêɠêɳ̃dẞø† ⚜", "https://t.me/LegendBot_Pros")]]
    await tgbot.send_file(event.chat_id, THANOSBOT_IMG, caption=LegendBoy, buttons=GOOD)
