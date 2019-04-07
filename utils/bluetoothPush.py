import json
import requests
import os


class bluetoothPush():
    def __init__(self):
        pass

    # initialising pushbullet API

    def send_notification_via_pushbullet(self, title, body):
        __ACCESS_TOKEN = "o.M13sYREYvbBuRz5xUh0A86lrpclTFCuc"
        __ACCESS_TOKEN_HARRY = "o.QcWpSbXN5EGj8Jxi1T7mDN0dq6Bz7h3P"

        data = {"type": "note", "title": title, "body": body}
        # sends notification to both clients
        response = requests.post("https://api.pushbullet.com/v2/pushes", data=json.dumps(data),
                                 headers={"Authorization": "Bearer " + __ACCESS_TOKEN, "Content-Type": "application/json"})
        response = requests.post("https://api.pushbullet.com/v2/pushes", data=json.dumps(data),
                                 headers={"Authorization": "Bearer " + __ACCESS_TOKEN_HARRY, "Content-Type": "application/json"})

        if(response.status_code != 200):
            raise Exception()
