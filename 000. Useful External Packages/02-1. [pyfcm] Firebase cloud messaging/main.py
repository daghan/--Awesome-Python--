﻿# pip install pyfcm
from pyfcm import FCMNotification
# FCM Notification을 위한 모듈. 원랜 firebase 측으로 HTTP request를 전송해야 하지만
# 어떤 개발자가 이게 불편하다고 느꼈는지 pyfcm을 만들어 두었다

fcm = FCMNotification(api_key='')
# FCM 서버 키를 통해 객체를 만들자

# 클라이언트 하나에 보내기, 여러 곳에 보내기, topic subscriber에 보내기가 대표적인 메소드다
fcm.notify_single_device(registration_id='', message_title='제목이야', message_body='body다')

fcm.notify_multiple_devices(registration_ids=['', ''], message_title='제-목', message_body='배고파')
# 여러 클라이언트에 보내는 메소드. registration_ids 파라미터로 리스트 형태의 클라이언트 키들을 전달한다

fcm.notify_topic_subscribers(topic_name='', message_title='제-목', message_body='body!')
# 특정 topic을 subscribe하고 있는 디바이스에 보내기
