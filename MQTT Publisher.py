import paho.mqtt.publish as publish

publish.single(
    "iot-test1234", 
    payload="12345", 
    qos=0, 
    retain=False,
    hostname="mqtt.eclipse.org",
    port=1883, 
    client_id="",
    keepalive=60, 
    will=None,
    auth=None, 
    tls=None,
    #protocol=mqtt.MQTTv311,
    transport="tcp"
)

msgs = [{'topic':"iot-test1234", 'payload':"Message 1"},
        {'topic':"iot-test1234", 'payload':"Message 2"},
        {'topic':"iot-test1234", 'payload':"Message 3"}]

publish.multiple(
    msgs,
    hostname="mqtt.eclipse.org",
    port=1883,
    client_id="",
    keepalive=60,
    will=None,
    auth=None,
    tls=None,
    #protocol=mqtt.MQTTv311,
    transport="tcp"
)
