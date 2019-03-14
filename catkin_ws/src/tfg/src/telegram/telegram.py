#! /usr/bin/env python
import urllib, requests
import rospy
from std_msgs.msg import String

def get_url(url):
    response = requests.get(url, verify=False)
    content = response.content.decode("utf8")
    return content
def callback(message) :
    get_url('https://api.telegram.org/bot687994977:AAFlBm2BSr1bt6GXIXpQUjmsntaNGC16zr8/sendMessage?chat_id=182585904&text='+message.data+'')

rospy.init_node('listener_telegram', anonymous=True)
rospy.Subscriber("message_output",String, callback)
rospy.spin()
#cuidado con el ID del canal y el bot!
