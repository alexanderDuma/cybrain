from flask import Flask, render_template,request
import pymongo
import DBmanager
from Entities import Target,Adversary,Event

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["cybrain"]
users = db['users']

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=['GET', 'POST'])
def login():
    req = request
    username = request.form['username']
    password = request.form['pwd']
    user = users.find_one({'username':username})
    if not user:
        return "User not exist!"
    if user['password'] == password:
        return render_template("event_feed.html")
    else:
        return "Authentication Failed!"

@app.route("/feed_event",methods=['GET', 'POST'])
def feed_event():
    """feed new event(report) to the data base"""
    #create adversary
    origin = request.form['adv_origin']
    organ = request.form['adv_orga']
    camp = request.form['adv_camp']
    adversary = Adversary(origin,organ,camp)

    #create target
    sector = request.form['trgt_sector']
    name = request.form['trgt_name']
    is_isr = request.form['trgt_israeli']
    if is_isr=='true':
        is_isr = True
    else:
        is_isr = False

    trgt = Target(sector, name, is_isr)

    #create the event
    date = request.form['date']
    ref = request.form['ref']
    status = 'Report'
    details = request.form['details']
    type = request.form['event_type']
    reporter = request.form['reporter']
    new_event = Event(date, adversary, trgt, ref, status, details, type, reporter)
    try:
        ack = DBmanager.insertNewEvent(new_event)
        if ack:
            return "<script>alert('Success Event Feed!')</script>"
        else:
            return "<script>alert('XXX Event Feed Failed! XXX')</script>"
    except Exception as e:
        return "<script>alert('XXX Event Feed Failed! XXX')</script>"


@app.route("/feed")
def feed():
    return render_template("event_feed.html")

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=80)