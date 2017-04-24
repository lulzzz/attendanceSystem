from flask import Flask, render_template, send_from_directory
import logic.dbStreamer as dbStreamer
import time

app = Flask(__name__, static_url_path='')

@app.route('/')
def homepage():
	info = dbStreamer.compoare_users_and_istream()

	users = dbStreamer.return_all_users()
	cvt = dbStreamer.complete_view_table()
	data = {}
	#data = { row1: [user, card_id time] } 
	for user in users:
        	user = user[0]
        	data[user] = [ str(user), str(cvt[user]['card_id']), str(cvt[user]['times'][0]) ]
	print data
	
	return render_template("index.html", title='SimpleAttendanceSystem', info=info, cvt=data)

@app.route('/js/<path:path>')
def sendJS(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def sendCSS(path):
	return send_from_directory('static/css', path)

if __name__ == "__main__":
	app.run()
