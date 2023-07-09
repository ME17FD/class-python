from random import randint, choice
from randomdata import firstnames,lastnames,majors


def add2list(id:int,name:str,lname:str,major:str,grades:dict, year:int):
    global c,studentlist
    c.execute('INSERT INTO Students VALUES (?,?,?,?,?)',(id,name,lname,major,year))
    studentlist.append(student(id,name,lname,major,grades, year))
    for k in grades:
        c.execute('INSERT INTO Grades VALUES (?,?,?)',(k,grades[k],id))

idcounter = 0 

def fill_random_data(n):
    
    global idcounter,conn
    while (idcounter<n):
        dd = {
            
            'course a': randint(10,20),
            'course b': randint(10,20),
            'course c': randint(10,20),
            'course d': randint(10,20),
            'course e': randint(10,20),
            'course f': randint(10,20)
        }
        add2list(idcounter,choice(firstnames),choice(lastnames),choice(majors),dd,randint(0,4))
        idcounter+=1
        print(idcounter)
    conn.commit()


def remove(id) -> int:
    try:
        c.execute("DELETE FROM Students WHERE id=?;",(id,))
        for stud in studentlist:
            if stud.id == id:
                studentlist.remove(stud)
        return 1
    except Exception:
        print(Exception)
        return 0

def database2py():
    pass
