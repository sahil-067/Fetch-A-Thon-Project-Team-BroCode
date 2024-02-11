import mysql.connector
import datetime
from tabulate import tabulate

db = input("Enter name of your database :")

mydb=mysql.connector.connect(host='localhost',user='root',passwd='sahil9087')
mycursor=mydb.cursor()
sql="CREATE DATABASE if not exists "+db
mycursor.execute(sql)
mydb.commit()
print("Database created successfully..")
mycursor = mydb.cursor()
mycursor.execute('use '+db)
print("Enter yours status : \n1.USER \n2.EMPLOYEE \n3.ADMIN")
xyz=int(input("Enter your choice:"))
if xyz==1:
    #user data
    tablename2 = input ("Name of the table to be created :")
    query = "create table if not exists "+tablename2+"\
    (Mobile_No integer(10) primary key,\
    Source varchar(12),\
    Destination varchar(12))"
    print("Table "+tablename2+" created successfully...")
    mycursor.execute(query)
elif xyz==2:
    #bus count
    tablename3 = input ("Name of the table to be created :")
    query = "create table if not exists "+tablename3+"\
    (count integer(2) default 0,\
    Source varchar(12),\
    Destination varchar(12))"
    print("Table "+tablename3+" created successfully...")
    mycursor.execute(query)
elif xyz==3:
    #bus data
    tablename4 = input ("Name of the table to be created :")
    query = "create table if not exists "+tablename4+"\
    (ID varchar(16) primary key,\
    Source varchar(12),\
    Destination varchar(12))"
    print("Table "+tablename4+" created successfully...")
    mycursor.execute(query)
else:
    print("INVALID CHPICE !!!")

while True:
    print('\n\n\n')
    print("*"*159)
    print('\t\t\t\ti. Adding user records')
    print('\t\t\t\t2. For displaying record of all the users')
    print('\t\t\t\t3. For displaying record of a particular user')
    print('\t\t\t\t4. For deleting records of all users')
    print('\t\t\t\t5. For deleting a record of a particular userr')
    print('\t\t\t\t6. For modification in a record')
    print('\t\t\t\t10.For exit')
    print('Enter choice...', end='' )
    choice = int(input())
    if choice==1:
        try:
            print("Enter Customer information...")
            ano=int(input("Enter mobile number :"))
            src=input("Enter source :")
            dest=int(input("Enter destination :"))
            rec=(ano,src,dest)
            query='insert into '+tablename2+' values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,rec)
            mydb.commit()
            print("Record added successfully !")
        except Exception as e:
            print("Something went wrong !!!")

    elif choice==2:
        try:
            query='select * from '+tablename2
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['Mobile_No','Source','Destination'],tablefmt='fancy_grid'))
            '''myrecords=mycursor.fetchall()
            For rec in myrecords:
            print(rec)'''
        except:
            print("Something went wrong !!!")

    elif choice==3:
        try:
            en=input("Enter mobile no. of the record to be displayed...")
            query='select * from '+tablename2+' where Mobile_No='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of Mobile no.:"+en)
            print(myrecord)
            y=mycursor.rowcount
            if y==-1:
                print("Nothing to display")
        except:
            print("Something went wrong !!!")

    elif choice==4:
        try:
            ch=input("Do you want to delete all the records [Y/N] :")
            if ch.upper=='Y':
                mycursor.execute('Delete from '+tablename2)
                mydb.commit()
                print("All the records are deleted...")
        except:
            print("Something went wrong !!!")

    elif choice==5:
        try:
            en=input("Enter mobile no. of the record to be deleted...")
            query='delete from '+tablename2+' where Mobile_no='+en
            mycursor.execute(query)
            mydb.commit()
            x=mycursor.rowcount
            if x>0:
                print("Deletion done")
            else:
                print("Something went wrong !!!")
        except:
            print("Something went wrong !!!")

    elif choice==6:
        try:
            en=input("Enter Mobile no. of the record to be modified...")
            query='select * from '+tablename2+' where Mobile_No='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            x=mycursor.rowcount
            if x==-1:
                print("Mobile no. not exist")
            else:
                mname=myrecord[0]
                msrc=myrecord[1]
                mdist=myrecord[2]
                print("Mobile No.  :",myrecord[0])
                print("Source         :",myrecord[1])
                print("Destination    :",myrecord[2])
                print('-'*15)
                print("Type value to modify below or just press enter for no change")
                p=input("Enter mobile")
                if len(p)>0:
                    uName=p
                q=input("Enter source")
                if len(q)>0:
                    usrc=q
                r=input("Enter destination")
                if len(r)>0:
                    udest=r
                query='update '+tablename2+' set Mobile_No= '+" ' "+uName+" ' "+' , '+' Source= '+" ' "+usrc+" ' "+' , '+' Destination= '+" ' "+udest+" ' "+' where Mobile_No= '+en
                mycursor.execute(query)
                mydb.commit()
                print('Record , modified')
        except:
            print("Something went wrong !!!")

    elif choice==10:
        break
    else:
        print("Wrong Choice")
