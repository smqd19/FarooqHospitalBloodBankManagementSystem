import pandas as pd, tkinter as tk
from tkinter import *
from openpyxl import load_workbook
from tkinter import messagebox
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from datetime import datetime
from openpyxl.workbook import Workbook
from datetime import date

ind = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None,header=None, sheet_name='Indoor',usecols=[0, 1, 2, 3])
op = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None, header=None, sheet_name='OPD',usecols=[0, 1, 2, 3])
panel = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None, header=None, sheet_name='PanelPt',usecols=[0, 1, 2, 3,4,5])
plasma = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None, header=None, sheet_name='PlasmaPt',usecols=[0, 1, 2, 3,4])
mega = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None, header=None, sheet_name='MegaUnit',usecols=[0, 1, 2, 3,4])
cab = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None, header=None, sheet_name='Cabg',usecols=[0, 1, 2, 3,4])
covd = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=None, header=None, sheet_name='Covid',usecols=[0, 1, 2, 3])

def write_excel(filename, sheetname, dataframe):
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
        workBook = writer.book
        try:
            try:
                workBook.remove(workBook[sheetname])
            except:
                print('Worksheet does not exist')

        finally:
            dataframe.to_excel(writer, sheet_name=sheetname, index=False,header=None)
            writer.save()
    
def monthClosed():
    first = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='Indoor')
    second = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='OPD')
    third = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='PanelPt')
    fourth = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='PlasmaPt')
    fifth = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='MegaUnit')
    sixth = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='Cabg')
    seventh = pd.read_excel('Ahsan Blood Bank.xlsx', index_col=0, header=0, sheet_name='Covid')
    today = datetime.today()
    if(today.month==1):
        filename='January Ahsan Blood Bank Report.xlsx'
    if(today.month==2):
        filename='February Ahsan Blood Bank Report.xlsx'
    if(today.month==3):
        filename='March Ahsan Blood Bank Report.xlsx'
    if(today.month==4):
        filename='April Ahsan Blood Bank Report.xlsx'
    if(today.month==5):
        filename='May Ahsan Blood Bank Report.xlsx'
    if(today.month==6):
        filename='June Ahsan Blood Bank Report.xlsx'
    if(today.month==7):
        filename='July Ahsan Blood Bank Report.xlsx'
    if(today.month==8):
        filename='August Ahsan Blood Bank Report.xlsx'
    if(today.month==9):
        filename='September Ahsan Blood Bank Report.xlsx'
    if(today.month==10):
        filename='October Ahsan Blood Bank Report.xlsx'
    if(today.month==11):
        filename='November Ahsan Blood Bank Report.xlsx'
    if(today.month==12):
        filename='December Ahsan Blood Bank Report.xlsx'

    if first['AMOUNT'].empty == False:
        first_total = first['AMOUNT'].sum()
        first.loc[len(first)] = [' ','TOTAL',first_total]
    if second['AMOUNT'].empty == False:
        second_total = second['AMOUNT'].sum()
        second.loc[len(second)] = [' ','TOTAL',second_total]
    if third['AMOUNT'].empty == False:
        third_total = third['AMOUNT'].sum()
        third.loc[len(third)] = [' ',' ',' ','TOTAL',third_total]
    if fourth['AMOUNT'].empty == False:
        fourth_total = fourth['AMOUNT'].sum()
        fourth.loc[len(fourth)] = [' ',' ','TOTAL',fourth_total]
    if fifth['AMOUNT'].empty == False:
        fifth_total = fifth['AMOUNT'].sum()
        fifth.loc[len(second)] = [' ',' ','TOTAL',fifth_total]
    if sixth['AMOUNT'].empty == False:
        sixth_total = sixth['AMOUNT'].sum()
        sixth.loc[len(sixth)] = [' ',' ','TOTAL',sixth_total]
    if seventh['AMOUNT'].empty == False:
        seventh_total = seventh['AMOUNT'].sum()
        seventh.loc[len(seventh)] = [' ','TOTAL',seventh_total]
    with pd.ExcelWriter(filename) as writer:
        first.to_excel(writer, sheet_name='Indoor')
        second.to_excel(writer, sheet_name='OPD')
        third.to_excel(writer, sheet_name='PanelPt')
        fourth.to_excel(writer, sheet_name='PlasmaPt')
        fifth.to_excel(writer, sheet_name='MegaUnit')
        sixth.to_excel(writer, sheet_name='Cabg')
        seventh.to_excel(writer, sheet_name='Covid')
    
    column_names = ['DATE', 'PATIENT NAME', 'MR NUMBER','AMOUNT']
    first = pd.DataFrame(columns = column_names)
    
    column_names = ['DATE', 'PATIENT NAME', 'SLIP NUMBER','AMOUNT']
    second = pd.DataFrame(columns = column_names)
    
    column_names = ['DATE', 'PATIENT NAME', 'MR NUMBER','PRODUCT','COMPANY NAME','AMOUNT']
    third = pd.DataFrame(columns = column_names)
    
    column_names = ['DATE', 'PATIENT NAME','SLIP NUMBER', 'MR NUMBER','AMOUNT']
    fourth = pd.DataFrame(columns = column_names)
    
    column_names = ['DATE', 'PATIENT NAME','SLIP NUMBER', 'MR NUMBER','AMOUNT']
    fifth = pd.DataFrame(columns = column_names)
    
    column_names = ['DATE', 'PATIENT NAME', 'MR NUMBER','PRODUCT','AMOUNT']
    sixth = pd.DataFrame(columns = column_names)
    
    column_names = ['DATE', 'PATIENT NAME', 'SLIP NUMBER','AMOUNT']
    seventh = pd.DataFrame(columns = column_names)
    
    with pd.ExcelWriter('Ahsan Blood Bank.xlsx') as writer:
        first.to_excel(writer, sheet_name='Indoor',index=False)
        second.to_excel(writer, sheet_name='OPD',index=False)
        third.to_excel(writer, sheet_name='PanelPt',index=False)
        fourth.to_excel(writer, sheet_name='PlasmaPt',index=False)
        fifth.to_excel(writer, sheet_name='MegaUnit',index=False)
        sixth.to_excel(writer, sheet_name='Cabg',index=False)
        seventh.to_excel(writer, sheet_name='Covid',index=False)
    messagebox.showinfo('Data Saved', 'Calculations Added to File')

