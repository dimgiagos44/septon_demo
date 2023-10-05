import mysql.connector
import requests
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

alert_json = {
    'ts': '2022-09-03 00:00:38',
    'te': '2022-09-09 15:09:40',
    'protocol': 'TCP',
    'source_ip': '10.0.2.108',
    'destination_ip': '62.75.184.70',
    'history': 'S',
    'td': 572942.228,
    'service': '-',
    'anomaly_score': 0.995,
    'created_at': current_time
}

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="red5PRO@action"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("use alertsDB;")
'''
mycursor.execute("select * from alert;")
records = mycursor.fetchall()
print(records)
print(len(records))
print(records[0])
print(type(records[0]))
'''
mycursor.execute("SELECT * FROM alert WHERE alert.created_at > now() - interval 5 minute ORDER BY ID DESC LIMIT 4")
records = mycursor.fetchall()
print(records)
print(len(records))

