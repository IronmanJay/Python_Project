from pymysql import connect

conn = connect(host='localhost',port=3306,user='root',password='990929',database='test',charset='utf8')

cursor = conn.cursor()

cursor.execute("select * from user;")

# cursor.fetchone()
all_data = cursor.fetchall()

for temp in all_data:
    print(temp)