class main:

    def mouseClick(self,event):
     
        self.rog=Tk()
        self.rog.title("Change password")
        self.rog.geometry("400x300+300+210")
        self.rog.iconbitmap("filename.ico")
        self.rog.resizable(0,0)
        self.rog.configure(bg='#000')

        self.framerog=Frame(self.rog,width=160,height=30,bg="#d6ed17")
        self.framerog.place(x=95,y=15)

        self.label=Label(self.framerog,text="SET NEW PASSWORD",bg='#d6ed17',fg='#606060',font=("Calibri",12,'bold'))
        self.label.place(x=5,y=4)

        #User ID
        self.user=Label(self.rog,text='User ID',bg='#000',fg='white',font=("Times New Roman",11,'bold'))
        self.user.place(x=40,y=95)

        #New Password
        self.user = Label(self.rog, text='New Password',bg='#000', fg='white', font=("Times New Roman", 11, 'bold'))
        self.user.place(x=40, y=170)

        self.ef1 = Entry(self.rog, width=24, font=('Calibri', 8, 'bold'), bd=4, relief='groove')
        self.ef1.place(x=170, y=95)

        self.ef2 = Entry(self.rog, width=24, font=('Calibri', 8, 'bold'), bd=4, relief='groove')
        self.ef2.place(x=170, y=170)

        #Submit Button
        self.btn1 = Button(self.rog, text='SUBMIT', fg='#606060', bg='#d6ed17', width=8, font=('Calibri', 12, 'bold'),
                        activebackground='black', activeforeground='#d6ed17',bd=3, relief='flat',
                            cursor='hand2',command=self.chan_pas)
        self.btn1.place(x=40, y=240)
        
        
    
    def chan_pas(self):
    
        self.a=self.ef1.get()
        self.b=self.ef2.get()
        
        import sqlite3
        conn=sqlite3.connect('admin.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='"+self.a+"'")
        conn.commit()
        self.data=cursor.fetchone()

        if self.data!=None:
                cursor = conn.cursor()
                cursor.execute("UPDATE UserLogin SET Password='" + self.b + "' WHERE UserID='" + self.a + "'")
                conn.commit()
                messagebox.showinfo("SUCCESSFUL","Your Password is changed")
                self.rog.destroy()
        else:
                messagebox.showerror("ERROR", "UserID doesn't exist")
                self.rog.destroy()
                

        self.rog.mainloop()
