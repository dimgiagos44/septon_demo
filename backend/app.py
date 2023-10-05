from flask import Flask, redirect, url_for, request
import mysql.connector
import os
from datetime import datetime
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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
    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    alert_json['created_at'] = now
    '''ts = data['ts']
    te = data['te']
    protocol = data['protocol']
    source_ip = data['source_ip']
    destination_ip = data['destination_ip']
    td = data['td']
    history = data['history']
    service = data['service']
    anomaly_score = data['anomaly_score']'''
    mycursor.execute("insert into alert (ts, te, protocol, source_ip, destination_ip, history, td, service, anomaly_score, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (alert_json['ts'], alert_json['te'], alert_json['protocol'], alert_json['source_ip'], alert_json['destination_ip'], 
                    alert_json['history'], alert_json['td'], alert_json['service'], alert_json['anomaly_score'], alert_json['created_at']))
    mydb.commit()
    return "Just added alert with ts: %s into DB" %(alert_json['ts'])

@app.route('/get_alerts', methods=['GET'])
def get():
    #mycursor.execute("SELECT * FROM alert WHERE alert.created_at > now() - interval 5 minute ORDER BY ID DESC LIMIT 4")
    mycursor.execute("SELECT * FROM alert ORDER BY ID DESC LIMIT 4")
    records = mycursor.fetchall()
    json_list = []
    for record in records:
        json_obj = {'created_at': str(record[2]), 'ts': str(record[9]), 'te': str(record[10]), 'protocol': record[5],
                'source_ip': record[3], 'destination_ip': record[7], 'td': record[8], 'history': record[4],
                'service': record[6], 'anomaly_score': record[1]}
        json_list.append(json_obj)
    mydb.commit()
    return json.dumps(json_list)

@app.route('/')
def hello():
    return "hello world\n"


if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port))

