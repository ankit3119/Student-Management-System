def addstudent():

    def submit_add():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        addedtime = time.strftime("%H:%M:%S")
        try:
            strr = 'INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} name {} added successfully and do you want to clear form'
                                            .format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','ID already exists.Try another value',parent=addroot)

        strr = 'SELECT * FROM student'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentTable.insert('',END,values=vv)


    addroot = Toplevel(master=DataEntryFrames)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='cyan')
    addroot.iconbitmap(r'F:\Python Project\student management\stud.ico')
    addroot.resizable(False,False)
    ######### LABELS #############
    idlabel = Label(addroot,text="Enter id",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    Namelabel = Label(addroot,text="Enter Name",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Namelabel.place(x=10,y=70)

    Mobilelabel = Label(addroot,text="Enter Mobile",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Mobilelabel.place(x=10,y=130) 

    Emaillabel = Label(addroot,text="Enter Email",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Emaillabel.place(x=10,y=190)

    Addresslabel = Label(addroot,text="Enter Address",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Addresslabel.place(x=10,y=250)

    Genderlabel = Label(addroot,text="Enter Gender",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Genderlabel.place(x=10,y=310)

    Doblabel = Label(addroot,text="Enter D.O.B",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Doblabel.place(x=10,y=370)
    ########## EntryBox #########
    idval = StringVar()
    identry = Entry(addroot,font=('times',15),bd=5,textvariable=idval,relief=GROOVE)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(addroot,font=('times',15),bd=5,textvariable=nameval,relief=GROOVE)
    nameentry.place(x=250,y=70)

    mobileval = StringVar()
    mobileentry = Entry(addroot,font=('times',15),bd=5,textvariable=mobileval,relief=GROOVE)
    mobileentry.place(x=250,y=130)

    emailval = StringVar()
    emailentry = Entry(addroot,font=('times',15),bd=5,textvariable=emailval,relief=GROOVE)
    emailentry.place(x=250,y=190)

    addressval = StringVar()
    addressentry = Entry(addroot,font=('times',15),bd=5,textvariable=addressval,relief=GROOVE)
    addressentry.place(x=250,y=250)

    genderval = StringVar()
    genderentry = Entry(addroot,font=('times',15),bd=5,textvariable=genderval,relief=GROOVE)
    genderentry.place(x=250,y=310)

    dobval = StringVar()
    dobentry = Entry(addroot,font=('times',15),bd=5,textvariable=dobval,relief=GROOVE)
    dobentry.place(x=250,y=370)

    submitbtn = Button(addroot,text='SUBMIT',font=('Comic Sans MS',15,),bd=5,relief=RAISED,bg='skyblue3',activebackground="red",
                       activeforeground="white",command=submit_add)
    submitbtn.place(x=150,y=410)
    addroot.mainloop     
##############################################################################################################################                      
def searchstudent():

    def submit_search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = dateval.get()
        if(id!=''):
            strr = 'SELECT * FROM student WHERE id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        elif(name!=''):
            strr = 'SELECT * FROM student WHERE name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        elif(mobile!=''):
            strr = 'SELECT * FROM student WHERE mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        elif(email!=''):
            strr = 'SELECT * FROM student WHERE email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        elif(address!=''):
            strr = 'SELECT * FROM student WHERE address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        elif(gender!=''):
            strr = 'SELECT * FROM student WHERE gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        if(dob!=''):
            strr = 'SELECT * FROM student WHERE dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)
        elif(addeddate!=''):
            strr = 'SELECT * FROM student WHERE addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vv)

    searchroot = Toplevel(master=DataEntryFrames)
    searchroot.grab_set()
    searchroot.geometry('470x530+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='cyan')
    searchroot.iconbitmap(r'F:\Python Project\student management\stud.ico')
    searchroot.resizable(False,False)
    ######### LABELS #############
    idlabel = Label(searchroot,text="Enter id",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    Namelabel = Label(searchroot,text="Enter Name",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Namelabel.place(x=10,y=70)

    Mobilelabel = Label(searchroot,text="Enter Mobile",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Mobilelabel.place(x=10,y=130) 

    Emaillabel = Label(searchroot,text="Enter Email",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Emaillabel.place(x=10,y=190)

    Addresslabel = Label(searchroot,text="Enter Address",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Addresslabel.place(x=10,y=250)

    Genderlabel = Label(searchroot,text="Enter Gender",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Genderlabel.place(x=10,y=310)

    Doblabel = Label(searchroot,text="Enter D.O.B",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Doblabel.place(x=10,y=370)

    Datelabel  = Label(searchroot,text="Enter Date",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Datelabel.place(x=10,y=430)
    ########## EntryBox #########
    idval = StringVar()
    identry = Entry(searchroot,font=('times',15),bd=5,textvariable=idval,relief=GROOVE)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(searchroot,font=('times',15),bd=5,textvariable=nameval,relief=GROOVE)
    nameentry.place(x=250,y=70)

    mobileval = StringVar()
    mobileentry = Entry(searchroot,font=('times',15),bd=5,textvariable=mobileval,relief=GROOVE)
    mobileentry.place(x=250,y=130)

    emailval = StringVar()
    emailentry = Entry(searchroot,font=('times',15),bd=5,textvariable=emailval,relief=GROOVE)
    emailentry.place(x=250,y=190)

    addressval = StringVar()
    addressentry = Entry(searchroot,font=('times',15),bd=5,textvariable=addressval,relief=GROOVE)
    addressentry.place(x=250,y=250)

    genderval = StringVar()
    genderentry = Entry(searchroot,font=('times',15),bd=5,textvariable=genderval,relief=GROOVE)
    genderentry.place(x=250,y=310)

    dobval = StringVar()
    dobentry = Entry(searchroot,font=('times',15),bd=5,textvariable=dobval,relief=GROOVE)
    dobentry.place(x=250,y=370)

    dateval = StringVar()
    dateentry = Entry(searchroot,font=('times',15),bd=5,textvariable=dateval,relief=GROOVE)
    dateentry.place(x=250,y=430)

    submitbtn = Button(searchroot,text='SUBMIT',font=('Comic Sans MS',15,),bd=5,relief=RAISED,bg='skyblue3',activebackground="red",
                       activeforeground="white",command=submit_search)
    submitbtn.place(x=150,y=470)

    searchroot.mainloop

def deletestudent():
    cc = studentTable.focus()
    content = studentTable.item(cc)
    pp = content['values'][0]
    strr = 'DELETE FROM student WHERE id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','ID {} deleted successfully...'.format(pp))
    strr = 'SELECT * FROM student'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studentTable.insert('',END,values=vv)    

def updatestudent():
    def submit_update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'UPDATE student SET name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s WHERE id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','ID {} updated successfully........'.format(id),parent=updateroot)
        strr = 'SELECT * FROM student'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentTable.insert('',END,values=vv)

            
    updateroot = Toplevel(master=DataEntryFrames)
    updateroot.grab_set()
    updateroot.geometry('470x595+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='cyan')
    updateroot.iconbitmap(r'F:\Python Project\student management\stud.ico')
    updateroot.resizable(False,False)
    ######### LABELS #############
    idlabel = Label(updateroot,text="Enter id",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    Namelabel = Label(updateroot,text="Enter Name",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Namelabel.place(x=10,y=70)

    Mobilelabel = Label(updateroot,text="Enter Mobile",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Mobilelabel.place(x=10,y=130) 

    Emaillabel = Label(updateroot,text="Enter Email",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Emaillabel.place(x=10,y=190)

    Addresslabel = Label(updateroot,text="Enter Address",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Addresslabel.place(x=10,y=250)

    Genderlabel = Label(updateroot,text="Enter Gender",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Genderlabel.place(x=10,y=310)

    Doblabel = Label(updateroot,text="Enter D.O.B",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Doblabel.place(x=10,y=370)

    Datelabel  = Label(updateroot,text="Enter Date",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Datelabel.place(x=10,y=430)

    Timelabel  = Label(updateroot,text="Enter Time",bg='skyblue3',font=('Comic Sans MS',16),relief=RIDGE,borderwidth=3,width=12,anchor='w')
    Timelabel.place(x=10,y=490)

    ########## EntryBox #########
    idval = StringVar()
    identry = Entry(updateroot,font=('times',15),bd=5,textvariable=idval,relief=GROOVE)
    identry.place(x=250,y=10)

    nameval = StringVar()
    nameentry = Entry(updateroot,font=('times',15),bd=5,textvariable=nameval,relief=GROOVE)
    nameentry.place(x=250,y=70)

    mobileval = StringVar()
    mobileentry = Entry(updateroot,font=('times',15),bd=5,textvariable=mobileval,relief=GROOVE)
    mobileentry.place(x=250,y=130)

    emailval = StringVar()
    emailentry = Entry(updateroot,font=('times',15),bd=5,textvariable=emailval,relief=GROOVE)
    emailentry.place(x=250,y=190)

    addressval = StringVar()
    addressentry = Entry(updateroot,font=('times',15),bd=5,textvariable=addressval,relief=GROOVE)
    addressentry.place(x=250,y=250)

    genderval = StringVar()
    genderentry = Entry(updateroot,font=('times',15),bd=5,textvariable=genderval,relief=GROOVE)
    genderentry.place(x=250,y=310)

    dobval = StringVar()
    dobentry = Entry(updateroot,font=('times',15),bd=5,textvariable=dobval,relief=GROOVE)
    dobentry.place(x=250,y=370)

    dateval = StringVar()
    dateentry = Entry(updateroot,font=('times',15),bd=5,textvariable=dateval,relief=GROOVE)
    dateentry.place(x=250,y=430)

    timeval = StringVar()
    timeentry = Entry(updateroot,font=('times',15),bd=5,textvariable=timeval,relief=GROOVE)
    timeentry.place(x=250,y=490)

    submitbtn = Button(updateroot,text='SUBMIT',font=('Comic Sans MS',15,),bd=5,relief=RAISED,bg='skyblue3',activebackground="red",
                       activeforeground="white",command=submit_update)
    submitbtn.place(x=150,y=530)

    cc =studentTable.focus()
    content = studentTable.item(cc)
    pp = content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    

    updateroot.mainloop


def displaystudent():
    strr = 'SELECT * FROM student'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studentTable.insert('',END,values=vv)
def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studentTable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studentTable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res==True):
        root.destroy()
###################################################################################################################################
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is Incorrect.Please enter correct Values')
            return

        try:
            strr = 'CREATE DATABASE studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'USE studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'CREATE TABLE student(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(50),gender varchar(10),DOB VARCHAR(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'ALTER TABLE student ADD PRIMARY KEY(id)'
            mycursor.execute(strr)
            messagebox.showinfo('Notifications','Database created and you are connected to the database.....',parent=dbroot)

        except:
            strr = 'USE studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notifications','You are connected to the database.....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.config(bg="cyan")
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap(r'F:\Python Project\student management\stud.ico')
    ##### inside stuffs  #####
    hostLabel = Label(dbroot,text="Host name",font=("Comic Sans MS",16),bg='skyblue3',relief=RIDGE,borderwidth=3,width=11,anchor=W,bd=5)
    hostLabel.place(x=5,y=5)
    UserLabel = Label(dbroot,text="User name",font=("Comic Sans MS",16),bg='skyblue3',relief=RIDGE,borderwidth=3,width=11,anchor=W,bd=5)
    UserLabel.place(x=5,y=65)
    PassLabel = Label(dbroot,text="Password",font=("Comic Sans MS",16),bg='skyblue3',relief=RIDGE,borderwidth=3,width=11,anchor=W,bd=5)
    PassLabel.place(x=5,y=125)

    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()
    hostEntry = Entry(dbroot,relief=GROOVE,font=("times",15),bd=5,textvariable=hostval)
    hostEntry.place(x=230,y=5)
    userEntry = Entry(dbroot,relief=GROOVE,font=("times",15),bd=5,textvariable=userval)
    userEntry.place(x=230,y=65)
    passEntry = Entry(dbroot,relief=GROOVE,font=("times",15),bd=5,textvariable=passval)
    passEntry.place(x=230,y=125)

    submitButton = Button(dbroot,text="SUBMIT",font=('Comic Sans MS',16,),bd=5,relief=RAISED,bg='skyblue3',activebackground="red",
                          activeforeground="white",command=submitdb)
    submitButton.place(x=170,y=185)

    dbroot.mainloop()
    

def tick():
    timestr = time.strftime("%H:%M:%S")
    datestr = time.strftime("%d/%m/%Y")
    Clock.config(text="Date: "+datestr+"\n"+"Time: "+timestr)
    Clock.after(200,tick)

def IntroLabelTick():
    global count, text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
    count+=1
    SliderLabel.after(200, IntroLabelTick)
####################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import time
import pymysql
import pandas
root = Tk()
root.title("Student Management System")
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.iconbitmap(r'F:\Python Project\student management\stud.ico')
root.resizable(False,False)
##############################################################################################
#                              FRAMES

#######################################################
#                             Data Entry Frame

DataEntryFrames = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrames.place(x=10,y=80,width = 520,height=600)
frontlabel = Label(DataEntryFrames,text="----------------WELCOME----------------",width=30,font=("times",22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)
addbutton = Button(DataEntryFrames,text="Add Student",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=addstudent)
addbutton.pack(side=TOP,expand=True)
searchbutton = Button(DataEntryFrames,text="Search Student",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=searchstudent)
searchbutton.pack(side=TOP,expand=True)
deletebutton = Button(DataEntryFrames,text="Delete Student",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=deletestudent)
deletebutton.pack(side=TOP,expand=True)
updatebutton = Button(DataEntryFrames,text="Update Student",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=updatestudent)
updatebutton.pack(side=TOP,expand=True)
displaybutton = Button(DataEntryFrames,text="Display Students",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=displaystudent)
displaybutton.pack(side=TOP,expand=True)
exportbutton = Button(DataEntryFrames,text="Export Data",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=exportstudent)
exportbutton.pack(side=TOP,expand=True)
exitbutton = Button(DataEntryFrames,text="Exit",width=20,font=('Comic Sans MS',16),bd=6,bg='skyblue3',activebackground='blue',
                    activeforeground='white',relief=RIDGE,command=exitstudent)
exitbutton.pack(side=TOP,expand=True)

##############################################################################################################################
##################                      Show Data Frame            ###############################


ShowDataFrames = Frame(root,bg='gold2',relief=RIDGE,borderwidth=5)
ShowDataFrames.place(x=550,y=80,width = 614,height=600)

style = ttk.Style()
style.configure('Treeview.Heading',font=('Comic Sans MS',12,'bold'),foreground = 'blue')
style.configure('Treeview',font=('times',13,'bold'),foreground = 'black',background='cyan')
scroll_x = Scrollbar(ShowDataFrames,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrames,orient=VERTICAL)
studentTable = Treeview(ShowDataFrames,column=('Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studentTable.xview)
scroll_y.config(command=studentTable.yview)
studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')
studentTable['show'] = 'headings'
studentTable.column('Id',width=100)
studentTable.column('Name',width=200)
studentTable.column('Mobile',width=200)
studentTable.column('Email',width=300)
studentTable.column('Address',width=300)
studentTable.column('Gender',width=100)
studentTable.column('D.O.B',width=150)
studentTable.column('Added Date',width=150)
studentTable.column('Added Time',width=150)
studentTable.pack(fill=BOTH,expand=1)

########################################################################################################
#                              Slider

ss = "Student Management System"
count = 0
text = ''
SliderLabel = Label(root,bg='cyan',font=("Times", "24"),text=ss,relief=RIDGE,borderwidth=4,width=25)
SliderLabel.place(x=350,y=0)
IntroLabelTick()
#########################################################################################################
#                               Clock

Clock = Label(root,font=("Times", "14"),relief=RIDGE,borderwidth=4,bg='cyan')
Clock.place(x=10,y=0)
tick()
##########################################################################################################
#                               connect to database button

connectbutton = Button(root,text="Connect to Database",font=("Times", "18"),bg="cyan",borderwidth=4,activebackground="blue",
                       activeforeground="white",relief=RAISED,command=Connectdb)
connectbutton.place(x=900,y=0)

root.mainloop()