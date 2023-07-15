import tkinter as tk
from tkinter import ttk
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
        self.geometry("1280x720")
        self.maxsize(1280,720)
        self.config(bg="lightgrey")
        page = ttk.Treeview(self)
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
        scrollbary = tk.Scrollbar(self,orient="vertical")
        scrollbary.place(relx=.985,rely=.05,width= int(1280*.82),height=int(720*.98))
        page.configure(yscrollcommand=scrollbary.set)
        page.configure(selectmode="extended")

        scrollbary.configure(command=page.yview)

        self.fill_list_stdnts(page,liste)

        butt1 = self.create_btn('mult')
        butt1.pack(anchor=tk.W)
        butt2 = self.create_btn('2222')
        butt2.pack(anchor=tk.W)
        
    def create_btn(self, mode): 
        cmd = lambda: self.list.config(selectmode=mode) 
        return tk.Button(self, command=cmd,
                         text=mode.capitalize()) 
 
    def print_selection(self): 
        selection = self.list.curselection() 
        print(*[self.list.get(i) for i in selection]) 
    
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

    def fill_list_stdnts(self,page,studliste:student):
        stndt:student
        for stndt in studliste:
            page.insert('','end',text=f"{(stndt.id):04d}",iid=stndt.id,values=(stndt.name,stndt.lname,stndt.major,stndt.year))
            for i in stndt.grades.grades:
                page.insert(stndt.id,'end',text=f"{(stndt.id):04d}",values=(i,stndt.grades.grades[i],None,None))
                
if __name__ == "__main__": 
    app = ListApp(DAYS) 
    app.mainloop() 