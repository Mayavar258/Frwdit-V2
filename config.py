#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", '1522127'))
    API_HASH = os.environ.get("API_HASH", '1252ffe16baf341bfd7236f92df76b0e')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6971823310:AAE_QcYgfRlCIQsuR-zuIqhvnoyAzf35b4g") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "AQAXOc8APTglOd8gyen6KjU4VTT4FkxHD5RLgRA9Bh4y_K0GFB1Fs_bHy0pzRCtAixFG2EpQeMYGqSUHyYZ5MzWZep6niKWHkJt-qjSQMuYJOOIO4ncjj7EpxihRUWiZGb0j_sBuwHcnPKs_c25L78wAw84TS-FYvJt513BIBdDQWJt2EUysznHY_TvjffMDjaPJ8wJukNVOFyxsotMJiI1lLD2B1e7m6dehJFiGEhbj1qQclWTJMof5MH-TzEhoPSWGplEnKRtW-iMKDUJ5QjheMuLQD2cb_3hDtF9n6UC-ggxv-JFoZiT96xHQHGStmQkZ177wQmeFzNcfCmkacKA-YsFAXgAAAAA7-MTRAA") 
    CAPTION = os.environ.get("CAPTION", "@GOOD_NATION")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 1006159057)
    SESSION = os.environ.get("SESSION")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
