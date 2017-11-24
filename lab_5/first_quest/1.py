import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect(
    host='localhost',
    user='Victor',
    passwd='12345678',
    db='first_db'
)

c = db.cursor()

c.execute('INSERT INTO myapp_film (id, name, description, country, author) VALUES (%s, %s, %s, %s, %s);', (2, 'Fight Club', 'Was create by Palauhnik', 'USA', 'Chuck Palauhnik'))

db.commit()

c.execute('SELECT * FROM myapp_film;')

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()