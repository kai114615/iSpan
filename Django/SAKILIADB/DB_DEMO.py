import MySQLdb


class Category():
    def __init__():
        pass

    def create_connection():
        # 第一步 建立連線(重複相同段)
        try:
            connection = MySQLdb.connect(
                host='localhost',
                database='sakila',
                user='root',
                password='Kai114615'
            )
            return connection
        except MySQLdb.MySQLError as e:
            print(f"資料讀取錯誤: {e}")
            return None

    # 讀取所有資料

    def category_all():
        # 第一步 建立連線
        connection = Category.create_connection()
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

    # 讀取單一資料
    def category_single(id):
        # 第一步 建立連線
        connection = Category.create_connection()
        if not connection:
            return None

        # 第二步 SQL語法
        sql = f'SELECT * FROM category where category_id=%s'

        # 第三步 建立cursor語法執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql, (id,))

                    # 第三步之一 讀取資料
                    results = cursor.fetchone()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤: {e}")
                    return None

    # 新增資料
    def category_create(category_name):
        connection = Category.create_connection()
        if not connection:
            return None

        # 第二步 新增SQL資料語法
        sql = 'insert into category (name) values (%s)'

        # 第三步 建立cursor語法執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql, (category_name,))

                    # 第三步之二 讀取資料
                    cursor.commit()
                    return cursor.rowcount
                except MySQLdb.MySQLError as e:
                    print(f"資料新增失敗: {e}")
                    return None
