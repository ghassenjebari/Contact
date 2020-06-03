from tkinter import *
from tkinter import ttk
import tkinter as ttk

PhoneNumber=0
Name=''
Count=0
CountN=0



def reset():
    global Name,PhoneNumber,NameEntry,PhoneNumberEntry,Count,CountN
    PhoneNumber=0
    Name=''
    Count=0
    CountN=0
    root.focus()

    PhoneNumberEntry.config(foreground='#edebe4')
    PhoneNumberEntry.delete(0,ttk.END)
    PhoneNumberEntry.insert(0,' ex :  28168997')

    NameEntry.delete(0,ttk.END)
    NameEntry.config(foreground='#edebe4')
    NameEntry.insert(0,' Name ex : Ghassen')


def Check(Name):
    global NameEntry,CountN
    name=''
    root.focus()
    for c in Name:
        if c.isalpha() or c==" ":
            name=name+c
    if Name !=name:
        NameEntry.config( fg="red")
        CountN=2

    #if len(Name)==0:
        #NameEntry.config(insertbackground='red')
    return Name==name and len(Name)>0


def CheckExistance(ch):
    f=open("data.txt","r")
    Test=True
    while True:
        s=f.readline()
        if s!='':
            if ch == s :
             Test=False

        else:
            break;
    f.close()

    return Test




def AddContact():
    global PhoneNumberEntry,NameEntry,PhoneNumber,Name,PhoneLabel
    Data=open("data.txt","a")
    Name=NameEntry.get()
    try:
        PhoneNumber=int(PhoneNumberEntry.get())
    except ValueError:
        PhoneNumber=0
    root.focus()
    if(PhoneNumber != 0 and Check(Name) and CheckExistance(Name+","+str(PhoneNumber)+'\n')):
        Data.write(Name+","+str(PhoneNumber)+'\n')
        reset()
        root.focus()
        PhoneLabel=Label(root,text="The contact has been added successfully. ",font=('futurist-fixed-width', 10),fg='green',relief='flat',bg='white')
        PhoneLabel.grid(column=1,row=6,padx=0,pady=5,columnspan=3)
    else:
        PhoneLabel=Label(root,text="The contact can not be added.",font=('futurist-fixed-width', 10),fg='red',relief='flat',bg='white')
        PhoneLabel.grid(column=1,row=6,padx=0,pady=5,columnspan=3)



    Data.close()






def WriteMsg(event):
    global  PhoneNumberEntry,Count,KeyFrame,PhoneNumber
    try:
        PhoneNumber=int(PhoneNumberEntry.get())
    except ValueError:
        PhoneNumber=0
    if PhoneNumber==0:
        PhoneNumberEntry.config(foreground='#edebe4')
        PhoneNumberEntry.delete(0,ttk.END)
        PhoneNumberEntry.insert(0,' ex :  28168997')
        Count=0
    root.geometry("380x300")

    KeyFrame.grid_forget()



def WriteMSg(event):
    global NameEntry,PhoneNumber,CountN,Name
    if NameEntry.get()=='':
        NameEntry.config(foreground='#edebe4')
        NameEntry.insert(0,' Name ex : Ghassen')
        CountN=0
    Name=NameEntry.get()


def DeleteMsg(event):
    global PhoneNumberEntry,LabelEntry,PhoneLabel
    try:
        PhoneLabel.grid_forget()
    except NameError:
        NONE

    global Count
    if Count==0:
        PhoneNumberEntry.config(foreground='#343634')
        PhoneNumberEntry.delete(0,ttk.END)
        Count=1
    root.geometry("380x640")
    DrawKeyboard()


def DeleteMSg(event):
    global NameEntry
    global CountN

    try:
        PhoneLabel.grid_forget()
    except NameError:
        NONE

    if NameEntry.get()==' Name ex : Ghassen':
        NameEntry.config(foreground='#343634')
        NameEntry.delete(0,ttk.END)

def ReadKey(Digit):
    global PhoneNumber,PhoneNumberEntry,Count
    try:
        PhoneNumber=int(PhoneNumberEntry.get())
    except ValueError:
        PhoneNumber=0
    PhoneNumber=PhoneNumber*10+Digit
    Count=1
    PhoneNumberEntry.delete(0,ttk.END)
    PhoneNumberEntry.focus()
    PhoneNumberEntry.insert(0,PhoneNumber)
    PhoneNumberEntry.config(foreground='#343634')


