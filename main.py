import os
import sqlite3
try:
    os.remove("StudentsDatabase.db")
except Exception:
    pass
conn = sqlite3.connect("StudentsDatabase.db")
c = conn.cursor()
class claass:
    def __init__(self,classname:str,teacher,studentlist) -> None:
        self.classname:str = classname
        self.teacher:str = teacher
        self.studentlist:list= studentlist.copy()


class student:
    def __init__(self,id:int,name:str,lname:str,major:str,grades:dict, year:int=0) -> None:
        self.id = id
        self.name= name
        self.fname = lname
        self.major = major
        self.year = year
        self.grades = grade_book(grades,major)

    def __str__(self) -> str:
        return (f'Name : {self.name}\nFamily name:{self.fname}\n{self.major}\nID:{self.id:08d}      year:{self.year}')



class grade_book:
    def __init__(self,grades:dict,major) -> None:
        self.grades:dict =grades
        self.modules_number:int = len(grades)


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



