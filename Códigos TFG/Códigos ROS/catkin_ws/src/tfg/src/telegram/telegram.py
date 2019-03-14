#! /usr/bin/env python
import urllib, requests
import rospy
from std_msgs.msg import String

def get_url(url):
    response = requests.get(url, verify=False)
    content = response.content.decode("utf8")
    return content
def callback(message) :
<<<<<<< HEAD:Códigos TFG/Códigos ROS/catkin_ws/src/tfg/src/telegram/telegram.py
    get_url('https://api.telegram.org/bot[BOT_API_KEY]/sendMessage?chat_id=[CHAT_ID]&text='+message.data+'')
=======
    get_url('https://api.telegram.org/bot[API_BOT_KEY]/sendMessage?chat_id=[CHAT_ID_KEY]&text='+message.data+'')
>>>>>>> 81f5988fa16c7dfd2658e79fbd5ddfb77c507a1c:Códigos TFG/catkin_ws/src/tfg/src/telegram/telegram.py

rospy.init_node('listener_telegram', anonymous=True)
rospy.Subscriber("message_output",String, callback)
rospy.spin()
#cuidado con el ID del canal y el bot!
