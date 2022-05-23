import asyncio

from thanospros.cmdhelp import CmdHelp

from thanospros.utils import admin_cmd, edit_or_reply, sudo_cmd

@bot.on(admin_cmd(pattern="ilovur$", outgoing=True))

@bot.on(sudo_cmd(pattern="ilovur$", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await edit_or_reply(event, "ilovur")

    animation_chars = [

        "i_",

        "il_",

        "ilo_",

        "ilov_",

        "ilovu_",

        "ilovub_",

        "ilovuba_",

        "ilovubaBu",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])

@bot.on(admin_cmd(pattern=r"amores$", outgoing=True))

@bot.on(sudo_cmd(pattern=r"amores$", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await edit_or_reply(event, "amores")

    animation_chars = [

        "A💙_",

        "AM💙_",

        "AMO💙_",

        "AMOR💙_",

        "AMORE💙_",

        "AMORE💙_",

        ".-.",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])

import asyncio

@bot.on(admin_cmd(pattern=r"sexys$", outgoing=True))

@bot.on(sudo_cmd(pattern=r"sexys$", allow_sudo=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await edit_or_reply(event, "Sexys")

    animation_chars = [

        "S_",

        "SE_",

        "SEX_",

        "SEXY_",

        "SEXY💋_",

        "SEXY💋",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])

@bot.on(admin_cmd(pattern="istars$", outgoing=True))

@bot.on(sudo_cmd(pattern="istars$", allow_sudo=True))

async def ammastar(THANOSBOTstar):

    if THANOSBOTstar.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    await edit_or_reply(THANOSBOTstar, "I am A Star")

    animation_chars = [

        "I Party like a rockstar",

        "I Look like a movie star",

        "I Play like an all star",

        "I Fuck like a pornstar",

        "Baby I'm a superstar",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await THANOSBOTstar.edit(animation_chars[i % 11])

@bot.on(admin_cmd(pattern=r"lmoons", outgoing=True))

@bot.on(sudo_cmd(pattern=r"lmoons", allow_sudo=True))

async def test(event):

    if event.fwd_from:

        return

    await edit_or_reply(

        event,

        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕",

    )

@bot.on(admin_cmd(pattern=r"city2", outgoing=True))

@bot.on(sudo_cmd(pattern=r"city2", allow_sudo=True))

async def test(event):

    if event.fwd_from:

        return

    await edit_or_reply(

        event,

        """☁☁🌞      ☁           ☁

       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫

              🌲/     l🚍\🌳👭

           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲

      🌲/   🚖     l               \

   🌳/🚶           |   🚍         \ 🌴🚴🚴

🌴/                    |                     \🌲""",

    )

@bot.on(admin_cmd(pattern=r"^Hiii", outgoing=True))

@bot.on(sudo_cmd(pattern=r"^Hiii", allow_sudo=True))

async def hi(event):

    if event.fwd_from:

        return

    await edit_or_reply(

        event, "💞✨✨💞✨💞💞💞\n💞✨✨💞✨✨💞✨\n💞💞💞💞✨✨💞✨\n💞✨✨💞✨✨💞✨\n💞✨✨💞✨💞💞💞\n💙💙💙💙💙💙💙💙"

    )

@bot.on(admin_cmd(pattern=r"cheerr", outgoing=True))

@bot.on(sudo_cmd(pattern=r"cheerr", allow_sudo=True))

async def cheer(event):

    if event.fwd_from:

        return

    await edit_or_reply(

        event,

        "🌹🌹😉😊🌹🌹\n☕ Cheer Up  🍵\n💕 ✨ )) ✨  💕\n💕┃ (( * ┣┓ 💕\n💕┃*💙 ┣┛ 💕 \n💕┗━━┛  💕🎂 For YOU  🍰\n🌹🌹😌😚🌹🌹",

    )

@bot.on(admin_cmd(pattern=r"getwells", outgoing=True))

@bot.on(sudo_cmd(pattern=r"getwells", allow_sudo=True))

async def getwell(event):

    if event.fwd_from:

        return

    await edit_or_reply(

        event, "🍁🍁🍁🍁🍁🍁🍁🍁🍁\n🍁😷😢😓😷😢💨🍁\n🍁💝💉🍵💊💐💝🍁\n🍁 GetBetter Soon! 🍁\n🍁🍁🍁🍁🍁🍁🍁🍁"

    )


    

@bot.on(admin_cmd(pattern=r"sprinkles", outgoing=True))

@bot.on(sudo_cmd(pattern=r"sprinkles", allow_sudo=True))

async def sprinkle(event):

    if event.fwd_from:

        return

    await edit_or_reply(

        event,

        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌹🌸🌹🌸🌹🌸🌹\n Sprinkled with love💙\n🍁🌻🍁🌻🍁🌻🍁🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n⚘🍀⚘🍀⚘🍀⚘🍀",

    )

@bot.on(admin_cmd(pattern=r"fstyles", outgoing=True))

@bot.on(sudo_cmd(pattern=r"fstyles", allow_sudo=True))

async def payf(event):

    if event.fwd_from:

        return

    paytext = event.pattern_match.group(1)

    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(

        paytext * 8,

        paytext * 8,

        paytext * 2,

        paytext * 2,

        paytext * 2,

        paytext * 6,

        paytext * 6,

        paytext * 2,

        paytext * 2,

        paytext * 2,

        paytext * 2,

        paytext * 2,

    )

    await edit_or_reply(event, pay)

CmdHelp("animation4").add_command("ilovur", None, "Animated I love u babu Typing").add_command(

    "amores", None, "Animated AMORE Typing"

).add_command("sexys", None, "Animated SEXY Typing").add_command(

    "unoob", None, "Animated text calling them noob🚶"

).add_command(

    "menoob", None, "Animated text claiming you noob"

).add_command(

    "uproo", None, "Animated text claiming you to be proooo"

).add_command(

    "mepro", None, "Animated text calling them proo Af!!"

).add_command(

    "sprinkle", None, "Use and see"

).add_command(

    "getwells", None, "Use and see"

).add_command(

    "cheer", None, "Use and see"

).add_command(

    "hiii", None, "Use and see"

).add_command(

    "city", None, "Use and see"

).add_command(

    "lmoon", None, "Use and see"

).add_command(

    "istar", None, "I am a Superstar⚡✨"

).add_command(

    "switch", None, "Click on the switch to reveal the price✨"

).add_command(

    "thanos", None, "A poem on Thanos... Maybe🤐"

).add_command(

    "tp", None, "Use and see"

).add_command(

    "fstyles", "<text>", "Prints the given text in 'F' format"

).add_command(

    "wahack", None, "Whatsapp Hack animation"

).add_type(

    "Addons"

).add()

# tha
