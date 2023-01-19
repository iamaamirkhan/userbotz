import os
import sys
import time
from events import get

@get(pattern=".start")
async def start(event):
    await event.edit("Hello World!")

@get(pattern=".alive")
async def alive(event):
    await event.edit("I'm alive")

@get(pattern=".ping")
async def ping(event):
    start = time.time()
    await event.edit('Pong!')
    end = time.time()
    await event.edit(f'Pong! `{round((end - start) * 1000)}ms`')
    

@get(pattern=".stop")
async def stop(event):
    await event.edit("Stopping...")
    exit()


    