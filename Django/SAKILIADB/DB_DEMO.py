import MySQLdb

class Category():
    def __init__():
        pass

    def categories():
        connection = MySQLdb.connect(
            host='localhost',
            database='sakila',
            user='root',
            password='kai114615'
        )
        if not connection:
            return None
        

        sql = 'SELECT * FROM category'

        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤: {e}")
                    return None