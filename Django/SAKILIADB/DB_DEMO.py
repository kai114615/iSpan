import MySQLdb

class Category():
    def __init__():
        pass

    def categories():
        # 第一步 建立連線
        connection = MySQLdb.connect(
            host='localhost',
            database='sakila',
            user='root',
            password='Kai114615'
        )
        if not connection:
            return None


        # 第二步 SQL語法
        sql = 'SELECT * FROM category'

        # 第三步 建立cursor語法執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)

                    # 第三步之一 讀取資料
                    results = cursor.fetchall()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤: {e}")
                    return None



