# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#THIS PLUGIN MODED BY RISHABH

import asyncio

from thanospros.cmdhelp import CmdHelp
from thanospros.Config import Config
from thanospros.utils import admin_cmd, sudo_cmd

from . import THANOSBOT_mention

SUDO_WALA = Config.SUDO_USERS
lg_id = Config.LOGGER_ID






@bot.on(admin_cmd("chatf (.*)"))
@bot.on(sudo_cmd(pattern="chatf (.*)", allow_sudo=True))
async def spam(event):
    chatf = str("".join(event.text.split(maxsplit=1)[1:]))
    message = chatf.split()
    await event.delete()
    for word in message:
        await event.respond(word)
    if lg_id:
        if event.is_private:
            await event.client.send_message(
                lg_id,
                "#CHATF\n"
                + f"Word Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with : `{message}`",
            )
        else:
            await event.client.send_message(
                lg_id,
                "#CHATF\n"
                + f"Word Spam was executed successfully in {THANOSBOT_mention} chat with : `{message}`",
            )




CmdHelp("CHATFIGHT").add_command(
    "chatf", "Use like this", "chatf thanos is op"
).add()
