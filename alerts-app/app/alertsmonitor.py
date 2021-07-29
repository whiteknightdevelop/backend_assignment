from bson.json_util import dumps
import json

THRESHOLD = 3.757

class AlertsMonitor:

    def __init__(self):
        self.db_data = None

    def process(self, data):
        print('alerts-process')
        print(self.db_data)
        if not self.db_data:
            self.db_data = data
        
        jsonObject = json.loads(self.db_data)
        jsonObject[0].pop('_id')
        for key in jsonObject[0]:
            value = jsonObject[0][key]
            if self.check_threshold(value):
                print("({}) = ({})".format(key, value))


    def check_threshold(self, value):
        print('check_threshold')
        if value > THRESHOLD:
            return True
        else:
            return False
            # print(value)
            



    def dispatch_alert(self):
        print('dispatch_alert')