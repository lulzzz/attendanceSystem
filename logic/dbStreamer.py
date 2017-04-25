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
		if args == "time":
			cur.execute("select time from istream;")
			return cur.fetchall()

def calc_users():
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute("select count(name) from users")
		return cur.fetchall()

def compoare_users_and_istream():
	conn = connect()
        cur = conn.cursor()
        with cur:
                cur.execute("select name, users.card_id, time, branch from istream join users on istream.card_id=users.card_id")
		return cur.fetchall()

def complete_view_table():
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute("select name, users.card_id, branch, time from istream join users on istream.card_id=users.card_id order by time")
		data = cur.fetchall()
	res = {}
	for row in data:
		if row[0] not in res:
			res[row[0]] = {'card_id': row[1], 'branch': row[2], 'times': []}
	
	for user in res:
		for row in data:
			if row[0] == user:
				res[row[0]]['times'].append(row[3])
		
	return res

def return_all_users():
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute("select name from users;")
		return cur.fetchall()

def add_user(name, card_id, branch):
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute('''insert into users (name, card_id, branch) values ("%s", "%s", "%s");''' % (name, card_id, branch), plain_query=True)

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
		cur.execute('''insert into istream (card_id, time) values ("%s", "%s");''' % (card_id, timestamp), plain_query=True)

print complete_view_table()

#add_user("TestUser", "123456789", "Praha")
#add_user("TestUser1", "987654321", "Pardubice")
#add_user("TestUser2", "521346789", "Brno")
#add_user("TestUser3", "752822764", "Holesovice")

#save_iStream("123456789")
#compoare_users_and_istream()
