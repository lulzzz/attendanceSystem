import oursql
import yaml
import os
import datetime

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

def read_data_from_istream(args):
	conn = connect()
	cur = conn.cursor()
	with cur:
		if args == "card_id":
			cur.execute("select card_id from istream;")
			return cur.fetchall()
		elif args == "time":
			cur.execute("select time from istream;")
			return cur.fetchall()

def add_user(name, card_id):
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute('''insert into users (id, name, card_id) values (NULL, "%s", "%s");''' % (name, card_id), plain_query=True)

def save_iStream(card_id):
	conn = connect()
	now = datetime.datetime.now()
	year = str(now.year)
	month = now.month
	if month < 10:
		month = "0" + str(now.month)
	else:
		month = str(now.month)
	day = now.day
	if day < 10:
		day = "0" + str(day)
	else:
		day = str(day)
	hour = now.hour
	if hour < 10:
		hour = "0" + str(hour)
	else:
		hour = str(hour)
	minute = now.minute
	if minute < 10:
		minute = "0" + str(minute)
	else:
		minute = str(minute)
	second = now.second
	if second < 10:
		second = "0" + str(second)
	else:
		second = str(second)
	timestamp = year + month + day + hour + minute + second
	cur = conn.cursor()
	with cur:	
		cur.execute('''insert into istream (id, card_id, time) values (NULL, "%s", "%s");''' % (card_id, timestamp), plain_query=True)

#add_user("TestUser", "123456789")
#save_iStream("123456789")
