#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", '27610252'))
    API_HASH = os.environ.get("API_HASH", '73e16fc08192ba7c1d52d4dc9fa2b220')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6487620358:AAE4iz1l7VIALr0mUVdMp5GDhlNM5DEqQfM") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "BQGlTIwAAfkuMOzEfm3azK-uhHbYkxCDUDR-XSGxcmfqY51JnVBYdttlTs0ckBabyZXEg4Pdr2nYdiuqcg5t8w-1_d11Vdg1DMFDXYGzI1NmSHuW1b0jZVYyEyFYGPY63Jwijyyr6XcpLHJ5N4KGbrNC2YHEVsf3T-VBNjVy1UMyyu12bj9htsjpXBVO8A_4ybP5sZ5E3-PVcsmOdIyW5d9usT2MvbYNfGNVgvKgjIDBk6U3AHd8gSab7RI_SYmm96SnPjcszfxVcjgOqWIMaFJq7wwmcpZJl69Nhz1Puj3WgEO9SmC3ippI0y1BdvdF3J9GzpN2_wRcpOSbp1_Owct79X6StAAAAAE9EwLhAA") 
    CAPTION = os.environ.get("CAPTION", "@GOOD_NATION")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 5319623393)
    SESSION = os.environ.get("SESSION")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
