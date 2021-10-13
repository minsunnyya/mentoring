import pymysql

conn = pymysql.connect(host="database-2.clvwtbd3pi7c.ap-northeast-2.rds.amazonaws.com",
                       user="admin",
                       password="12345678",
                       db="mentoring01",
                       charset="utf8"

)


# insert
# curs = conn.cursor()
# sql = """insert into User(id, name)
#         values (%s, %s)"""
# curs.execute(sql, ('hello', 'moon'))
# curs.execute(sql, ('bye', 'star'))
# curs.execute(sql, ('long', 'sun'))
# conn.commit()

# update
# curs = conn.cursor()
# sql = """update User set id='goodmorning' where id='hello'"""
# curs.execute(sql)
# conn.commit()

# delete
curs = conn.cursor()
sql = """delete from User where name=%s"""
curs.execute(sql, "test1")
conn.commit()


sql2 = "select * from User order by age"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
conn.close()
exit()


curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from User where name=%s" #select기능
curs.execute(sql, 'naver')
rows = curs.fetchall()
print(rows)


for row in rows:
    print(row)
    print(row['name'], row['id'], row['age'])
