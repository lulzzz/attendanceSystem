import oursql
import yaml
import os

__dir__ = os.path.dirname(__file__)
config = yaml.safe_load(open(__dir__ + '/../config.yaml'))

def connect():
	conn = oursql.connect(host=config['DB_HOST'], user=config['DB_USER'], passwd=config['DB_PASS'], db=config['DB_NAME'])
	return conn

def read(tablename):
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute("select * from %s;" % (tablename))
		data = cur.fetchall()
		return data

def add_user(name, card_id):
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute('''insert into users (id, name, card_id) values (NULL, "%s", "%s");''' % (name, card_id), plain_query=True)

def save_iStream(card_id, time):
	conn = connect()
	cur = conn.cursor()
	with cur:	
		cur.execute('''insert into istream (id, card_id, time) values (NULL, "%s", "%s");''' % (card_id, time), plain_query=True)

#add_user("TestUser", "123456789")
#save_iStream("123456789", "12:45")
#print(read("istream"))
