# Функции для работы с базой данных
import pandas as pd
from mysql.connector import connect, Error

class My_db:
    def __init__(self,db, host, user):
        self.db = db
        self.host = host
        self.user = user
        self.con = self.connect()
        self.cursor = self.con.cursor()

    def connect(self):
        try:
            connection = connect(
                host=self.host,
                user=self.user,
                database=self.db,
            )
            return connection
        except Error as e:
            print(e)

    def add_light(self,id, light):
        insert_query = f"""
        INSERT INTO light(ID_SENSOR, light)
        VALUES ({id}, {int(light)})
        """
        self.cursor.execute(insert_query)
        self.con.commit()

    def do_request(self, request):
        self.cursor.execute(request)
        col_names = [col[0] for col in self.cursor.description]
        return pd.DataFrame(self.cursor.fetchall(), columns=col_names)

