import pymysql

conn = pymysql.connect(host="database-2.clvwtbd3pi7c.ap-northeast-2.rds.amazonaws.com",
                       user="admin",
                       password="12345678",
                       db="mentoring01",
                       charset="utf8"
                       )


class MyTbl:
    def __init__(self):
        pass

    def getTbls(self):
        ret = []
        db = pymysql.connect(host='database-2.clvwtbd3pi7c.ap-northeast-2.rds.amazonaws.com',
                             user='admin',
                             db='mentoring01',
                             password='12345678',
                             charset='utf8')
        curs = db.cursor()

        sql = "select * from User";
        curs.execute(sql)

        rows = curs.fetchall()
        for e in rows:
            temp = {'id': e[0], 'name': e[1], 'age': e[2]}
            ret.append(temp)

        db.commit()
        db.close()
        return ret

    def insEmp(self, id, name, age):
        db = pymysql.connect(host='database-2.clvwtbd3pi7c.ap-northeast-2.rds.amazonaws.com',
                             user='admin',
                             db='mentoring01',
                             password='12345678',
                             charset='utf8')
        curs = db.cursor()

        sql = '''insert into emp (id, name, age) values(%s,%s,%s)'''
        curs.execute(sql, (id, name, age))
        db.commit()
        db.close()

    def updEmp(self, id, name, age):
        db = pymysql.connect(host='database-2.clvwtbd3pi7c.ap-northeast-2.rds.amazonaws.com',
                             user='admin',
                             db='mentoring01',
                             password='12345678',
                             charset='utf8')
        curs = db.cursor()

        sql = "update User set id=%s, name=%s, age=%s where User=%s"
        curs.execute(sql, (id, name, age))
        db.commit()
        db.close()

    def delEmp(self, empno):
        db = pymysql.connect(host='database-2.clvwtbd3pi7c.ap-northeast-2.rds.amazonaws.com',
                             user='admin',
                             db='mentoring01',
                             password='12345678',
                             charset='utf8')
        curs = db.cursor()

        sql = "delete from User where age=7"
        curs.execute(sql, User)
        db.commit()
        db.close()


if __name__ == '__main__':
    #MyTbl().insEmp('aaa', 'bb', 'cc', 'dd')
    #MyTbl().updEmp('aa', 'dd', 'dd', 'aa')
    #MyTbl().delEmp('aaa')
    Userlist = MyTbl().getTbls();
    print(Userlist)