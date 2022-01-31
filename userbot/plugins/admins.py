from asyncio import sleep

from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)
from telethon.utils import get_display_name

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.helpers.events import get_user_from_event, get_user_from_init
from userbot.helpers.utils import _format
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from userbot.utils import *

from . import *

lg_id = Config.LOGGER_ID
# =================== CONSTANT ===================

PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing the image`"
NO_ADMIN = "`I am not an admin! Chutiya sala`"
NO_PERM = "`I don't have sufficient permissions! Sed -_-`"
INVALID_MEDIA = "`Invalid media Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================

NORMAL_PIC = os.environ.get("NORMAL_PIC", None)
if NORMAL_PIC:
    THANOSBOT = [x for x in NORMAL_PIC.split()]
    PIC = list(THANOSBOT)
    help_pic = random.choice(PIC)
else:
    help_pic = main_pic


@bot.on(admin_cmd("setgpic$"))
@bot.on(sudo_cmd(pattern="setgpic$", allow_sudo=True))
@errors_handler
async def set_group_photo(gpic):
    if gpic.fwd_from:
        return
    if not gpic.is_group:
        await edit_or_reply(gpic, "`I don't think this is a group.`")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await edit_or_reply(gpic, NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await edit_or_reply(gpic, INVALID_MEDIA)
    THANOSBOT = None
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await gpic.client.upload_file(photo))
            )
            await bot.send_file(
                gpic.chat_id,
                help_pic,
                caption=f"⚜ `Group Profile Pic Changed` ⚜\n🔰Chat ~ {gpic.chat.title}",
            )
            THANOSBOT = True
        except PhotoCropSizeSmallError:
            await edit_or_reply(gpic, PP_TOO_SMOL)
        except ImageProcessFailedError:
            await edit_or_reply(gpic, PP_ERROR)
        except Exception as e:
            await edit_or_reply(gpic, f"**Error : **`{str(e)}`")
        if LOGGER and THANOSBOT:
            await gpic.client.send_message(
                lg_id,
                "#GROUPPIC\n"
                f"Group profile pic changed "
                f"CHAT: {gpic.chat.title}(`{gpic.chat_id}`)",
            )


