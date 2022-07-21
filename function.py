class main:
    def cur(self):
        self.fm3=Frame(root,bg='#fff',width=900,height=390)
        self.fm3.place(x=0,y=110)
        
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            if int(h) >=12 and int(m) >=0:
                    self.lb7_hr.config(text="PM")

            #if int(h) > 12:
                    #h = str(int(h) // 12)

            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)

            self.lb1_hr.after(200, clock)
        
        self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb1_hr.place(x=607, y=0, width=60, height=30)
        
        
        self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb3_hr.place(x=677, y=0, width=60, height=30)
        
        
        self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb5_hr.place(x=747, y=0, width=60, height=30)
        
        
        self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#581845', fg='white')
        self.lb7_hr.place(x=817, y=0, width=60, height=30)
        
        clock()
        
        #right side image
        self.canvas8 = Canvas(self.fm3, bg='black', width=400, height=300)
        self.canvas8.place(x=475, y=40)
        self.photo9=PhotoImage(file="filename.png")
        self.canvas8.create_image(0,0,image=self.photo9,anchor=NW)
        
        self.develop=Label(self.fm3,text='Developed By - <YourName>',bg='#fff',fg='#d7837f',
                       font=('Candara',12,'bold'))
        self.develop.place(x=732,y=350)
        
        #AddButton

        self.bt1=Button(self.fm3,text='  Add Books',fg='#fff',bg='#581845',font=('Candara',15,'bold'),width=170,
                  height=0,bd=7,relief='flat',command=self.addbook,cursor='hand2',activebackground='black',activeforeground='#581845')
        self.bt1.place(x=40,y=40)
        self.logo = PhotoImage(file='filename.png')
        self.bt1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1,1)
        self.bt1.config(image=self.small_logo)
        
        #IssueButton

        self.bt2 = Button(self.fm3, text='  Issue Books', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                    width=170,height=0, bd=7,relief='flat',command=self.issuebook,cursor='hand2',activebackground='black',activeforeground='#581845')
        self.bt2.place(x=250, y=40)
        self.log = PhotoImage(file='bt2.png')
        self.bt2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1, 1)
        self.bt2.config(image=self.small_log)
        
        #EditButton

        self.bt3 = Button(self.fm3, text='  Edit Books', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                   width=170,height=0,bd=7,relief='flat',cursor='hand2',command=self.edit,activebackground='black',activeforeground='#581845')
        self.bt3.place(x=40, y=120)
        self.logb = PhotoImage(file='bt3.png')
        self.bt3.config(image=self.logb, compound=LEFT)
        self.small_logb = self.logb.subsample(1, 1)
        self.bt3.config(image=self.small_logb)
        
        #ReturnButton

        self.bt4 = Button(self.fm3, text='  Return Books', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                  width=170,height=0,bd=7,relief='flat',cursor='hand2',command=self.returnbook,activebackground='black',activeforeground='#581845')
        self.bt4.place(x=250, y=120)
        self.log4 = PhotoImage(file='bt4.png')
        self.bt4.config(image=self.log4, compound=LEFT)
        self.small_log4 = self.log4.subsample(1, 1)
        self.bt4.config(image=self.small_log4)
        
        #DeleteButton

        self.bt5 = Button(self.fm3, text=' Delete Books', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                  width=170,height=0,bd=7,relief='flat',cursor='hand2',command=self.delete,activebackground='black',activeforeground='#581845')
        self.bt5.place(x=40, y=200)
        self.log5 = PhotoImage(file='bt5.png')
        self.bt5.config(image=self.log5, compound=LEFT)
        self.small_log5 = self.log5.subsample(1, 1)
        self.bt5.config(image=self.small_log5)
        
                
        #ShowButton

        self.bt6 = Button(self.fm3, text=' Show Books', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                  width=170,height=0,bd=7, relief='flat',cursor='hand2',command=self.show,activebackground='black',activeforeground='#581845')
        self.bt6.place(x=40, y=280)
        self.log6 = PhotoImage(file='bt6.png')
        self.bt6.config(image=self.log6, compound=LEFT)
        self.small_log6 = self.log6.subsample(1, 1)
        self.bt6.config(image=self.small_log6)
        
        
        #SearchButton

        self.bt7 = Button(self.fm3, text='  Search Books', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                   width=170,height=0,bd=7, relief='flat',cursor='hand2',command=self.search,activebackground='black',activeforeground='#581845')
        self.bt7.place(x=250, y=200)
        self.log7 = PhotoImage(file='bt7.png')
        self.bt7.config(image=self.log7, compound=LEFT)
        self.small_log7 = self.log7.subsample(1, 1)
        self.bt7.config(image=self.small_log7)
        
        
        #ExitButton
        try:
        
            self.bt8 = Button(self.fm3, text='  Log Out', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'),
                           width=170,
                      height=0, bd=7, relief='flat',cursor='hand2',command=self.code,activebackground='black',activeforeground='#581845')
            self.bt8.place(x=250, y=280)
            self.log8 = PhotoImage(file='bt8.png')
            self.bt8.config(image=self.log8, compound=LEFT)
            self.small_log8 = self.log8.subsample(1, 1)
            self.bt8.config(image=self.small_log8)
        
        except:
        
            self.bt9 = ttk.Button(self.fm3, text="Name", bg='#a40000', font=('Candara', 15, 'bold'), width=150,
                                 height=0)
            self.bt9.place(x=40, y=350)
            self.log9 = PhotoImage(file='bt8.png')
            self.bt9.config(image=self.log9, compound=LEFT)
            self.small_log9 = self.log9.subsample(3, 3)
            self.bt9.config(image=self.small_log9)  
            
    def addbook(self):
        pass
    
    def issuebook(self):
        pass
    
    def edit(self):
        pass
    
    def returnbook(self):
        pass
    
    def delete(self):
        pass
    
    def show(self):
        pass
        
    def search(self):
        pass
