from flask import Flask, redirect, url_for, request
import mysql.connector
import os

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="red5PRO@action"
)
mycursor = mydb.cursor(buffered=True)
mycursor.execute("use alertsDB;")


@app.route('/add',methods = ['POST'])
def add():
    alert_json = request.json
    '''ts = data['ts']
    te = data['te']
    protocol = data['protocol']
    source_ip = data['source_ip']
    destination_ip = data['destination_ip']
    td = data['td']
    history = data['history']
    service = data['service']
    anomaly_score = data['anomaly_score']'''
    mycursor.execute("insert into alert (ts, te, protocol, source_ip, destination_ip, history, td, service, anomaly_score) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (alert_json['ts'], alert_json['te'], alert_json['protocol'], alert_json['source_ip'], alert_json['destination_ip'], 
                    alert_json['history'], alert_json['td'], alert_json['service'], alert_json['anomaly_score']))
    mydb.commit()



    return "Just added alert with ts: %s into DB" %(alert_json['ts'])

@app.route('/')
def hello():
    return "hello world\n"


if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port))

