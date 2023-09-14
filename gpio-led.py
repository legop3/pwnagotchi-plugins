from threading import Event
import _thread
import logging
import time

import pwnagotchi.plugins as plugins

class GpioLed(plugins.Plugin):
    __author__='legop3'
    __version__='1.0.0'
    __license__='GPL3'
    __description__='allows you to set a GPIO pin to blink for certain events'

    def __init__(self):
        self.running = False

    def on_loaded(self):
        logging.info("gpio-led plugin loaded")
    
    def on_ready(self):
        logging.info("gpio-led plugin ready")
