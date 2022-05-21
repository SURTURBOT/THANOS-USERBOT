# THANOS-PRO Assistant
from telethon import Button, custom

from thanospros import ALIVE_NAME, bot

from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


THANOSBOT_USER = bot.me.first_name
THANOSCEO = bot.uid

THANOSBOT_mention = f"[{THANOSBOT_USER}](tg://user?id={THANOSCEO})"
gban_pic = "./thanospros/thanospackage/thanosresource/pics/gban.mp4"
main_pic = "./thanospros/thanospackage/thanosresource/pics/main.jpg"
core_pic = "./thanospros/thanospackage/thanosresource/pics/core.jpg"
chup_pic = "./thanospros/thanospackage/thanosresource/pics/chup.mp4"
bsdk_pic = "./thanospros/thanospackage/thanosresource/pics/bsdk.jpg"
bsdkwale_pic = "./thanospros/thanospackage/thanosresource/pics/bsdk_wale.jpg"
chutiya_pic = "./thanospros/thanospackage/thanosresource/pics/chutiya.jpg"
THANOSBOTversion = "3.0"

perf = "[ THANOS-PRO ]"


DEVLIST = ["2143095429"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
