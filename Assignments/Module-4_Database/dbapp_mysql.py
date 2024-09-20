import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdatabase')
    print("Database Connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()

#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data

"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('hitesh','surat'),('prasiddh','ahmedabad'),('mahesh','wadhwan')"

try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set name='pratik', city='rajkot' where id=5"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

#Show Data

select_data="select * from studinfo"
try:
    cr.execute(select_data)
    #data=cr.fetchall()
    #data=cr.fetchmany(3)
    data=cr.fetchone()
    print(data)
except Exception as e:
    print(e)