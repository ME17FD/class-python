import logging
import datetime as dt
import os

def setup():
    logging.basicConfig(filename="log.txt",level=logging.DEBUG)
    logging.debug(f'************PROGRAM STARTED : {dt.datetime.now()::%d-%m-%Y %H:%M:%S}************')


def log(msg:str):
        logging.debug(f'{msg} {dt.datetime.now()::%d-%m-%Y %H:%M:%S}')

def remove_logs():
    logging.shutdown()
    os.remove("log.txt")
