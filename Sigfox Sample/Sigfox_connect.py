from network import Sigfox
import socket
​
# init Sigfox for RCZ4 (Thailand)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)
​
# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
​
# make the socket blocking
s.setblocking(True)
​
# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
​
# send some bytes

#s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

#real code here ---------------
#Here is just example

#s.send("Welcome to IoT")
s.send("I'm LoPy4")

