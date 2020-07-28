import sqlite3

conn = sqlite3.connect("Database.db")
c = conn.cursor()

choice = """
    [1]  Create New Account
    [2] Withdraw Money
    [3] Deposit Money
    [4] Check Saving      
"""
print(choice)

pick = int(input("Enter Number : "))

"""========================================METHOD==========================================================="""

def create_account():
    fname = input("Enter First Name : ")
    lname = input("Enter Last Name : ")
    pin = input("Enter Pin Code : ")
    if len(pin) == 6:
        find = "SELECT * FROM account WHERE firstname = ? and pin = ?"
        c.execute(find,(fname,pin))
        if c.fetchall():
            print("Your Firstname And Pin Code is Taken")
        else:
            saving = input("Enter Amount you want to Deposit : ")
            c.execute("CREATE TABLE IF NOT EXISTS account (firstname TEXT, lastname TEXT, pin TEXT, saving INTEGER)")
            a = "INSERT      INTO account(firstname, lastname, pin, saving) VALUES(?, ?, ?, ?)"
            c.execute(a, (fname, lname, pin, saving))
            print("Your account was successfully Created")
        conn.commit()
    else:
        print("Sorry! Your Pin must be 6 Numbers only")

"""========================================METHOD==========================================================="""

def withdraw():
    fname = input("Enter Your Firstname : ")
    pin = input("Enter Your Pin : ")
    sql = "SELECT * FROM account WHERE firstname = ? AND pin = ?"
    c.execute(sql,(fname,pin))
    if c.fetchall():
        wdraw = int(input("Enter Amount you want to Withdraw : "))
        f = c.execute(sql, (fname, pin))
        for i in f:
            if i[3] >= wdraw:
                a = i[3] - wdraw
                a1 = "UPDATE account set saving = ? WHERE firstname = ?"
                c.execute(a1, (a, fname))
                print("Successfully Withdraw")
                print("Your savings is "+str(a))
            else:
                print("You Savings is "+str(i[3])+" Pesos Only")


        conn.commit()


    else:
        print("You don't have an account")
"""========================================METHOD==========================================================="""

def deposit():
    fname = input("Enter Your Firstname : ")
    pin = input("Enter Your Pin : ")
    sql = "SELECT * FROM account WHERE firstname = ? AND pin = ?"
    c.execute(sql, (fname, pin))
    if c.fetchall():
        dep = int(input("Enter Amount you want to Deposit : "))
        f = c.execute(sql,(fname,pin))
        for i in f:
            a = dep+i[3]
            a1 ="UPDATE account set saving = ? WHERE firstname = ?"
            c.execute(a1,(a,fname))

        print("Successfully Deposit")
        print("Your Savings is "+str(a))
        conn.commit()
    else:
        print("You don't have an account")

"""========================================METHOD==========================================================="""

def acc():
    fname = input("Enter Your Firstname : ")
    pin = input("Enter Your Pin : ")
    sql = "SELECT * FROM account WHERE firstname = ? AND pin = ?"
    c.execute(sql, (fname, pin))
    if c.fetchall():
        f = c.execute(sql, (fname, pin))
        for i in f:
            print("-------------------------")
            print("     Account Details")
            print("-------------------------")
            print("Firstname : "+i[0])
            print("Lastname : "+i[1])
            print("Pin : "+i[2])
            print("Saving : "+str(i[3]))

    else:
        print("You don' have an Account")

"""========================================METHOD==========================================================="""

if pick == 1:
    create_account()

elif pick == 2:
    withdraw()

elif pick ==3:
    deposit()

elif pick ==4:
    acc()

else:
    print("Invalid Number")