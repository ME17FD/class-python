import os
import sqlite3
from utilties.structures import *
from utilties.logging import *
from gui.gui import *


path_db = "db\\StudentsDatabase.db"
conn = sqlite3.connect(path_db)
c = conn.cursor()
from utilties.data_filler import *
studentlst:student = []


setup()

if os.path.isfile(path_db):
    database2py(c,studentlst)
    log("loading database")
else:
    log("database not found creating new one")
    create_tables(c)

names = [studentlst[m].name for m in range(len(studentlst))]
print(*names)

app = ListApp(studentlst) 
app.mainloop()