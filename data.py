import mysql.connector

class db:
    def __init__(self, user, host, password, database):
         try:
             self.db = mysql.connector.connect(user=user, host=host, password=password, database=database)
             self.cursor = self.db.cursor()
             print('[Result] Database Connected')

         except Exception as a:
            print('[error] error connecting to database')
            print(a)
    def user(self, username, api):
        try:
            query = "select * from users where username='{}' and api_key='{}'".format(username, api)
            self.cursor.execute(query)
            output = self.cursor.fetchall()
            return output[0]
        except Exception as e:
            print('[error] ' + e)