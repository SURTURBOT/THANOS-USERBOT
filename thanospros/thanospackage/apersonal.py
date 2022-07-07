# this plugin maked by @thanosceo for thanos pro kang whith credits 
#thanos pro
import asyncio
from thanospros import *
from THANOSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from thanospros.cmdhelp import CmdHelp
from thanospros import ALIVE_NAME
#thanospro
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT"


@borg.on(admin_cmd(outgoing=True, pattern="^Pm$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("❤")
    animation_chars = [
        "ＳＵＮ♢",
        "ＰΞＲＳ♢ＮΛＬ ＭΞＳＳΛＧΞ ＫΛＲ♢",
        f"ＰΞＲＳ♢ＮΛＬ ＭΞＳＳΛＧΞ ＫΛＲ♢",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 

from thanospros.cmdhelp import CmdHelp

CmdHelp("PERSONAL").add_command("^Pm", None, "PM FULL FORM").add()
