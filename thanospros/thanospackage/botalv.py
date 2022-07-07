from telethon import version

from thanospros import *
from thanospros.cmdhelp import CmdHelp
from thanospros.utils import *

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOS"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

THANOSBOT = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={THANOSBOT})"


PM_IMG = "https://telegra.ph/file/c8fe5de96a7968636edc4.mp4"
pm_caption = "**Շђคภ๏ร-קг๏ 𝙸𝚜 𝙾𝚗𝚕𝚒𝚗𝚎**\n\n"

pm_caption += f"**┏💞Շђคภ๏ร-קг๏💞┓**\n"
pm_caption += f"**┣⚡ 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣⚡ 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣⚡ Linux-Mix  : {7.2}(t.me/legendhacker_iin)\n"
pm_caption += f"**┣⚡ Շђคภ๏ร-קг๏ : {THANOSBOTversion}**\n"
pm_caption += f"**┣⚡ 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣⚡ 𝙾𝚠𝚗𝚎𝚛     : [Շђคภ๏ร](https://t.me/thanosceo)**\n"
pm_caption += f"**┗[💕𝙶𝚛𝚘𝚞𝚙💕](https://t.me/+cJG1PbKtpPVmNDg5)┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/thanosuser/THANOS-PRO) "


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
