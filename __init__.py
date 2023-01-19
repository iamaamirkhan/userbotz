import logging
from datetime import datetime
from pathlib import Path
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from config import *
def create_session(api_id, api_hash, phone):
    """Create a new session or load an existing one"""
    session_name = str(phone)
    session = Path(session_name)
    if not session.is_file():
        client = TelegramClient(session_name, api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            print('Creating a new session')
            print("First run. Sending code request...")
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter the code: '))
    else:
        print("Session file already exists! Attempting to load it...")
        client = TelegramClient(session_name, api_id, api_hash)
        client.connect()
    return client

app = create_session(api_id, api_hash, phone)