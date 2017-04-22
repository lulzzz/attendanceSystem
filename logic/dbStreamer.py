import oursql

def connect(db_name):
	conn = oursql.connect(host="localhost", user="attendanceSystem", passwd="somerandomgiberlish", db=db_name)
	return conn

def read(db_name):
	conn = connect(db_name)
	cur = conn.cursor()
	with cur:
		cur.execute("select * from users;")
		data = cur.fetchall()
		print data

def add_user(name, card_id):
	conn = connect("attendanceSystem")
	cur = conn.cursor()
	with cur:
		cur.execute('''insert into users (id, name, card_id) values (NULL, "%s", "%s");''' % (name, card_id), plain_query=True)

def save_iStream(card_id, time):
	conn = connect("attendanceSystem")
	cur = conn.cursor()
	with cur:	
		cur.execute('''insert into istream (id, card_id, time) values (NULL, "%s", "%s");''' % (card_id, time), plain_query=True)

read("attendanceSystem")
add_user('Lukas', '2312312')
