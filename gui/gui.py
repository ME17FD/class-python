import tkinter as tk
from tkinter import ttk
import os
import time
if __name__!='__main__':
    from utilties.structures import student
    from utilties.data_filler import add2list, updatepy,remove
else:
    from structures import student
 

x = 1280
y=720
class BackBone(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.background = "lightgrey"
        self.set_menu()
        self.set_page(str(x)+'x'+str(y))
        self.resizable(1,1)
        for i in range(8):
            self.columnconfigure(i,weight=1)
        
        for i in range(8):
            self.rowconfigure(i, weight=1)

    def set_page(self,resolution):
        self.title("School DataBase")
        self.geometry(resolution)
        self.config(bg= self.background)


    def set_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.quit)
        helpmenu = tk.Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='No help just pray it works')

    def create_btn(self, text,func,page): 
        return tk.Button(self, command=lambda:func(page),
                         text=text,width=20,height=5) 
 
    def print_selection(self,page): 
        selection = page.selection()
        for i in list(selection):
            print(page.item(i))


class ListApp(BackBone): 
    def __init__(self,liste:student,c,conn): 
        super().__init__()
        
        page = ttk.Treeview(self,selectmode=tk.BROWSE)
        scrollbary = tk.Scrollbar(self,orient="vertical")
        self.put_tree(page,scrollbary)
        
        self.fill_list_stdnts(page,liste)
        
        butt1 = self.create_btn('print selection',self.print_selection,page)
        butt1.grid(column = 0, row = 0)


        butt2 = tk.Button(self, command=lambda:self.go_to_add_std(page,liste,c),
                         text="Add Student",width=20,height=5) 
        butt2.grid(column = 0, row = 1)
        

        butt3 = tk.Button(self, command=lambda:self.remove_std(page,c,conn,liste),
                         text="Remove Student",width=20,height=5) 
        butt3.grid(column = 0, row = 2)


    def put_tree(self,page,scrollbary):
        page.grid(column = 1,columnspan = 7,row=0,rowspan=8,sticky = "NSEW")
        page.configure(selectmode='extended')
        page.configure(columns=("Name","Last Name","Major","Year"))
        page.heading("#0",text="ID",anchor="w")
        page.heading("Name",text="Name",anchor="w")
        page.heading("Last Name",text="Last Name",anchor="w")
        page.heading("Major",text="Major",anchor="w")
        page.heading("Year",text="Year",anchor="w")

        page.column('#0',stretch=tk.YES,width=50)
        page.column('#1',stretch=tk.YES)
        page.column('#2',stretch=tk.YES)
        page.column('#3',stretch=tk.YES)
        page.column('#4',stretch=tk.YES)
        
        scrollbary.grid(row=0, column=8,rowspan=8, sticky='ns')
        page.configure(yscrollcommand=scrollbary.set)
        page.configure(selectmode="extended")

        scrollbary.configure(command=page.yview)



    def fill_list_stdnts(self,page,studliste:student):
        stndt:student
        for stndt in studliste:
            page.insert('','end',text=f"{(stndt.id):04d}",iid=stndt.id,values=(stndt.name,stndt.lname,stndt.major,stndt.year))
            for i in stndt.grades.grades:
                page.insert(stndt.id,'end',text=f"{(stndt.id):04d}",values=(i,stndt.grades.grades[i],None,None))
    
    def go_to_add_std(self,page,studliste,c):
        
        os.system("cmd /c py add_stdnt.py")

        updatepy(c,studliste)
        
        for stndt in studliste:
            try:
                page.insert('','end',text=f"{(stndt.id):04d}",iid=stndt.id,values=(stndt.name,stndt.lname,stndt.major,stndt.year))
                for i in stndt.grades.grades:
                    page.insert(stndt.id,'end',text=f"{(stndt.id):04d}",values=(i,stndt.grades.grades[i],None,None))
                print("done")
            except Exception:
                pass
            

    def remove_std(self,page,c,conn,studntlst):
        selection = page.selection()
        for selected_item in list(selection):
            
                id = int(page.item(selected_item)['text'])
                print(str(id)+' deleted')
                remove(c,conn,studntlst,id)
                page.delete(selected_item)
            

class AddStudentPage(BackBone):
    def __init__(self,c,conn,studentlist):
        super().__init__()
        self.c =c
        
        self.conn = conn
        


        name = ttk.Label(self,text="Name",background=self.background)
        name.grid(column=2,row=1,sticky=tk.W)
        name_entry = ttk.Entry(self)
        name_entry.grid(column=3,row=1,sticky=tk.EW)


        last_name = ttk.Label(self,text="Last Name",background=self.background)
        last_name.grid(column=4,row=1,sticky=tk.W)
        last_name_entry = ttk.Entry(self)
        last_name_entry.grid(column=5,row=1,sticky=tk.EW)


        major = ttk.Label(self,text="Major",background=self.background)
        major.grid(column=2,row=2,sticky=tk.W)
        major_entry = ttk.Entry(self)
        major_entry.grid(column=3,row=2,sticky=tk.EW)
        
        year = ttk.Label(self,text="Year",background=self.background)
        year.grid(column=2,row=3,sticky=tk.W)
        year_entry = ttk.Entry(self)
        year_entry.grid(column=3,row=3,sticky=tk.EW)




        newid = ttk.Label(self,text="New ID : ",background=self.background)
        newid.grid(column=4,row=2,sticky=tk.W)
        newidlabel = ttk.Label(self,text="")
        newidlabel.grid(column=5,row=2,sticky=tk.W)


        addStud = ttk.Button(self,text='Add Student', command= lambda :
                                self.add_stud(studentlist, name_entry.get(),last_name_entry.get(),major_entry.get(),year_entry.get(),newidlabel))
        
        addStud.grid(column=2,columnspan=2,row=3,rowspan=2,sticky=tk.EW)

    
    
    def add_stud(self,studentlist,name_entry,last_name_entry,major_entry,year,newidlabel):
        
        newID = studentlist[-1].id +1
        add2list(self.c,studentlist, newID ,name_entry,last_name_entry,major_entry,{},year)
        newidlabel.config(text=newID)
        self.conn.commit()
        





if __name__ == "__main__":
    os.system('cmd /c "py main.py"')
