from pyfcm import FCMNotification

#https://github.com/olucurious/PyFCM

API_KEY = "AAAAjA9yJPo:APA91bGpa13pfTdiiWS4wEKpH_ougbCbK15oDrbatFhxo3wtiv39fIgN41RVignrHWmrDVB3tvTxZLK7K41D9dAD6xNyrX-7dJgVSIIqjapeMf8yEvBL1nWW_YtsHL9OmzWHotYsSwMV"
push_service = FCMNotification(api_key=API_KEY)

result = push_service.notify_topic_subscribers(topic_name="news", message_body=" THIS IS PYTHOOOON!!!")
print(result)
