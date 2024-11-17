def update(t): 
    print(""" 
                         1. SCHEDULE DATE 
                         2. SCHEDULE TIME 
                         3. SERVICES 
    """) 
    choice = int(input("Enter your choice")) 
    if choice == 1: 
        update_date(t) 
    elif choice == 2: 
        update_time(t) 
    elif choice == 3: 
        update_services(t) 
    else: 
        print("Error: invalid choice") 

def update_date(u):      
    s = input("Enter date to be modified") 
    so = "SELECT service_date FROM schedule WHERE service_date='{0}' AND user='{1}'".format(s, u) 
    cur.execute(so) 
    row = cur.fetchall() 
    for i in row: 
        print(i) 
    if len(row) == 0: 
        print("Sorry, the date is not in the table") 
    else: 
        dt = input("Enter new date") 
        st = "UPDATE schedule SET service_date='{0}' WHERE service_date='{1}' AND user='{2}'".format(dt, s, u) 
        cur.execute(st) 
        con.commit() 
        print("Data updated successfully") 

def update_time(u):         
    sno = input("Enter time slot to be modified") 
    so = "SELECT Time_service FROM schedule WHERE Time_service='{0}' AND user='{1}'".format(sno, u) 
    cur.execute(so) 
    row = cur.fetchall() 
    for i in row: 
        print(i) 
    if len(row) == 0: 
        print("Sorry, the time slot is not in the table") 
    else: 
        ti = input("Enter new time") 
        st = "UPDATE schedule SET Time_service='{0}' WHERE Time_service='{1}' AND user='{2}'".format(ti, sno, u) 
        cur.execute(st) 
        con.commit() 
        print("Data updated successfully") 

def update_services(u):      
    sno = input("Enter service to be modified") 
    so = "SELECT service FROM schedule WHERE service='{0}' AND user='{1}'".format(sno, u) 
    cur.execute(so) 
    row = cur.fetchall() 
    for i in row: 
        print(row) 
    if len(row) == 0: 
        print("Sorry, the service is not chosen by " + u + " yet") 
    else:     
        sr = input("Enter new services") 
        st = "UPDATE schedule SET service='{0}' WHERE service='{1}' AND user='{2}'".format(sr, sno, u) 
        cur.execute(st) 
        
        # Adjust Total_bill after changing service
        cur.execute('SELECT rates FROM services WHERE service_name="{}"'.format(sno)) 
        r1 = cur.fetchone() 
        cur.execute('SELECT rates FROM services WHERE service_name="{}"'.format(sr)) 
        r2 = cur.fetchone() 
        cur.execute('UPDATE schedule SET Total_bill={0} WHERE Total_bill={1}'.format(r2[0], r1[0])) 
        con.commit() 
    print("Data updated successfully") 

def delete_details(): 
    print(""" 
                         1. SCHEDULE DATE 
                         2. SCHEDULE TIME 
                         3. SERVICES 
    """) 
    ch = input('Enter the column to be deleted from above list of columns:') 
    if ch == '1': 
        d = input('Enter record with date to be deleted:') 
        so = "SELECT * FROM schedule WHERE service_date='{}'".format(d) 
        cur.execute(so) 
        row = cur.fetchall() 
        for i in row: 
            print(i) 
        if len(row) == 0: 
            print("Sorry, no such record exists") 
        else: 
            st = "DELETE FROM schedule WHERE service_date='{}';".format(d) 
            cur.execute(st) 
            con.commit() 
            print("Data deleted successfully") 
    elif ch == '2': 
        d = input('Enter record with time slot to be deleted:') 
        so = "SELECT * FROM schedule WHERE Time_service='{}'".format(d) 
        cur.execute(so) 
        row = cur.fetchall() 
        for i in row: 
            print(i) 
        if len(row) == 0: 
            print("Sorry, no such record exists") 
        else: 
            st = "DELETE FROM schedule WHERE Time_service='{}';".format(d) 
            cur.execute(st) 
            con.commit() 
            print("Data deleted successfully") 
    elif ch == '3': 
        d = input('Enter record with service to be deleted:') 
        so = "SELECT * FROM schedule WHERE service='{}'".format(d) 
        cur.execute(so) 
        row = cur.fetchall() 
        for i in row: 
            print(i) 
        if len(row) == 0: 
            print("Sorry, no such record exists") 
        else: 
            st = "DELETE FROM schedule WHERE service='{}';".format(d) 
            cur.execute(st) 
            con.commit() 
            print("Data deleted successfully") 

