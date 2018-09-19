from pyfcm import FCMNotification

# https://github.com/olucurious/PyFCM

API_KEY = "AAAAjA9yJPo:APA91bGpa13pfTdiiWS4wEKpH_ougbCbK15oDrbatFhxo3wtiv39fIgN41RVignr" \
          "HWmrDVB3tvTxZLK7K41D9dAD6xNyrX-7dJgVSIIqjapeMf8yEvBL1nWW_YtsHL9OmzWHotYsSwMV"

push_service = FCMNotification(api_key=API_KEY)

def push_event(msg, event="news"):
    result = push_service.notify_topic_subscribers(topic_name=event, message_body=msg, content_available=True)
    print("FCM %s" % result)


def push_data(msg, event="news"):
    result = push_service.notify_topic_subscribers(topic_name=event, data_message=msg, content_available=True)
    print("FCM %s" % result)
