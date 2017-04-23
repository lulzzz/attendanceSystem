from flask import Flask, render_template, send_from_directory
import logic.dbStreamer as dbStreamer
import time

app = Flask(__name__, static_url_path='')

@app.route('/')
def homepage():
	card_UID = dbStreamer.read_data_from_istream("card_id")
	time = dbStreamer.read_data_from_istream("time")
	return render_template("index.html", title='SimpleAttendanceSystem', cardUID=card_UID, Time=time)

@app.route('/js/<path:path>')
def sendJS(path):
	return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def sendCSS(path):
	return send_from_directory('static/css', path)

if __name__ == "__main__":
	app.run()
