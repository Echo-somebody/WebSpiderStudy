import pymysql
import logging
logging.basicConfig(level=logging.INFO,format='line:%(lineno)d %(message)s')
'''
1,安装pymysql
'''
'''
2,连接数据库   host port user password
'''
db = pymysql.connect(host='localhost',user='root',password='dove2021.',port=3306)   #声明MySQL连接对象
cursor = db.cursor()   #调用cursor方法获得MySQL操作游标
cursor.execute('SELECT VERSION()')  #利用游标来执行SQL语句
data = cursor.fetchone() #调用fetchone()方法获得第一条数据
logging.info(data)
'''
3,创建数据库
'''
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
cursor.execute('SHOW DATABASES')
data = cursor.fetchall() #调用fetchall()方法获得所有数据
logging.info(data)
'''
4,创建表
'''
cursor.execute('USE spiders')
sql = 'CREATE TABLE IF NOT EXISTS students ' \
      '(id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
cursor.execute('SHOW TABLES')
data = cursor.fetchall() #调用fetchall()方法获得所有数据
logging.info(data)
'''
5,插入数据  SQL语句字典动态构造
'''
# id = '202120001'
# user = 'Echo'
# age = 18
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()

data = {
    'id':'20001201',
    'name':'sky',
    'age':20
}
table = 'students'
keys = ','.join(data.keys()) #连接字符串数组，返回一个以分隔符sep连接的各个元素后生成的字符串
values = ','.join(['%s'] * len(data))
logging.info(keys)
logging.info(values)
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
logging.info(sql)
logging.info(data.keys())
logging.info(data.values())
try:
    cursor.execute(sql,tuple(data.values()))
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT * from students')
data = cursor.fetchall()
logging.info(data)
'''
6，更新数据
'''
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql,(10,'Echo'))
    db.commit()
except:
    db.rollback()
cursor.execute('SELECT * from students')
data = cursor.fetchall()
logging.info(data)

data = {
    'id':'20120094',
    'name':'Bob',
    'age':21

}
logging.info('+ id +')
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = f'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([f' {key}=%s'.format(key=key) for key in data])
sql += update
logging.info(sql)
logging.info(tuple(data.values())*2)
try:
    if cursor.execute(sql,tuple(data.values())*2):
        logging.info('successful')
        db.commit()
except:
    db.rollback()

'''
7,删除数据
'''
table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

'''
8,查询数据
'''


db.close()



