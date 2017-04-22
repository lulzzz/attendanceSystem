from flask import Flask, render_template
import logic.getData as getData
import logic.dbStreamer as dbStreamer

app = Flask(__name__)

@app.route('/')
def homepage():
    card_UID = dbStreamer.getUID()
    return render_template("index.html", title='SimpleAttendanceSystem', cardUID=card_UID)

if __name__ == "__main__":
    app.run()
