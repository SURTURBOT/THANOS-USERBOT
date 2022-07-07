# this plugin maked by @thanosceo for thanos pro kang with credits 
#thanos pro
import asyncio
from thanospros import *
from THANOSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from thanospros.cmdhelp import CmdHelp
from thanospros import ALIVE_NAME
#thanospro
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT"


@borg.on(admin_cmd(outgoing=True, pattern="^Mcb$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "SUNO",
        "TUM MADARCHOD HO 🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",
        f"SUNO TUM MADARCHOD HO 🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



@borg.on(admin_cmd(outgoing=True, pattern="^Mc$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "SUNO",
        "TU MADARCHOD HAI🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",
        f"SUNO PAGAL GIRL TU MADARCHOD HAI 🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



@borg.on(admin_cmd(outgoing=True, pattern="^Bc$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "Behanchod",
        "Behanchod",
        f"Behanchod",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 


@borg.on(admin_cmd(outgoing=True, pattern="^Bsdk$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "Bhosdike",
        "TUM Bhosdike  🤣🤣🤣 ",
        f"tere MAA bhi  Bhosdike",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



from thanospros.cmdhelp import CmdHelp

CmdHelp("AGALI").add_command("^Mcb", None, "Use this plugin to boy and see").add_command( 
    "^Mc", None, "Use and see  girls"
).add_command("^Bc", None, "Use and see").add_command(
    "^Bsdk", None, "Use and see"
).add()
