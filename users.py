from data import db
import hashlib
from passlib.hash import sha512_crypt as sha
from datetime import datetime

class users:

    def __init__(self, username, password):
        self.db = db('root', 'localhost', 'Shashank$26', 'customer_acq')
        self.username = username
        self.secret = password
        self.authenticated = False
        self.auth()
        self.get_details()
#self.get_devices()

    def auth(self):
        # this is the place where user will get authenticated
        try:
            query = 'select password from users where username = "{0}"'.format(self.username)
            self.db.cursor.execute(query)
            output = self.db.cursor.fetchall()
            if sha.verify(self.secret, output[0][0]):
                self.authenticated = True

                query = 'update users set last_login = now() where username = "{0}";'.format(self.username)
                self.db.cursor.execute(query)
                self.db.db.commit()

                return True
            else:
                self.authenticated = False
                return False

        except Exception as e:
            print("[ERROR!]")
            print(e)

    def get_details(self):

        try:
            if self.authenticated:
                query = 'select * from users where username = "{0}"'.format(self.username)
                self.db.cursor.execute(query)
                output = self.db.cursor.fetchall()
                output = output[0]
                self.first = output[2]
                self.last = output[3]
                self.email = output[4]
                self.phone = output[5]
                self.last_login = output[6].strftime("%d-%b-%Y (%H:%M:%S.%f)")
                self.api = output[7]
                return True

            else:
                print("User not logged in!")
                return False

        except Exception as e:
            print("ERROR!")
            print(e)