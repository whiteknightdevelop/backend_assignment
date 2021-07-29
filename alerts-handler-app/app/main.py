from publisher import *
from listener import *

WEBHOOK_URL = 'https://webhook.site/907401ab-e75c-4dcd-97f7-c17f4bcdd0f5'

publisher = Publisher(WEBHOOK_URL)
listener = Listener()

data = {"test":"test"}
publisher.publish(data)