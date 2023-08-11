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

#show_student_lst(studentlst)
#main loop
try:
    app = ListApp(studentlst) 
    
    app.mainloop()
finally:
    log("program closed")
    os.system('cmd /c "cls"')