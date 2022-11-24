def OK():
    username = username_login_entry.get()
    password = password__login_entry.get()
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="welcome123456",database="moonsun_hospital")
    cursor = mydb.cursor()
    
    savequery = "SELECT * FROM Login_table WHERE username=%s AND password=%s" # Get the records with these username and password ONLY
    cursor.execute(savequery,(username,password)) 
    myresult = cursor.fetchall() 
    
    if myresult: # If there is such a record, then success
        messagebox.showinfo("LOGIN",'LOGIN SUCCESSFUL')
        # Whatever you want to do after user is authentic
        new = Toplevel() # To open new window

    else: # Wrong password
        messagebox.showerror("LOGIN ERROR","LOGIN ERROR")
    cursor.close()
    mydb.close()


SELECT * FROM Login_table WHERE username='John' AND password='123123'; -- If username is john and password is 123123


