#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", '1522127'))
    API_HASH = os.environ.get("API_HASH", '1252ffe16baf341bfd7236f92df76b0e')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6971823310:AAE_QcYgfRlCIQsuR-zuIqhvnoyAzf35b4g") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 1006159057)
    SESSION = os.environ.get("SESSION")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