@bot.on(admin_cmd("promote(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="promote(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def promote(promt):
    if promt.fwd_from:
        return
    chat = await promt.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(promt, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    THANOSBOTevent = await edit_or_reply(promt, "Promoting...")
    user, rank = await get_user_from_init(promt)
    if not rank:
        rank = "тнαησѕ"
    if not user:
        return
    try:
        await promt.client(EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await bot.send_file(
            promt.chat_id,
            help_pic,
            caption=f"**⚜Promoted ~** [{user.first_name}](tg://user?id={user.id})⚜\n**Successfully In** ~ `{promt.chat.title}`!! \n**Admin Tag ~**  `{rank}`",
        )
    except BadRequestError:
        await THANOSBOTevent.edit(NO_PERM)
        return
    await promt.client.send_message(
        lg_id,
        "#PROMOTE\n"
        f"\nUSER: [{user.first_name}](tg://user?id={user.id})\n"
        f"CHAT: {promt.chat.title}(`{promt.chat_id}`)",
    )


@bot.on(admin_cmd("demote(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="demote(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def demote(dmod):
    if dmod.fwd_from:
        return
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(dmod, NO_ADMIN)
        return
    THANOSBOTevent = await edit_or_reply(dmod, "Demoting...")
    rank = "??????"
    user = await get_user_from_init(dmod)
    user = user[0]
    if not user:
        return
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await dmod.client(EditAdminRequest(dmod.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await THANOSBOTevent.edit(NO_PERM)
        return
    await bot.send_file(
        dmod.chat_id,
        help_pic,
        caption=f"Demoted Successfully\nUser:[{user.first_name}](tg://{user.id})\n Chat: {dmod.chat.title}",
    )
    if LOGGER:
        await dmod.client.send_message(
            lg_id,
            "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)",
        )


@bot.on(admin_cmd("ban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ban(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def _ban(event):
    user, reason = await get_user_from_init(event)
    if not user:
        return
    if user.id == event.client.uid:
        return await eod(event, "__You cant ban yourself.__")
    THANOSBOTevent = await edit_or_reply(event, "`Whacking the pest!`")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await THANOSBOTevent.edit(NO_PERM)
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await THANOSBOTevent.edit(
            "`I dont have message nuking rights! But still he is banned!`"
        )
    if reason:
        await bot.send_file(
            event.chat_id,
            help_pic,
            caption=f"{_format.mentionuser(user.first_name ,user.id)}` is banned !!`\n**Reason : **`{reason}`",
        )
    else:
        await bot.send_file(
            event.chat_id,
            help_pic,
            caption=f"{_format.mentionuser(user.first_name ,user.id)} `is banned !!`",
        )
    await event.delete()
    if LOGGER:
        if reason:
            await event.client.send_message(
                LOGGER_ID,
                f"#BAN\
                \nUSER: [{user.first_name}](tg://user?id={user.id})\
                \nCHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)\
                \nREASON : {reason}",
            )
        else:
            await event.client.send_message(
                LOGGER_ID,
                f"#BAN\
                \nUSER: [{user.first_name}](tg://user?id={user.id})\
                \nCHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd("unban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="unban(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def nothanos(unbon):
    if unbon.fwd_from:
        return
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(unbon, NO_ADMIN)
        return
    THANOSBOTevent = await edit_or_reply(unbon, "Unbanning...")
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await bot.send_file(
            unbon.chat_id,
            help_pic,
            f"[{user.first_name}](tg://user?id={user.id})has been unbanned Successfully In Chat: {unbon.chat_title} \nGiving one more chance 😏",
        )
        await THANOSBOTevent.delete()
        if LOGGER:
            await unbon.client.send_message(
                lg_id,
                "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)",
            )
    except UserIdInvalidError:
        await THANOSBOTevent.edit("Sorry I Can't Unban This Retard!")


@command(incoming=True)
async def watcher(event):
    if event.fwd_from:
        return
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@bot.on(admin_cmd("mute(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="mute(?: |$)(.*)", allow_sudo=True))
async def startmute(event):
    "To mute a person in that paticular chat"
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await sleep(2)
        await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "`This user is already muted in this chat ~~lmfao sed rip~~`"
            )
        if event.chat_id == bot.uid:
            return await edit_delete(event, "`You cant mute yourself`")
        try:
            mute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**Error **\n`{e}`")
        else:
            await bot.send_file(
                event.chat_id,
                help_pic,
                "`Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **`",
            )
        if LOGGER:
            await event.client.send_message(
                LOGGER_ID,
                "#PM_MUTE\n"
                f"**User :** [{replied_user.user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
            )
        user, reason = await get_user_from_init(event)
        if not user:
            return
        if user.id == bot.uid:
            return await edit_or_reply(event, "`Sorry, I can't mute myself`")
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(
                event, "`This user is already muted in this chat ~~lmfao sed rip~~`"
            )
        result = await event.client.get_permissions(event.chat_id, user.id)
        try:
            if result.participant.banned_rights.send_messages:
                return await edit_or_reply(
                    event,
                    "`This user is already muted in this chat ~~lmfao sed rip~~`",
                )
        except AttributeError:
            pass
        except Exception as e:
            return await edit_or_reply(event, f"**Error : **`{e}`")
        try:
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
                )
            mute(user.id, event.chat_id)
        except Exception as e:
            return await edit_or_reply(event, f"**Error : **`{e}`")
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is muted in {get_display_name(await event.get_chat())}`\n"
                f"`Reason:`{reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is muted in {get_display_name(await event.get_chat())}`\n",
            )
        if LOGGER:
            await event.client.send_message(
                LOGGER_ID,
                "#MUTE\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd("unmute(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="unmute(?: |$)(.*)", allow_sudo=True))
async def endmute(event):
    "To mute a person in that paticular chat"
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await sleep(1)
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        if not is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "`__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）`"
            )
        try:
            unmute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**Error **\n`{e}`")
        else:
            await bot.send_file(
                event.chat_id,
                help_pic,
                "`Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍`",
            )
        if LOGGER:
            await event.client.send_message(
                LOGGER_ID,
                "#PM_UNMUTE\n"
                f"**User :** [{replied_user.user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        user, _ = await get_user_from_init(event)
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client.get_permissions(event.chat_id, user.id)
                if result.participant.banned_rights.send_messages:
                    await event.client(
                        EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                    )
        except AttributeError:
            return await edit_or_reply(
                event,
                "`This user can already speak freely in this chat ~~lmfao sed rip~~`",
            )
        except Exception as e:
            return await edit_or_reply(event, f"**Error : **`{e}`")
        await edit_or_reply(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} `is unmuted in {get_display_name(await event.get_chat())}\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍`",
        )
        if LOGGER:
            await event.client.send_message(
                LOGGER_ID,
                "#UNMUTE\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd("pin($| (.*))"))
@bot.on(sudo_cmd(pattern="pin($| (.*))", allow_sudo=True))
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(msg, NO_ADMIN)
        return
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        await edit_or_reply(msg, "Reply to a message to pin it.")
        return
    options = msg.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await msg.client(UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await edit_or_reply(msg, NO_PERM)
        return
    hmm = await eod(msg, "ριииє∂ ѕυϲϲєѕѕƒυℓℓγ!")
    user = await get_user_from_id(msg.sender_id, msg)
    if LOGGER:
        await msg.client.send_message(
            lg_id,
            "#PIN\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
            f"LOUD: {not is_silent}",
        )
    await sleep(3)
    try:
        await hmm.delete()
    except:
        pass


@bot.on(admin_cmd("kick(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="kick(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def kick(usr):
    if usr.fwd_from:
        return
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(usr, NO_ADMIN)
        return
    user, reason = await get_user_from_init(usr)
    if not user:
        await edit_or_reply(usr, "Couldn't fetch user.")
        return
    THANOSBOTevent = await edit_or_reply(usr, "Kicking...")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        await THANOSBOTevent.edit(NO_PERM + f"\n{str(e)}")
        return
    if reason:
        await bot.send_file(
            usr.chat_id,
            help_pic,
            f"🔶Kicked [{user.first_name}](tg://user?id={user.id})!\n🔶яєαѕοи: {reason}",
        )
    else:
        await THANOSBOTevent.edit(f"Kicked [{user.first_name}](tg://user?id={user.id})!")
    if LOGGER:
        await usr.client.send_message(
            lg_id,
            "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}({usr.chat_id})\n",
        )


@bot.on(admin_cmd("undelete$"))
@bot.on(sudo_cmd(pattern="undelete$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await event.client.get_admin_log(
            event.chat_id, limit=5, edit=False, delete=True
        )
        deleted_msg = "Deleted message in this group:"
        for i in a:
            deleted_msg += "\n👉{}".format(i.old.message)
        await edit_or_reply(event, deleted_msg)
    else:
        await edit_or_reply(
            event, "You need administrative permissions in order to do this command"
        )
        await sleep(3)
        try:
            await event.delete()
        except:
            pass


async def get_user_from_init(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("Pass the user's username, id or reply!")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("Could not fetch info of that user.")
            return None
    return user_obj, extra


async def get_user_from_id(user, event):
    if event.fwd_from:
        return
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CmdHelp("admins").add_command(
    "setgpic", "<reply to image>", "Changes the groups display picture"
).add_command(
    "promote",
    "<username/reply> <custom rank (optional)>",
    "Provides admins right to a person in the chat.",
).add_command(
    "demote", "<username/reply>", "Revokes the person admin permissions    in the chat."
).add_command(
    "ban", "<username/reply> <reason (optional)>", "Bans the person off your chat."
).add_command(
    "unban", "<username/reply>", "Removes the ban from the person in the chat."
).add_command(
    "mute",
    "<username/reply> <reason (optional)>",
    "Mutes the person in the chat, works on admins too.",
).add_command(
    "unmute", "<username/reply>", "Removes the person from the muted list."
).add_command(
    "pin", "<reply> or .pin loud", "Pins the replied message in Group"
).add_command(
    "kick", "<username/reply>", "kick the person off your chat"
).add_command(
    "undelete", None, "display last 5 deleted messages in group."
).add()
