# tilt sensor
import paho.mqtt.client as mqtt
import datetime as dt
import time

#Variables
# counter=1

# Events
def on_message_tilt_sensor(client, userdata, msg):
    # global counter
    # counter += 1
    # if(counter%5==0):
     print('Received a new tilt data:' + str(msg.payload.decode('utf-8')))   
   
def on_connect(edge, userdata, flags, rc):
    # RelayOn=False
    if rc == 0:
        print('connected to MQTT broker')
        edge.message_callback_add('VTEST2/IN/TLT:00001', on_message_tilt_sensor)
        edge.on_subscribe = on_subscribe_success
        edge.subscribe('VTEST2/IN/TLT:00001')
    else:
        print('Failed to connect to MQTT broker, return code %d\n', rc)
        
def on_subscribe_success(mosq, obj, mid, granted_qos):
    # print("Subscribed: " + str(mid) + " " + str(granted_qos))
    time.sleep(0.5)
    edge.on_publish = on_publish_stp_success
    edge.publish('VTEST2/BOOT','IN:TLT:00001:N/A:STP')
    
def on_publish_stp_success(mosq, obj, mid):
    # print("mid: " + str(mid))
    time.sleep(0.5)
    edge.on_publish = on_publish_srt_success
    edge.publish('VTEST2/BOOT','IN:TLT:00001:N/A:SRT')
    
def on_publish_srt_success(mosq, obj, mid):
    print("mid:" + str(mid))
    
# Starting Point
edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
edge.on_connect = on_connect
edge.connect('20.219.125.196', 1883)
edge.loop_forever()







# tilt sensor
import paho.mqtt.client as mqtt
import datetime as dt
import time

#Variables
# counter=1

# Events
def on_message_tilt_sensor(client, userdata, msg):
    # global counter
    # counter += 1
    # if(counter%5==0):
     print('Received a new tilt data:' + str(msg.payload.decode('utf-8')))   
   
def on_connect(edge, userdata, flags, rc):
    # RelayOn=False
    if rc == 0:
        print('connected to MQTT broker')
        edge.message_callback_add('VTEST2/IN/TLT:00001', on_message_tilt_sensor)
        edge.on_subscribe = on_subscribe_success
        edge.subscribe('VTEST2/IN/TLT:00001')
    else:
        print('Failed to connect to MQTT broker, return code %d\n', rc)
        
def on_subscribe_success(mosq, obj, mid, granted_qos):
    # print("Subscribed: " + str(mid) + " " + str(granted_qos))
    time.sleep(0.5)
    edge.on_publish = on_publish_stp_success
    edge.publish('VTEST2/BOOT','IN:TLT:00001:N/A:STP')
    
def on_publish_stp_success(mosq, obj, mid):
    # print("mid: " + str(mid))
    time.sleep(0.5)
    edge.on_publish = on_publish_srt_success
    edge.publish('VTEST2/BOOT','IN:TLT:00001:N/A:SRT')
    
def on_publish_srt_success(mosq, obj, mid):
    print("mid:" + str(mid))
    
# Starting Point
edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
edge.on_connect = on_connect
edge.connect('20.219.125.196', 1883)
edge.loop_forever()