class Indoor(Toplevel):
    def indoor(self,date, ptname, mr, amount):
        global ind
        date = date
        ptname = ptname
        mr = mr
        amount = int(amount)
        ind.loc[len(ind)] = [date,ptname,mr,amount]
        text = 'Indoor'
        write_excel('Ahsan Blood Bank.xlsx', text, ind)
        messagebox.showinfo('Data Saved', 'Calculations Added to File')
        self.destroy()

    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('INDOOR PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='MR Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        self.e1.focus_set()
        l4 = Label(self, text='Amount')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.indoor(str(today), self.e1.get(), self.e2.get(),self.e3.get()))
        self.b.pack(side='bottom', pady=10)
        self.mainloop()
        
class OPD(Toplevel):
    
    def opd(self,date, ptname, slip, amount):
        global op
        date = date
        ptname = ptname
        slip = slip
        amount = int(amount)
        op.loc[len(op)] = [date,ptname,slip,amount]
        text = 'OPD'
        write_excel('Ahsan Blood Bank.xlsx', text, op)
        messagebox.showinfo('Data Saved', 'Calculations Added to File')
        self.destroy()
    
    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('OPD PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='Slip Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        l4 = Label(self, text='Amount')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.opd(str(today), self.e1.get(), self.e2.get(),self.e3.get()))
        self.b.pack(side='bottom', pady=10)
        self.mainloop()

class PanelPt(Toplevel):

    def panelpt(self,date, ptname, mr,prod,comp,amount):
        global panel  
        date = date
        ptname = ptname
        mr = mr
        prod = prod
        comp = comp
        amount = int(amount)
        panel.loc[len(panel)] = [date,ptname,mr,prod,comp,amount]
        text = 'PanelPt'
        write_excel('Ahsan Blood Bank.xlsx', text, panel)
        messagebox.showinfo('Data Saved', 'Calculations Added to File')
        self.destroy()

    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('PANEL PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='MR Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        l4 = Label(self, text='Product')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        l5 = Label(self, text='Company Name')
        l5.pack()
        self.e4 = Entry(self)
        self.e4.pack()
        self.e4.focus_set()
        l6 = Label(self, text='Amount')
        l6.pack()
        self.e5 = Entry(self)
        self.e5.pack()
        self.e5.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.panelpt(str(today), self.e1.get(), self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get()))
        self.b.pack(side='bottom', pady=10)
        self.mainloop()        

class PlasmaPt(Toplevel):
    
    def plasmapt(self,date, ptname,slip, mr, amount):
        global plasma
        date = date
        ptname = ptname
        slip = slip
        mr = mr
        amount = int(amount)
        plasma.loc[len(plasma)] = [date,ptname,slip,mr,amount]
        text = 'PlasmaPt'
        write_excel('Ahsan Blood Bank.xlsx', text, plasma)
        messagebox.showinfo('Data Saved', 'Calculations Added to File')
        self.destroy()
    
    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('PLASMA APHRASIS PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='Slip Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        l4 = Label(self, text='MR Number')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        l5 = Label(self, text='Amount')
        l5.pack()
        self.e4 = Entry(self)
        self.e4.pack()
        self.e4.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.plasmapt(str(today), self.e1.get(), self.e2.get(),self.e3.get(),self.e4.get()))
        self.b.pack(side='bottom', pady=10)
        self.mainloop()
        
