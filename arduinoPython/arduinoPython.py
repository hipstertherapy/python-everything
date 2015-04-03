import time
import serial
import mosquitto

#broker connection
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")
client.subscribe("Light")

#arduino usb serial port
port = serial.Serial("COM3",9600,timeout=2)

#message from broker 
def messageReceived(broker, obj, msg):
    global client
    print(msg.topic + " is "+ msg.payload)
    
    #switch
    if msg.payload == "on":
    
        port.write("1")
    
    elif msg.payload == "off":
    
        port.write("0")

    elif msg.payload == "dance":
       
        port.write("1")
        time.sleep(0.1)
        port.write("0")
        time.sleep(0.1)
        port.write("1")
        time.sleep(0.1)
        port.write("0")
        time.sleep(0.1)
        port.write("1")
        port.write("1")
        time.sleep(0.1)
        port.write("0")
        time.sleep(0.1)
        port.write("1")
        time.sleep(0.1)
        port.write("0")
        time.sleep(0.1)
        port.write("1")
        port.write("1")
        time.sleep(0.1)
        port.write("0")
        time.sleep(0.1)
        port.write("1")
        time.sleep(0.1)
        port.write("0")
        time.sleep(0.1)
        port.write("1")
        
        
        
      
        
    
client.on_message = messageReceived

while (client != None): client.loop()
