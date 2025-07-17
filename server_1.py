import pymysql

class SERVER_2:
    def __init__(self, data):
        self.my_db = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='load_balancer'
        )
        self.data = data
        print(data, "in server 1")
        self.write_in_database()
        self.my_db.close()  # Close only after everything is done

    def write_in_database(self):
        try:
            with self.my_db.cursor() as cursor:
                sql = "INSERT INTO server_1 (data) VALUES (%s)"
                cursor.execute(sql, (self.data,))
                self.my_db.commit()

                ask = input("Display the data from the server? y/n: ")
                if ask.lower() == 'y':
                    self.display_data()
        except Exception as e:
            print("Error while writing to DB:", e)

    def display_data(self):
        try:
            with self.my_db.cursor() as cursor:
                sql = "SELECT * FROM server_1"  # ✅ Correct table name
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    print(row)
        except Exception as e:
            print("Error while reading from DB:", e)
