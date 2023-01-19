import asyncio
from events import get
import random
import os

@get(pattern=".upload")
async def download(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await event.client.download_media(reply_message.media, "downloads/")
        await event.edit("Downloaded to `downloads/` folder")
    else:
        await event.edit("Reply to a media to download it")

# if user message .uploadlist then send the list of files in downloads folder
@get(pattern=".downloads")
async def uploadlist(event):
    files = os.listdir("downloads/")
    msg = ""
    for file in files:
        msg += file + "\n"
    await event.edit(f"**Files in downloads folder:**\n\n```{msg}```")

# if user message .download then send the file from downloads folder
@get(pattern=".download")
async def upload(event):
    input = event.text[10:]
    if input in os.listdir("downloads/"):
        await event.client.send_file(
            event.chat_id,
            "downloads/" + input,
            caption="Here is the requested file",
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
        )
        await event.delete()
    else:
        await event.edit("File not found in downloads folder")

# if user message .delete then delete the file from downloads folder
@get(pattern=".delete")
async def delete(event):
    input = event.text[8:]
    if input in os.listdir("downloads/"):
        os.remove
        await event.edit(f"Deleted `{input}` from downloads folder")
    else:
        await event.edit("File not found in downloads folder")

        