def DeleteLastDigit():
    global PhoneNumber,PhoneNumberEntry
    try :
        PhoneNumber=int(PhoneNumberEntry.get())
    except ValueError:
        PhoneNumber=0
    PhoneNumber=PhoneNumber//10
    PhoneNumberEntry.delete(0,ttk.END)
    PhoneNumberEntry.focus()
    if PhoneNumber!=0:
        PhoneNumberEntry.insert(0,PhoneNumber)
    print(PhoneNumber)


def DrawKeyboard():
    global NumberButton,ResetImage
    global KeyFrame

    KeyFrame=Frame(root)
    KeyFrame.configure(bg="white")

    KeyFrame.grid(column=1,row=6,padx=5,pady=5,columnspan=3)
    x=10
    for i in range(1,4):
        for j in range(4,1,-1):
            x=x-1
            button=Button(KeyFrame,image=NumberButton,text=x,compound=ttk.CENTER,font=('futurist-fixed-width', 20),fg='white',relief='flat',bg='white',borderwidth='0',command=lambda x=x:ReadKey(x))
            button.grid(column=j,row=i,padx=5,pady=5)
    button=Button(KeyFrame,image=NumberButton,text='0',compound=ttk.CENTER,font=('futurist-fixed-width', 20),fg='white',relief='flat',bg='white',borderwidth='0',command=lambda :ReadKey(0))
    button.grid(column=3,row=4,padx=0,pady=5)

    button=Button(KeyFrame,image=Delete,relief='flat',bg='white',borderwidth='0',command=lambda :DeleteLastDigit())
    button.grid(column=4,row=4)
    button=Button(KeyFrame,image=NumberButton,text='X',compound=ttk.CENTER,font=('futurist-fixed-width', 20),fg='white',relief='flat',bg='white',borderwidth='0',command=lambda :reset())
    button.grid(column=2,row=4,padx=0,pady=5)



def DrawAddContactFrame():
    global PhoneNumberEntry,NameEntry,ConfirmImage,CancelImage,HeaderImage

    for widget in root.winfo_children():
        widget.grid_forget()
    root.geometry("380x300")

    CancelButton=Button(root,image=CancelImage,relief='flat',borderwidth=-4,height=69,command= lambda : DrawMainFrame())
    CancelButton.grid(column=1,row=1,padx=0,pady=0)

    HeaderCanvas=Canvas(root,width=237,height=75,borderwidth=-4,bg='white',relief='flat')
    HeaderCanvas.create_image(0,0, anchor=NW, image=HeaderImage)
    HeaderCanvas.grid(column=2,row=1,padx=0,pady=0)

    Confirm=Button(root,image=ConfirmImage,command=lambda:AddContact(),relief='flat',borderwidth=-4,height=69)
    Confirm.grid(column=3,row=1,padx=0,pady=0)

    NameLabel=Label(root,text=" Contact Name :",font=('futurist-fixed-width', 20),fg='blue',relief='flat',bg='white')
    NameLabel.grid(column=1,row=2,padx=0,pady=5,columnspan=2)

    NameEntry=Entry(root,font=('futurist-fixed-width', 20),width=18,foreground='#edebe4',relief="solid")
    NameEntry.insert(0,' Name ex : Ghassen')
    NameEntry.bind('<FocusIn>',DeleteMSg)
    NameEntry.bind('<FocusOut>',WriteMSg)
    NameEntry.grid(column=1,row=3,padx=0,pady=5,columnspan=3)

    PhoneLabel=Label(root,text=" Phone Number :",font=('futurist-fixed-width', 20),fg='blue',relief='flat',bg='white')
    PhoneLabel.grid(column=1,row=4,padx=0,pady=5,columnspan=2)

    PhoneNumberEntry=Entry(root,font=('futurist-fixed-width', 20),width=18,foreground='#edebe4',relief="solid")
    PhoneNumberEntry.insert(0,' ex :  28168997')
    PhoneNumberEntry.bind('<FocusOut>',WriteMsg)
    PhoneNumberEntry.bind('<FocusIn>',DeleteMsg)
    PhoneNumberEntry.grid(column=1,row=5,padx=0,pady=0,columnspan=3)


