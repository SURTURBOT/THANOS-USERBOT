import asyncio

from thanospros.cmdhelp import CmdHelp
from thanospros.utils import admin_cmd

from . import *


@bot.on(admin_cmd(pattern="byeall"))
async def _(event):
    await event.edit("Guys I Gotta Go!")
    await asyncio.sleep(3)
    await event.edit(
        """
╭━━┳╮╱╱╭┳━━━┳━━━┳╮💕💕╭╮
┃╭╮┃╰╮╭╯┃╭━━┫╭━╮┃┃💕💕┃┃
┃╰╯╰╮╰╯╭┫╰━━┫┃💞┃┃┃💕💕┃┃
┃╭━╮┣╮╭╯┃╭━━┫╰━╯┃┃💕  ┫┃💕╭╮
┃╰━╯┃┃┃╱┃╰━━┫╭━╮┃╰━╯┃╰━╯┃
╰━━━╯╰╯╱╰━━━┻╯💕╰┻━━━┻━━━╯
       [💞»»»Շђคภ๏ร-קг๏«««💞](https://t.me/thanosbot_chats)
"""
    )


CmdHelp("byeall").add_command("byeall", None, "Say Bye to U all in anmation").add()
