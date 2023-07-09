import os
import sqlite3
from utilties.structures import *
conn = sqlite3.connect("db\\StudentsDatabase.db")
c = conn.cursor()
from utilties.data_filler import *
studentlst = []
create_tables(c)
fill_random_data(c,conn,studentlst,300,0)

#database2py(c,studentlst)

#for i in studentlst:
#    print(i)