class MegaUnit(Toplevel):

    def megaunit(self,date, ptname,slip, mr, amount):
        global mega
        date = date
        ptname = ptname
        slip = slip
        mr = mr
        amount = int(amount)
        mega.loc[len(mega)] = [date,ptname,slip,mr,amount]
        text = 'MegaUnit'
        write_excel('Ahsan Blood Bank.xlsx', text, mega)
        messagebox.showinfo('Data Saved', 'Calculations Added to File')
        self.destroy()
    
    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('MEGAUNIT PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='Slip Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        l4 = Label(self, text='MR Number')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        l5 = Label(self, text='Amount')
        l5.pack()
        self.e4 = Entry(self)
        self.e4.pack()
        self.e4.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.megaunit(str(today), self.e1.get(), self.e2.get(),self.e3.get(),self.e4.get()))
        self.b.pack(side='bottom', pady=10)
        self.mainloop()

class Cabg(Toplevel):

    def cabg(self,date, ptname, mr,prod, amount):
        global cab
        date = date
        ptname = ptname
        prod = prod
        mr = mr
        amount = int(amount)
        cab.loc[len(cab)] = [date,ptname,mr,prod,amount]
        text = 'Cabg'
        write_excel('Ahsan Blood Bank.xlsx', text, cab)
        messagebox.showinfo('Data Saved', 'Calculations Added to File') 
        self.destroy()

    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('CABG PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='MR Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        l4 = Label(self, text='Product')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        l5 = Label(self, text='Amount')
        l5.pack()
        self.e4 = Entry(self)
        self.e4.pack()
        self.e4.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.cabg(str(today), self.e1.get(), self.e2.get(),self.e3.get(),self.e4.get()))
        self.b.pack(side='bottom', pady=10)
        self.mainloop()
        
class Covid(Toplevel):
    def covid(self,date, ptname, slip, amount):
        global covd
        date = date
        ptname = ptname
        slip = slip
        amount = int(amount)
        covd.loc[len(covd)] = [date,ptname,slip,amount]
        text = 'Covid'
        write_excel('Ahsan Blood Bank.xlsx', text, covd)
        messagebox.showinfo('Data Saved', 'Calculations Added to File')
        self.destroy()
        
    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('Author.jpeg')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l11 = Label(self, text='')
        l11.pack()
        l12 = Label(self, text='')
        l12.pack()
        l16 = Label(self, text='')
        l16.pack()
        l17 = Label(self, text='')
        l17.pack()
        l1 = Label(self, text='Date')
        l1.pack()
        self.title('COVID PLASMA PATIENTS')
        self.geometry('500x500')
        self.e = Entry(self)
        self.e.pack()
        self.e.focus_set()
        today = date.today()
        self.e.focus_set()
        self.e.insert('end', str(today))
        
        l2 = Label(self, text='Patient Name')
        l2.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.e1.focus_set()
        l3 = Label(self, text='Slip Number')
        l3.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        self.e2.focus_set()
        self.e1.focus_set()
        l4 = Label(self, text='Amount')
        l4.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        self.e3.focus_set()
        self.b = Button(self, text='Save')
        self.b.bind('<Button>', lambda e: self.covid(str(today), self.e1.get(), self.e2.get(),self.e3.get()))
        self.b.pack(side='bottom', pady=10)

        self.mainloop()
        
class MonthClosed(Toplevel):

    def __init__(self, master, text):
        super().__init__(master=master)
        load = Image.open('last.jpeg')
        self.geometry('793x694')
        bg = ImageTk.PhotoImage(load)
        background_label = Label(self, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        monthClosed()
        self.mainloop()

root = tk.Tk()
root.title('Farooq Hospital Management System')
root.geometry('550x550')
load = Image.open('BackgroundFarooq.jpg')
bg = ImageTk.PhotoImage(load)
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
l11 = Label(root)
l11.pack(pady=40)
indoo = Button(root, text='Indoor Patients', padx=10)
indoo.bind('<Button>', lambda e: Indoor(root, 'Indoor'))
indoo.pack(pady=10)
care = Button(root, text='OPD Patients', padx=10)
care.bind('<Button>', lambda e: OPD(root, 'Outdoor'))
care.pack(pady=10)
sky = Button(root, text='Panel Patients', padx=10)
sky.bind('<Button>', lambda e: PanelPt(root, 'Panel'))
sky.pack(pady=10)
skyservice = Button(root, text='Plasma Aphrasis Patients', padx=10)
skyservice.bind('<Button>', lambda e: PlasmaPt(root, 'Plasma'))
skyservice.pack(pady=10)
verizon = Button(root, text='Mega Unit Patients', padx=10)
verizon.bind('<Button>', lambda e: MegaUnit(root, 'Platelets'))
verizon.pack(pady=10)
LM = Button(root, text='Cabg Patients', padx=10)
LM.bind('<Button>', lambda e: Cabg(root, 'Cabg'))
LM.pack(pady=10)
LMM = Button(root, text='Covid Plasma Patients', padx=10)
LMM.bind('<Button>', lambda e: Covid(root, 'Covid'))
LMM.pack(pady=10)
LMMM = Button(root, text='Month Closed', padx=10)
LMMM.bind('<Button>', lambda e: MonthClosed(root, 'Closing'))
LMMM.pack(pady=20)
root.mainloop()