def DrawMainFrame():
    global AddContactImage,SearchContactImage
    for widget in root.winfo_children():
        widget.grid_forget()
    AddContactButton=Button(root,image=AddContactImage,command=lambda : DrawAddContactFrame(),relief='flat')
    AddContactButton.grid(column=0,row=0)
    SearchContact=Button(root,image=SearchContactImage,relief='flat',command=lambda : DrawSearchFrame())
    SearchContact.grid(column=1,row=0)
    root.geometry("775x305")



def DrawSearchFrame():
    global SearchIcon,HeaderImage2,CancelImage

    for widget in root.winfo_children():
        widget.grid_forget()
    root.geometry('380x300')

    CancelButton=Button(root,image=CancelImage,relief='flat',borderwidth=-4,height=69,command= lambda : DrawMainFrame())
    CancelButton.grid(column=1,row=1,padx=0,pady=0)

    HeaderCanvas=Canvas(root,width=237,height=75,borderwidth=-4,bg='white',relief='flat')
    HeaderCanvas.create_image(0,0, anchor=NW, image=HeaderImage2)
    HeaderCanvas.grid(column=2,row=1,padx=0,pady=0)

    Confirm=Button(root,image=SearchIcon,command=lambda:Search(NameEntry.get()),relief='flat',borderwidth=-4,height=69)
    Confirm.grid(column=3,row=1,padx=0,pady=0)

    NameLabel=Label(root,text=" Search for:",font=('futurist-fixed-width', 20),fg='blue',relief='flat',bg='white')
    NameLabel.grid(column=1,row=2,padx=0,pady=5,columnspan=2)

    NameEntry=Entry(root,font=('futurist-fixed-width', 20),width=18,foreground='#343634',relief="solid")
    NameEntry.grid(column=1,row=3,padx=0,pady=10,columnspan=3)


def Search(ch):

    DrawSearchFrame()
    l=SearchInFile(ch)
    print(l)
    if len(l)==0:
        NameLabel=Label(root,text="No contacts found",font=('futurist-fixed-width', 20),fg='#98aba7',relief='flat',bg='white')
        NameLabel.grid(column=2,row=4,padx=0,pady=5,columnspan=1)
    else:
        x=4
        Size=300
        for i in l :
            SizeGeomtry="380x"+str(Size)
            root.geometry(SizeGeomtry)

            name=''
            Phone=''
            j=0
            while i[j]!=',' :
                name=name+i[j]
                j=j+1
            while  len(i)-2>j:
                Phone=Phone+i[j+1]
                j=j+1

            NameLabel=Label(root,text="      Name :  "+name,font=('futurist-fixed-width', 20),fg='blue',relief='flat',bg='white')
            NameLabel.grid(column=1,row=x,padx=0,pady=5,columnspan=3,sticky='w')
            NameLabel=Label(root,text="      Phone number: "+Phone,font=('futurist-fixed-width', 20),fg='blue',relief='flat',bg='white')
            NameLabel.grid(column=1,row=x+1,padx=0,pady=5,columnspan=3,sticky='w')
            x=x+2
            Size=Size+100



def SearchInFile(ch):
    l=[]
    f=open("data.txt","r")
    while True:
        s=f.readline()
        if s!='':
            if ch in s :
                l.append(s)
        else:
            break;
    f.close()
    return l





root=Tk()



root.configure(bg='white')

NumberButton=PhotoImage(file="buttonbg.png")
Delete=PhotoImage(file="delete.png")
ResetImage=PhotoImage(file="reset.png")
CancelImage=PhotoImage(file="x.png")
ConfirmImage=PhotoImage(file="confirm.png")
HeaderImage=PhotoImage(file="header.png")
AddContactImage=PhotoImage(file="add.png")
SearchContactImage=PhotoImage(file="search.png")
SearchIcon=PhotoImage(file='searchIcon.png')
HeaderImage2=PhotoImage(file="header2.png")
root.geometry("380x650")
DrawMainFrame()




mainloop()
