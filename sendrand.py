import time
import sacn
import random

sender = sacn.sACNsender()
sender.start()
sender.activate_output(5)
sender[5].multicast = True

universe5 = []
for i in range(512):
    universe5.append(0)

print(len(universe5))

endTime = time.time() + 30

while time.time() < endTime:

    universe5[0] = random.randint(0,254)
    universe5[5] = random.randint(0,254)
    sender[5].dmx_data = universe5
    time.sleep(.1)

sender.stop()