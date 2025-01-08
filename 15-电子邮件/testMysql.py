# 1. 导入mysql驱动
import mysql.connector
# 2. 创建连接
try:
    conn = mysql.connector.connect(
        host='localhost',       # 主机名（默认为 localhost）
        user='root',            # 用户名
        password='123456',      # 密码
        database='my_db_01'     # 数据库名称
    )
    print("连接成功")
except mysql.connector.Error as err:
    print(f"连接失败: {err}")
    exit()