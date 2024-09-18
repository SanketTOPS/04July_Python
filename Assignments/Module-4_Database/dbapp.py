import sqlite3

try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database created/connected!")
except Exception as e:
    print(e)


#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text, city text)"
try:
    dbcon.execute(tbl_create)
    print("Table crated!")
except Exception as e:
    print(e)


#Insert Data

insert_data=f"insert into studinfo(name,city)values('nirav','baroda'),('ashok','surat'),('hitesh','navsari'),('mitesh','gondal'),('prsiddh','ahmedabad')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)