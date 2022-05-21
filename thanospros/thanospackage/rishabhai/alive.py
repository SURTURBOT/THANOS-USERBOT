from telethon import events

from thanospros import *

from . import *

PM_IMG = "https://telegra.ph/file/c8fe5de96a7968636edc4.mp4"
pm_caption = f"💔THANOS-PRO IS NEVER SLEEP💔 \n\n"
pm_caption += f"๏ฬภєг ~ 『{THANOSBOT_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣тнαησѕ~ `{THANOSBOTversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/thanos_userbots)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/thanosuser/ThanosBot/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [тнαησѕ ](https://t.me/thanos_pro)\n"
pm_caption += f"┣Assistant ~ By [·.·•тнαησѕ•·.· ](https://t.me/THANOSCEO)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [·.·•тнαησѕ•·.·](https://t.me/THANOSBOT_CHATS) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
