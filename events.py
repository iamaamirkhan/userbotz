import sys
import os

from numpy import get_include

from __init__ import app
from telethon import events
from loguru import logger
import os
import importlib.util
from time import gmtime, strftime
from traceback import format_exc

LOGS = logger
# Main Handler
def get(**kargs):
    def decorator(func):
        app.add_event_handler(func, events.NewMessage(**kargs))
        return func
    return decorator

# Group Exclusion
def grp_exclude():
    def decorator(func):
        async def wrapper(event):
            if event.is_private:
                await func(event)
            else:
                if event.chat_id in os.environ.get('EXCLUDE_CHATS', '').split():
                    LOGS.info(f'Excluded {event.chat_id} from {func.__name__}')
                else:
                    await func(event)
        return wrapper
    return decorator
    