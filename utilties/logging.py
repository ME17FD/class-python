import logging
import datetime as dt
import os

bo = False

def setup():
    if bo:    
        logging.basicConfig(filename="log.txt",level=logging.DEBUG)
        logging.debug(f'************PROGRAM STARTED : {dt.datetime.now()::%d-%m-%Y %H:%M:%S}************')


def log(msg:str):
        if bo:    
            logging.debug(f'{msg} {dt.datetime.now()::%d-%m-%Y %H:%M:%S}')

def remove_logs():
    logging.shutdown()
    os.remove("log.txt")
