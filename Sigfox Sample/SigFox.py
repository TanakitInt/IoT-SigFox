from network import Sigfox
import binascii

# Initialise SigFox for RCZ4 (You may need a different RCZ Region)
sigfox = Sigfox(mode=Sixfox.SIGFOX, rcz=Sigfox.RCZ4)

# print SigFox Device ID
print(binascii.hexlify(sigfox.id()))

# print SigFox PAC number
print(binascii.hexlify(sigfox.pac()))
