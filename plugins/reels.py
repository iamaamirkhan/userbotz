from plugins.functions.insta import instadownload
import time
from events import get
import re


@get(pattern=".reel")
async def reel(event):
    # if reply message is link then download the reel
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.text:
            # link regex
            link = re.search(r'(https?://[^\s]+)', reply_message.text)
            if link:
                # download the reel
                video_url = instadownload(link.group(1))
                # send the reel
                await event.client.send_file(event.chat_id, video_url)
                await event.delete()
            else:
                await event.edit('Reply to a link')
        else:
            await event.edit('Reply to a link')
    elif event.message.text:
        # link regex
        link = re.search(r'(https?://[^\s]+)', event.message.text)
        if link:
            # download the reel
            video_url = instadownload(link.group(1))
            # send the reel
            await event.client.send_file(event.chat_id, video_url)
            await event.delete()
        else:
            await event.edit('Reply to a link')
