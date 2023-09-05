import os
import sqlite3
from utilties.structures import *
from utilties.logging import *
from gui.gui import *


path_db = "db\\StudentsDatabase11.db"
conn = sqlite3.connect(path_db)
c = conn.cursor()
from utilties.data_filler import *
studentlst:student = []


setup()

if  os.stat(path_db).st_size != 0:
    database2py(c,studentlst)
    log("loading database")
else:
    log("database not found creating new one")
    create_tables(c)
    fill_random_data(c,conn,studentlst,50,0)

#show_student_lst(studentlst)
#main loop
try:
    app = ListApp(studentlst) 
    sapp = AddStudentPage(c,conn,studentlst)
    sapp.mainloop()

finally:
    log("program closed")
    conn.commit()
    os.system('cmd /c "cls"')