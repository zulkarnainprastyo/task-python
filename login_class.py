class main:

    def login(self):
    
        self.var1 = self.e1.get()
        self.var2 = self.e2.get()
        
        cursor=db.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='"+self.var1+"' and Password='"+self.var2+"'")
        db.commit()
        self.ab = cursor.fetchone()
        
        if self.ab!=None:
            self.under_fm=Frame(root,height=500,width=900,bg='#fff')
            self.under_fm.place(x=0,y=0)
            
            self.fm2=Frame(root,bg='#012727',height=80,width=900)
            self.fm2.place(x=0,y=0)
            
            self.lbb=Label(self.fm2,bg='#012727')
            self.lbb.place(x=15,y=5)
            self.ig=PhotoImage(file='filename.png')
            self.lbb.config(image=self.ig)
            
            self.lb3=Label(self.fm2,text='DASHBOARD',fg='White',bg='#012727',font=('times new roman',30,'bold'))
            self.lb3.place(x=325,y=17)
            
            #Name of the logged in admin
            self.name=Label(root,text="Name : ",bg='#fff',fg="black",font=('Calibri',12,'bold'))
            self.name.place(x=5,y=83)
            self.name1=Label(root,text=self.ab[0],fg='black',bg='#fff',font=('Calibri',12,'bold'))
            self.name1.place(x=60,y=83)
            
            #Display Date
            self.today=date.today()
            self.dat=Label(root,text='Date : ',bg='#fff',fg='black',font=('Calibri',12,'bold'))
            self.dat.place(x=750,y=83)
            self.dat2 = Label(root, text=self.today, bg='#fff', fg='black', font=('Calibri', 12, 'bold'))
            self.dat2.place(x=800, y=83)
            
            #For Head part
            self.cur()

        else:
            messagebox.showerror('Library System', 'Your ID or Password is invalid!')
