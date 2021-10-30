import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "123456",
    database = input("enter the database here\n")
)

while(True) :
    mycursor = mydb.cursor()
    # table = input("Enter the table name, which you want to get the result\n")
    command = input("enter the command here which you want to get the information about\n")

    mycursor.execute(command)

    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

    print("press 'q' to quit and 'c' for continue")
    press = ""
    while(press != "q" and press != "c") :
        press = input()
        if press == "q" :
            exit()
        elif press == "c" :
            continue    
