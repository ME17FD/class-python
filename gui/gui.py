import tkinter as tk
from tkinter import ttk
import os
if __name__!='__main__':
    from utilties.structures import student
else:
    from structures import student
 
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"] 
MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED] 
 
class ListApp(tk.Tk): 
    def __init__(self,liste:student): 
        super().__init__()
        self.set_menu()
        self.set_page("1280x720")
        page = ttk.Treeview(self,selectmode=tk.BROWSE)
        scrollbary = tk.Scrollbar(self,orient="vertical")
        self.put_tree(page,scrollbary)
        
        self.fill_list_stdnts(page,liste)
        
        butt1 = self.create_btn('mult',self.print_selection,page)
        butt1.pack(anchor=tk.W)
        
    def create_btn(self, text,func,page): 
        return tk.Button(self, command=lambda:func(page),
                         text=text,width=20,height=5) 
 
    def print_selection(self,page): 
        selection = page.selection()
        for i in list(selection):
            try:
                i = int(i)
            except:
                continue 
            print(page.item(i))


    def set_page(self,resolution):
        self.title("School DataBase")
        self.geometry(resolution)
        self.config(bg="lightgrey")


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
        helpmenu.add_command(label='About')


    def set_list(self,liste):
        self.list = tk.Listbox(self,height=40)
        self.list.insert(0, *liste) 
        self.print_btn = tk.Button(self ,text="Print selection", 
                                   command=self.print_selection) 
        self.btns = [self.create_btn(m) for m in MODES] 
        self.list.pack(side="right")
        self.print_btn.pack() 
        for btn in self.btns: 
            btn.pack(side=tk.LEFT)


    def put_tree(self,page,scrollbary):
        page.place(relx=.2,rely=.028,width= int(1280*.8),height=int(720*.972))
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
        
        scrollbary.place(relx=.985,rely=.05,width= int(1280*.82),height=int(720*.98))
        page.configure(yscrollcommand=scrollbary.set)
        page.configure(selectmode="extended")

        scrollbary.configure(command=page.yview)



    def fill_list_stdnts(self,page,studliste:student):
        stndt:student
        for stndt in studliste:
            page.insert('','end',text=f"{(stndt.id):04d}",iid=stndt.id,values=(stndt.name,stndt.lname,stndt.major,stndt.year))
            for i in stndt.grades.grades:
                page.insert(stndt.id,'end',text=f"{(stndt.id):04d}",values=(i,stndt.grades.grades[i],None,None))



if __name__ == "__main__": 
    os.system('cmd /c "py main.py"')
