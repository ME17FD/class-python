import os
import sqlite3
from utilties.structures import *
from utilties.logging import *
conn = sqlite3.connect("db\\StudentsDatabase.db")
c = conn.cursor()
from utilties.data_filler import *
studentlst = []


setup()

if os.path.isfile("db\\StudentsDatabase.db"):
    database2py(c,studentlst)
    log("loading database")

