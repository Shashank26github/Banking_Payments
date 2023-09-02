from passlib.hash import sha512_crypt as sha
password = sha.hash("pass")
print(password)
from data import db

mydb = db('root', 'localhost', 'Shashank$26', 'customer_acq')
query = "update users set password = '{}' where username = 'Shashank'".format(password)

mydb.cursor.execute(query)
mydb.db.commit()