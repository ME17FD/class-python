from random import randint, choice
from utilties.structures import student,grade_book
from utilties.randomdata import firstnames,lastnames,majors
import os



def add2list(c,studentlist:list,id:int,name:str,lname:str,major:str,grades:dict, year:int):
    c.execute('INSERT INTO Students VALUES (?,?,?,?,?)',(id,name,lname,major,year))
    studentlist.append(student(id,name,lname,major,grades, year))
    for k in grades:
        c.execute('INSERT INTO Grades VALUES (?,?,?)',(k,grades[k],id))


def fill_random_data(c,conn,studentlist,n,idcounter) -> int:
    n += idcounter
    while (idcounter<n):
        studYear = randint(1,3)
        dd = {}
        for i in range(studYear*12):
            dd[f'course {i}'] = randint(10,20)
        
        add2list(c,studentlist,idcounter,choice(firstnames),choice(lastnames),choice(majors),dd.copy(),studYear)
        dd.clear()
        idcounter+=1
        print(idcounter)
    conn.commit()
    return idcounter


def remove(c,conn,studentlist:list,id) -> int:
    try:
        c.execute("DELETE FROM Students WHERE id=?;",(id,))
        c.execute("DELETE FROM Grades WHERE studentid=?;",(id,))
        for stud in studentlist:
            if stud.id == id:
                studentlist.remove(stud)
        return 1
    except Exception:
        print(Exception)
        return 0
    conn.commit()

def database2py(c,studentlist:list):
    c.execute("SELECT * FROM Students")
    studs = c.fetchall().copy()
    dd:dict = {}
    for id,n,l,m,y in studs:
        c.execute("SELECT * FROM Grades where studentid=?",(id,))
        table = c.fetchall()
        for mdl,g,i in table:
            dd[mdl] = g
        studentlist.append(student(id,n,l,m,dd.copy(),y))
        dd.clear()
    studs.clear()

def updatepy(c,studentlist:list):
    studentlist.clear()
    c.execute("SELECT * FROM Students")
    studs = c.fetchall().copy()
    dd:dict = {}
    for id,n,l,m,y in studs:
        c.execute("SELECT * FROM Grades where studentid=?",(id,))
        table = c.fetchall()
        for mdl,g,i in table:
            dd[mdl] = g
        studentlist.append(student(id,n,l,m,dd.copy(),y))
        dd.clear()
    studs.clear()



def create_tables(c):
    c.execute("""CREATE TABLE IF NOT EXISTS Students(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            lname TEXT NOT NULL,
            major TEXT NOT NULL,
            year INTEGER DEFAULT 0 NOT NULL);""")


    c.execute("""CREATE TABLE IF NOT EXISTS GRADES(
            module TEXT NOT NULL,
            grd INTEGER DEFAULT NULL,
            studentid INTEGER NOT NULL,
            FOREIGN KEY(studentid) REFERENCES Students(id)
            );""")
    
def show_student_lst(studentlst:list):
    for i in studentlst:
        print(i)


if __name__ == "__main__":
    os.system('cmd /c "py main.py"')