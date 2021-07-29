import requests

class Publisher:

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def publish(self, data):
        res = requests.post(self.webhook_url, json = data)
        print(res.status_code)