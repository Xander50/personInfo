from tkinter import *
from tkinter import messagebox



root = Tk()
root.geometry('1200x1200')
root.config(bg = '#FFA500')
contactlist = [
    ['Alexander','alexanderjaramillo1130s@gmail.com','videogames, cooking, and coding'],
    ['Gaurav Patil', 'Gaurav Patil@gmail.com','videogames, cooking, and coding'],
    ['Abhishek Nikam', 'person1@gmail.com','videogames, cooking, and coding'],
    ['Sakshi Gaikwad', 'person2@gmail.com','videogames, cooking, and coding'],
    ['Mohit Paul', 'person3@gmail.com','videogames, cooking, and coding'],
    ['Karan Patel', 'person4@gmail.com','videogames, cooking, and coding'],
    ['Sam Sharma', 'person5@gmail.com','videogames, cooking, and coding'],
    ['John Maheshwari', 'person6@gmail.com','videogames, cooking, and coding'],
    ['Ganesh Pawar','person7@gmail.com','videogames, cooking, and coding']
    ]

Name = StringVar()
Email= StringVar()
Hobby = StringVar()



frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',14),bg="#f0fffc",width=70,height=70,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=2)




def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
    

def AddContact():
    if Name.get()!="" and Email.get()!="" and Hobby.get()!="":
        contactlist.append([Name.get() ,Email.get(),Hobby.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New person info")

    else:
        messagebox.showerror("Error","Please fill the information")




def UpdateDetail():
	if Name.get() and Email.get() and Hobby.get():
		contactlist[Selected()] = [Name.get(), Email.get(),Hobby.get()]
    

		messagebox.showinfo("Confirmation", "Successfully Updated this person's info")
		EntryReset()
		Select_set()

	elif not(Name.get()) and not(Email.get()) and not(Hobby.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)

def EntryReset():

	Name.set('')
	Email.set('')
    Hobby.set('')


def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   

def VIEW():
    NAME, EMAIL,HOBBY = contactlist[Selected()]
    Name.set(NAME)
    Email.set(EMAIL)
    Hobby.set(HOBBY)
        

  
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name in contactlist :
        select.insert (END, name)
Select_set()


 
Label(root, text = 'Name', font=("Times new roman",25,"bold"), bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name, width=30).place(x= 200, y=30)
Label(root, text = 'Email', font=("Times new roman",22,"bold"),bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Email, width=30).place(x= 200, y=80)
Label(root, text = 'Hobby', font=("Times new roman",22,"bold"),bg = 'SlateGray3').place(x= 30, y=120)
Entry(root, textvariable = Hobby, width=30).place(x= 200, y=130)

Button(root,text=" ADD", font='Helvetica 18 bold',bg='#e8c1c7', command = AddContact, padx=20). place(x= 50, y=160)
Button(root,text="EDIT", font='Helvetica 18 bold',bg='#e8c1c7',command = UpdateDetail, padx=20).place(x= 50, y=220)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = Delete_Entry, padx=20).place(x= 50, y=280)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#e8c1c7', command = VIEW).place(x= 50, y=345)
Button(root,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = EntryReset).place(x= 50, y=410)
Button(root,text="EXIT", font='Helvetica 24 bold',bg='tomato', command = EXIT).place(x= 250, y=490)

root.mainloop()