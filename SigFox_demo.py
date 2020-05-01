from network import SigFox
import socket


def run():
    print("Demo Sigfox - sending")
    # init Sigfox from RCZ4 (Thailand)
    sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

    # create a SigFox socket
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

    # make the socket blocking
    s.setblocking(True)

    # configure it as uplink only
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

    # send some bytes
    print("sending data to Sigfox")
    ret = s.send("I'm LoPy4")
    print("Total sent : " + str(ret))
