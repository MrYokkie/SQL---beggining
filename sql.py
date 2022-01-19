import sqlite3
from random import randint
#before to create a dataset we must create 3 var reposned for connection betwenn python and sql
global db
global sql

db = sqlite3.connect("users.db") #creation of our database, in case it does not exist, it will be created, likewise it will connect us to
sql = db.cursor()# create a cursore, is needed within the work with db, to stear our databse
#create table users if not exist. CREATE TABLE - will create table/IF NOT EXISTS - to creat the table 'users' if it does not exists
sql.execute("""CREATE TABLE IF NOT EXISTS users ( 
    login TEXT, 
    password TEXT,
    cash INT 
)""") #two columnes login and passwords and cash
#now we must to cunfirm a tbale creation with "commite"
db.commit()


def reg():
    user_login = input("Log in:")
    user_password = input("Password:")

    #now we are going to check the fact of the data presence, if exists we add it, if not so not
    sql.execute("SELECT login FROM users WHERE login = '{user_login}'") #select row login from table users, with the reasone to select all from table use "*"
    if sql.fetchone() is None: #Check data in our dataset
        sql.execute(f"INSERT INTO users VALUES (?,?,?)",(user_login,user_password,0))#quastion signs allow to protect our SQL
        db.commit() #after each action must go confuramtion!!!
        print('Registered')
    else:
        print("The data was created yet")
    #output data from table,instead * could be everithing    
        for value in sql.execute("SELECT * FROM users"):
            print(value) 

def add_casino():
    user_login = input("Log in:")
    number = randint(1,2)
    
    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print("The login does not exist, please registre")
        reg()
    else:    
        if number == 1:
            sql.execute(f'UPDATE users SET cash = {1000} WHERE login = "{user_login}"')
            db.commit()
        else:
            print("You lose")

def enter():
    for i in sql.execute("SELECT login, cash FROM users"):
        print(i)

def main():
   add_casino()
   enter()

main()

