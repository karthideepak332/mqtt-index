# Vibration sensor
import re 
import paho.mqtt.client as mqtt
import datetime as dt
import time

#Variables
counter=1

# Events
def on_message_vibration_sensor(client, userdata, msg):
    global counter
    message = msg.payload.decode('utf-8')
    data = message.split(":")
    vibration_list = re.findall("\d+", data[3]) # "\d" matches one or more digits
    if len(vibration_list)<=0:
         vibration_value = 0 
    else:
         vibration_value =  int(vibration_list[0])
    
    if vibration_value >= 1000:
          counter += 1
          if counter%3==0:
           print("Warning!")  
          else:
              print("")
         

def on_connect(edge, userdata, flags, rc):
    # RelayOn=False
    if rc == 0:
        print('connected to MQTT broker')
        edge.message_callback_add('VTEST2/IN/VIB:00009', on_message_vibration_sensor)
        edge.on_subscribe = on_subscribe_success
        edge.subscribe('VTEST2/IN/VIB:00009')
    else:
        print('Failed to connect to MQTT broker, return code %d\n', rc)
        
def on_subscribe_success(mosq, obj, mid, granted_qos):
    # print("Subscribed: " + str(mid) + " " + str(granted_qos))
    time.sleep(0.5)
    edge.on_publish = on_publish_stp_success
    edge.publish('VTEST2/BOOT', 'IN:VIB:00009:hertz:STP')
    
def on_publish_stp_success(mosq, obj, mid):
    # print("mid: " + str(mid))
    time.sleep(0.5)
    edge.on_publish = on_publish_srt_success
    edge.publish('VTEST2/BOOT', 'IN:VIB:00009:hertz:SRT')
    
def on_publish_srt_success(mosq, obj, mid):
    print("mid:" + str(mid))
    
# Starting Point
edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
edge.on_connect = on_connect
edge.connect('20.219.125.196', 1883) 
edge.loop_forever()

