# Plugin by @Rishisuperyo
# Animation by kiddo
# kang =gey ,keep credits = cool coder š¶
# usage .gim
from thanospros.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"gim", outgoing=True))
async def hapy(event):

    a = "š±āāāāāāš±\nš        \         /          š\nā­          \š/            ā­\nāØ           š½             āØ\n              /    \ \n            š    š"
    await event.edit(a)


from thanospros.cmdhelp import CmdHelp

CmdHelp("gim").add_command("gim", None, "Get info about a File Extension").add()
