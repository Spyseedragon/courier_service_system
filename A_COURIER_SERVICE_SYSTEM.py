# -*- coding: utf-8 -*-
import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'password', database='courier_service_system' )
cust1=conn.cursor()
print(12*'*','WELCOME TO PROJECT COURIER SERVICE',12*'*')
print('Hi')
o=input('Press enter to begin your courier surfing')
print('1.CREATE YOUR COURIER SERVICE ACCOUNT')
print('2.LOGIN')
choose=int(input('ENTER (1) FOR NEW ACCOUNT OR (2) FOR LOGIN:'))
if choose==1:
    name=input('Enter your user-name:')
    passwd=input('Set your password here:')
    passwd1=input('Confirm password:')
    cust1.execute("INSERT INTO login VALUES(' "+name+" ',' "+passwd+" ')")
    conn.commit()
    print('ACCOUNT CREATED CONGRATULATIONS')
    move_in=input('press enter to login:')
    import B_COURIER_MENU
elif choose==2:
    email=input('Enter your user name')
    passd=input('Enter your PASSWORD:')
    cust1.execute('select * from login where name=" '+email+' " and password=" '+passd+' " ')
    if cust1.fetchone() is None:
        print(' sorry your password in wrong')
    else:
        import B_COURIER_MENU
        