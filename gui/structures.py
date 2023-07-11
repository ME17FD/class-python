class student:
    def __init__(self,id:int,name:str,lname:str,major:str,grades:dict, year:int=0) -> None:
        self.id = id
        self.name= name
        self.lnamename = lname
        self.major = major
        self.year = year
        self.grades = grade_book(grades,major)

    def __str__(self) -> str:
        return (f'Name : {self.name}\nFamily name:{self.fname}\n{self.major}\nID:{self.id:08d}      year:{self.year}')



class grade_book:
    def __init__(self,grades:dict,major) -> None:
        self.grades:dict =grades
        self.modules_number:int = len(grades)

