import sqlite3

try:
    dbcon=sqlite3.connect("topsdb.db")
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name varchar(20),city varchar(20))"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data

"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('hitesh','surat'),('prasiddh','ahmedabad'),('mahesh','wadhwan')"

try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set name='pratik', city='rajkot' where id=9"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=10"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


#Show Data
cr=dbcon.cursor()
select_data="select * from studinfo"
try:
    cr.execute(select_data)
    #data=cr.fetchall()
    data=cr.fetchmany(3)
    #data=cr.fetchone()
    print(data)

    """for i in data:
        print(i[1])"""
except Exception as e:
    print(e)

