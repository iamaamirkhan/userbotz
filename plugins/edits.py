import asyncio
from events import get
import random
import os
RUNSREACTS = [
    "`Congratulations and BRAVO SIS!`",
    "`Aww Sis You did it! So proud of you Congo!`",
    "`OMG Sis This calls for celebrating! Congratulations!`",
    "`I knew it was only a matter of time. Well done!`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
    "`Congratulations on your success!`",
    
]
@get(pattern=".gm")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Good")
        await asyncio.sleep(0.7)
        await event.edit("Morning")
        await asyncio.sleep(1)
        await event.edit("Have")
        await asyncio.sleep(0.8)
        await event.edit("A")
        await asyncio.sleep(0.9)
        await event.edit("Nice")
        await asyncio.sleep(1)
        await event.edit("Day")
        await asyncio.sleep(0.8)
        await event.edit("`Good Morning Have A Nice Day`")
        
@get(pattern=".congo")
async def congo(event):
    await event.edit(random.choice(RUNSREACTS))

@get(pattern=".coin")
async def coin(event):
    await event.edit(random.choice(["Heads", "Tails"]), parse_mode="html")

@get(pattern=".dice")
async def dice(event):
    await event.edit(random.choice(["1", "2", "3", "4", "5", "6"]), parse_mode="html")

@get(pattern=".decide")
async def decide(event):
    await event.edit(random.choice(["Yes", "No", "Maybe"]), parse_mode="html")

@get(pattern=".degi")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Wo")
        await asyncio.sleep(0.7)
        await event.edit("Degi")
        await asyncio.sleep(1)
        await event.edit("Tum")
        await asyncio.sleep(0.8)
        await event.edit("Ekbar")
        await asyncio.sleep(0.9)
        await event.edit("Mang")
        await asyncio.sleep(1)
        await event.edit("Kar")
        await asyncio.sleep(0.8)
        await event.edit("Toh")
        await asyncio.sleep(0.7)
        await event.edit("Dekho")
        await asyncio.sleep(1)
        await event.edit("`Wo Degi Tum Ekbar Mang Kar toh Dekho`")


@get(pattern=".spam")
async def spam(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        text = event.text
        text = text[6:]
        await event.delete()
        for i in range(100):
            await event.respond(text)


# if user message .hi then bot will reply with many ways
@get(pattern=".hi")
async def hi(event):
    await event.edit(random.choice(["`Hi`", "`Hey`", "`Heya`", "`Hiya`", "`Hi!`", "`Hey!`", "`Heya!`", "`Hiya!`", "`Hii sunshine!`"]), parse_mode="html")


# if user message .hello then bot will reply with many ways
@get(pattern=".hello")
async def hello(event):
    await event.edit(random.choice(["`Hello`", "`Hi`", "`Hey`", "`Heya`", "`Hiya`", "`Hello!`", "`Hi!`", "`Hey!`", "`Heya!`", "`Hiya!`", "`Hello sunshine!`"]), parse_mode="html")

# if user message .bye then bot will reply with many ways
@get(pattern=".bye")
async def bye(event):
    await event.edit(random.choice(["`Bye`", "`Bye!`", "`Bye Bye!`", "`Bye Bye`", "`Bye Bye! See you soon`", "`Bye Bye! Take care`", "`Bye Bye! Have a nice day`", "`Bye Bye! Have a nice life`", "`Bye Bye! Have a nice time`"]), parse_mode="html")

# if user message .hru then bot will reply with many ways
@get(pattern=".hru")
async def hru(event):
    await event.edit(random.choice(["`I am fine, How are you?`", "`I am fine, How are you doing?`", "`I am fine, How are you today?`", "`I am fine, How are you this fine day?`", "`I am fine, How are you this fine morning?`", "`I am fine, How are you this fine evening?`", "`I am fine, How are you this fine night?`", "`I am fine, How are you this fine afternoon?`"]), parse_mode="html")

    


