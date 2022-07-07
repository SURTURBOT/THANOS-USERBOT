import datetime

from telethon import version

from thanospros import *
from thanospros.cmdhelp import CmdHelp
from thanospros.Config import Config
from thanospros.thanospackage.sql_helper.globals import addgvar, delgvar, gvarstatus
from thanospros.utils import *

THANOSBOT_USER = bot.me.first_name
THANOSBOT = bot.uid
THANOSBOT_mention = f"[{THANOSBOT_USER}](tg://user?id={THANOSBOT})"

gban_pic = "./thanospros/thanospackage/thanosresource/pics/gban.mp4"
main_pic = "./thanospros/thanospackage/thanosresource/pics/main.jpg"
core_pic = "./thanospros/thanospackage/thanosresource/pics/core.jpg"
chup_pic = "./thanospros/thanospackage/thanosresource/pics/chup.mp4"
bsdk_pic = "./thanospros/thanospackage/thanosresource/pics/bsdk.jpg"
bsdkwale_pic = "./thanospros/thanospackage/thanosresource/pics/bsdk_wale.jpg"
chutiya_pic = "./thanospros/thanospackage/thanosresource/pics/chutiya.jpg"

perf = "[ THANOS-PRO ]"


DEVLIST = ["2143095429"]


async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid


l1 = Config.HANDLER
l2 = Config.SUDO_HANDLER
sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m = "Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.YOUR_CHANNEL or "thanos_userbots"
my_group = Config.YOUR_GROUP or "thanosbot_chats"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")


mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

chnl_link = "https://t.me/thanos_userbots"
THANOSBOT_channel = f"[THANOS-PRO]({chnl_link})"
grp_link = "https://t.me/thanos_userbots"
THANOSBOT_grp = f"[THANOS Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
