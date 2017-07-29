import mysql.connector
conn =mysql.connector.connect(host='rm-uf69h590tre967spro.mysql.rds.aliyuncs.com', port=3306, user='root', passwd='Guwei@123456',db='guwei_test')
cur = conn.cursor()
cur.execute("SELECT * FROM user")
for r in cur.fetchall():
    print(r)
cur.close()
conn.close()