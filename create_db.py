import sqlite3

db = sqlite3.connect("codefest.db")

# db.execute("create table abcd(col1 integer)")
# db.execute("insert into abcd values(2)")
# db.execute("insert into abcd values(3)")
# db.execute("insert into abcd values(4)")
# db.commit()
cursor=db.cursor()
cursor.execute("select * from abcd")
q = db.execute("select * from abcd")
print(q)
for item in q:
	# print(item.fetchone
	print(item[0])

