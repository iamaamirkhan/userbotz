from __init__ import app
from telethon import events
from loguru import logger
import os
import importlib.util
import sys


# log plugins
logger.info('Loading Plugins...')
for plugin in os.listdir('plugins'):
    if plugin.endswith('.py'):
        logger.info(f'Loading {plugin}...')
        spec = importlib.util.spec_from_file_location(plugin, f'plugins/{plugin}')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        logger.info(f'Loaded {plugin}...')

if __name__ == '__main__':
    try:
        logger.info('Starting Bot...')
        app.run_until_disconnected()
    except KeyboardInterrupt:
        logger.info('Exiting...')
        sys.exit(0)
    