def schedule(u): 
    print(' SERVICES MENU') 
    cur.execute('SELECT * FROM services;') 
    row = cur.fetchall() 
    for i in row: 
        print(i) 
    cont = True 
    tb = 0 
    while cont: 
        ser = input('Enter service to be scheduled:') 
        date = input('Enter date of service') 
        cur.execute('SELECT curdate();') 
        r = cur.fetchone() 
        print('Current date is', r) 
        time = input('Enter time when you need service:') 
        cur.execute('SELECT rates FROM services WHERE service_name="{}"'.format(ser)) 
        bill = cur.fetchone() 
        tb += bill[0] 
        cur.execute('''INSERT INTO schedule 
        VALUES('{0}', '{1}', '{2}', '{3}', {4})'''.format(u, ser, date, time, bill[0])) 
        l = input('Do you want to continue?(y/n)') 
        if l == 'y':
            cont = True 
        else: 
            cont = False 
    print('Total bill is ', tb) 
    con.commit() 

def module(user): 
    while True: 
        print('''OPERATIONS MENU 
                    1. Display history 
                    2. Schedule a new service 
                    3. Update schedule 
                    4. Delete record from schedule 
                    5. Sign out''') 
        ch = int(input('Enter your choice for execution:')) 
        if ch == 1: 
            print('History') 
            cur.execute('SELECT * FROM schedule') 
            row = cur.fetchall() 
            if len(row) == 0: 
                print('''This table is empty!!! 
                        No schedule there''') 
            else: 
                for i in row: 
                    print(i) 
        elif ch == 2: 
            schedule(user) 
        elif ch == 3: 
            update(user) 
        elif ch == 4: 
            delete_details() 
        elif ch == 5: 
            print('Hope you had a good experience!!!') 
            f = False 
            break 
        else: 
            print('Invalid choice') 
            print('Please try again') 
            continue 

def login(): 
    print(""" 
                   ============================== 
                    {{LOGIN }}   
                   ============================== 
    """) 
    un = input("Enter the username:") 
    ps = input("Enter the password:") 

    cur.execute("SELECT user_name FROM customer WHERE user_name='{0}';".format(un)) 
    l = cur.fetchall() 
    if len(l) == 0: 
        print('Username does not exist') 
    else: 
        cur.execute("SELECT passwd FROM customer WHERE user_name='{0}'; ".format(un)) 
        l2 = cur.fetchall() 
        for i in l2: 
            a = list(i) 
            if a[0] == str(ps): 
                print('Logged in successfully') 
                module(un) 
            else: 
                print('Incorrect login. Please try again!!') 

def sign_in(): 
    print(""" 
                 ==================================== 
                 PLEASE REGISTER YOURSELF 
                 ==================================== 
    """) 
    user = input("Enter your preferred username:") 
    passwd = input("Enter your preferred password (Password should be strong):") 
    address = input('Enter your address:') 
    ph = input('Enter your phone number:') 
    em = input("Enter your email ID:") 
    cur.execute("""INSERT INTO customer 
    VALUES('{u}', '{p}', '{a}', '{f}', '{e}');""".format(u=user, p=passwd, a=address, f=ph, e=em)) 
    con.commit() 

    print(""" 
                  =============================== 
                  REGISTERED SUCCESSFULLY 
                  =============================== 
    """) 
    login() 

# Main
print(""" 
             ==================================== 
              WELCOME TO HOME SERVICE AND PERSONAL CARE  
             ==================================== 
                         -By Arisha Chadha
""")         
import mysql.connector as sq 
con = sq.connect(host='localhost', user='root', passwd='arisha', charset="utf8") 
if con.is_connected(): 
    print('Successfully connected to MySQL') 
cur = con.cursor() 
cur.execute('CREATE DATABASE IF NOT EXISTS ps') 
cur.execute('USE ps') 
cur.execute('CREATE TABLE IF NOT EXISTS customer (user_name VARCHAR(20) PRIMARY KEY, passwd VARCHAR(10) UNIQUE, address VARCHAR(50), ph_no VARCHAR(20), email VARCHAR(30));') 
cur.execute('CREATE TABLE IF NOT EXISTS services (service_name VARCHAR(20) PRIMARY KEY, rates INT(5));') 
cur.execute('CREATE TABLE IF NOT EXISTS schedule (user VARCHAR(20), service VARCHAR(50), service_date VARCHAR(20), Time_service VARCHAR(10), Total_bill INT(10))') 
cur.execute('SELECT * FROM services') 
l = cur.fetchall() 
if len(l) == 0: 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('AC servicing', 750);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Plumbing', 350);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Makeup', 550);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Washing Machine Service', 500);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Wall painting', 150);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Carpentry', 250);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Facial', 600);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Manicure', 450);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Pedicure', 600);''') 
    cur.execute('''INSERT INTO ps.services (`service_name`, `rates`) VALUES ('Massage', 500);''') 
con.commit() 

p = True 
while p: 
    print(""" 
                MAIN MENU 
                1. SIGN IN (LOGIN) 
                2. SIGN UP (REGISTER) 
                3. Exit 
    """) 
    ch = input('Enter your choice:') 
    if ch == '1': 
        login() 
    elif ch == '2': 
        sign_in() 
    elif ch == '3': 
        break 
    else:
        print('Invalid choice. Re-enter') 

con.close() 
print('Thank you!!!') 
print('Hope you had a nice time with us')
