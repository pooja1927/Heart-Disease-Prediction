import sqlite3
db=sqlite3.connect('heart.db')

query="""CREATE TABLE data(
age int,
anaemia int,
creatinine_phosphokinase int,
diabetes int,
ejection_fraction int,
high_blood_pressure int,
platelets int,
serum_creatinine int,
serum_sodium int,
sex int,
smoking int,
time int,
);"""

cur=db.cursor()

cur.execute(query)

query2="""INSERT INTO user (id,LastName,FirstName,Address)
VALUES(?,?,?,?);"""
cur.execute(query2, ())

db.commit()
db.close()