from tkinter import *
from tkinter import messagebox
from back import *

win = Tk()

win.geometry("700x400")

##############  functions 

def clear_ent():
    ent_name.delete(0,END)
    ent_family.delete(0,END)
    ent_password.delete(0,END)
    ent_class.delete(0,END)
    ent_login.delete(0,END)


def show():
    lst_box.delete(0,END)
    for i in show_all():
        text = F"{i[0]} {i[1]} {i[2]} {i[3]}"
        lst_box.insert(END,text)


def add():
    name = ent_name.get()
    family = ent_family.get()
    password = ent_password.get()
    clas = ent_class.get()

    if not name or not family or not password:
        messagebox.showerror("Invaid" , "You need to fill out Name or Family or Password")
        return


    insert_record(name,family,clas,password)
    show()
    clear_ent()


def delete ():
    if not lst_box.curselection():
        return  
    answer = messagebox.askquestion("Delete","Do you want to delete ?")
    if answer =="yes":
        item= lst_box.get(lst_box.curselection())
        student_id = int(item.split()[0])
        delete_student(student_id)
        show()
        clear_ent()


def select(event):
    if not lst_box.curselection():
        return

    item = lst_box.get(lst_box.curselection())
    student_id= int(item.split()[0])
    student = get_student(student_id)

    clear_ent()
    ent_name.insert(0,student[1])
    ent_family.insert(0,student[2])
    ent_class.insert(0,student[3])
    ent_password.insert(0,student[4])

def login_into():
    log = ent_login.get()
    if not log:
        messagebox.showwarning("PASSWORD","Please enter youre passwrod")
        return

    result = login(log)
    if result:
        messagebox.showinfo("Wellcome","Wellcome to Emam Ali")

    else:
        messagebox.showerror("PASSWORD","Youre password is wrong")


def exit_app():

    answer = messagebox.askquestion("EXIT","Do you want to exit ? ")
    if answer=="yes":
        close_db()
        win.destroy()










##########   wigets
ent_family=Entry(win)
ent_family.place(x=15,y=10)

ent_name=Entry(win)
ent_name.place(x=450,y=10)

ent_password=Entry(win,show="*")
ent_password.place(x=15,y=40)

ent_class=Entry(win)
ent_class.place(x=450,y=40)

lbl_family=Label(win,text=": Familly")
lbl_family.place(x=170,y=10)

lbl_name=Label(win,text=": Name")
lbl_name.place(x=605,y=10)

lbl_password=Label(win,text=": Password")
lbl_password.place(x=170,y=40)

lbl_class=Label(win,text=": Class")
lbl_class.place(x=605,y=40)

lst_box = Listbox(win,width=50)
lst_box.place(x=15,y=80)


btn_show = Button(win,width=25,text="Show all",command=show)
btn_show.place(x=450,y=80)

btn_add=Button(win,text="Add",width=25,command=add)
btn_add.place(x=450,y=120)

btn_clear=Button(win,text="Clear",width=25,command=clear_ent)
btn_clear.place(x=450,y=170)

btn_delete=Button(win,text="Delete",width=25,command=delete)
btn_delete.place(x=450,y=210)

btn_exit=Button(win,text="Exit",width=25,command=exit_app)
btn_exit.place(x=450,y=250)

btn_enter=Button(win,text="Enter",width=25,command=login_into)
btn_enter.place(x=450,y=290)

ent_login=Entry(win,width=70)
ent_login.place(x=15,y=340)

lbl_pass=Label(win,text=": Enter youre password ")
lbl_pass.place(x=480,y=340)


show()
lst_box.bind("<<ListboxSelect>>", select) 

win.mainloop()
