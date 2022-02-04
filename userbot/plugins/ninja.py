# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon.errors import rpcbaseerrors

from userbot import LOGGER, LOGGER_ID
from userbot.utils import admin_cmd, errors_handler, sudo_cmd


@bot.on(admin_cmd(outgoing=True, pattern="del$"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="del$"))
@errors_handler
async def delete_it(safai):
    """For .del command, delete the replied message."""
    msg_src = await safai.get_reply_message()
    if safai.reply_to_msg_id:
        try:
            await msg_src.delete()
            await safai.delete()
            if LOGGER:
                await delme.client.send_message(
                    LOGGER_ID, "#DEL \nDeletion of message was successful"
                )
        except rpcbaseerrors.BadRequestError:
            if LOGGER:
                await delme.client.send_message(
                    LOGGER_ID, "Well, I can't delete a message"
                )
