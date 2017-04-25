from flask import Flask, render_template, send_from_directory
import logic.dbStreamer as dbStreamer
import logic.time_parser as tp
import time

app = Flask(__name__, static_url_path='')

@app.route('/')
def homepage():
	info = dbStreamer.compoare_users_and_istream()

	users = dbStreamer.return_all_users()
	print users
	cvt = dbStreamer.complete_view_table()
	data = {}
	#data = { row1: [user, card_id time] }
	
	user_len = dbStreamer.calc_users()
	user_len = user_len[0][0]

	for user in users:
        	user = user[0]
		
		day_time = tp.calc_day_time(cvt[user]['times'][0], cvt[user]['times'][1], cvt[user]['times'][2], cvt[user]['times'][3])

		time1 = tp.return_time_in_normal_form(str(cvt[user]['times'][0]))
		time2 = tp.return_time_in_normal_form(str(cvt[user]['times'][1]))
		time3 = tp.return_time_in_normal_form(str(cvt[user]['times'][2]))
		time4 = tp.return_time_in_normal_form(str(cvt[user]['times'][3]))

		
			
        	data[user] = [ str(user), str(cvt[user]['card_id']), str(cvt[user]['branch']), time1, time2, time3, time4, day_time ]
		print data

	return render_template("index.html", title='SimpleAttendanceSystem', info=info, cvt=data, user_len=int(user_len))

@app.route('/js/<path:path>')
def sendJS(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def sendCSS(path):
	return send_from_directory('static/css', path)

if __name__ == "__main__":
	app.run()
