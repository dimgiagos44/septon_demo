import mysql.connector
import requests


alert_json = {
    'ts': '2022-09-03 00:00:38',
    'te': '2022-09-09 15:09:40',
    'protocol': 'TCP',
    'source_ip': '10.0.2.108',
    'destination_ip': '62.75.184.70',
    'history': 'S',
    'td': 572942.228,
    'service': '-',
    'anomaly_score': 0.995
}
'''
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="red5PRO@action"
    )

    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use alertsDB;")
    content = mycursor.execute("select * from alert;")
    print(content)

    mycursor.execute("insert into alert (ts, te, protocol, source_ip, destination_ip, history, td, service, anomaly_score) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
    (alert_json['ts'], alert_json['te'], alert_json['protocol'], alert_json['source_ip'], alert_json['destination_ip'], alert_json['history'], 
    alert_json['td'], alert_json['service'], alert_json['anomaly_score']))
    mydb.commit()

    mycursor.execute("select * from alert;")
    records = mycursor.fetchall()
    print(records)
'''

res = requests.post('http://localhost:5000/add', json=alert_json)
print(res.ok)