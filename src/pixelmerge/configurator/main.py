import sacn
import time

running = False
#maxUniverses = 0

consoleEnableCh = 1
consoleInStart = 20
pixelmapInStart = 50
pixelOutStart = 150
numOfPixeluniverses = 96

consoleEnable = False
unicastdest = '127.0.0.1'

def startsACN(universeModel, pixelModel, maxUniverses, consoleEnableChannel, unicastIP, priority):
    global receiver, sender, running, consoleEnableCh, unicastdest
    consoleEnableCh = consoleEnableChannel
    unicastdest = unicastIP
    receiver = sacn.sACNreceiver()
    sender = sacn.sACNsender()
    
    receiver.start()
    sender.start()
    createUniverses(universeModel, maxUniverses, priority)
    createMap(pixelModel)
    running = True

def stopsACN():
    global receiver, sender, running
    receiver.stop()
    sender.stop()
    running = False
    print("stopped")
    

def refreshUniverse():
    availableUniverses = []
    for i in sender.get_active_outputs():
        availableUniverses.append(i)
    for i in receiver.get_possible_universes():
        availableUniverses.append(i)
    print(availableUniverses)
    return availableUniverses
    
class universe():
    def __init__(self, number, mode, multicast=True, outputUni=0, priority=100):
        #possible modes: ['ctrlIn', 'consoleIn', 'pixelIn', 'pixelOut']
        self.number = number
        self.pixeloutputuni = outputUni
        self.mode = mode
        self.dmxdata = []
        self.newDMX = []
        self.priority = priority

        
        #print(self.number, self.mode)
        for i in range(513):
            self.dmxdata.append(0)

        
        if self.mode == 'ctrlIn':
            if multicast:
                receiver.join_multicast(self.number)
            receiver.register_listener('universe', self.ctrlcallback, universe=self.number)
            
        elif self.mode == 'consoleIn':
            self.map = []
            for i in range(513):
                self.map.append([])
            
            if multicast:
                receiver.join_multicast(self.number)
            receiver.register_listener('universe', self.consoleCallback, universe=self.number)


        elif self.mode == 'pixelIn':
            if multicast:
                receiver.join_multicast(self.number)
            receiver.register_listener('universe', self.pixelCallback, universe=self.number)

        elif self.mode == 'pixelOut':
            sender.activate_output(self.number)
            sender[self.number].priority = self.priority
            if multicast:
                sender[self.number].multicast = True
            else:
                sender[self.number].destination = unicastdest
                sender[self.number].multicast = False

        else:
            print("INVALID MDOE FOR UNIVERSE ", self.number)
    
    def ctrlcallback(self, packet):
        global consoleEnable
        if packet.dmxData[consoleEnableCh - 1] > 127:
            consoleEnable = True
        else:
            consoleEnable = False
        print(packet.universe)
        print(consoleEnable)

    def consoleCallback(self, packet):
        if consoleEnable and (map != None):

            for i in range(512):
                for out in self.map[i]:
                    if out != None:
                        universes[out[0]].dmxdata[out[1]] = packet.dmxData[i]
            for uni in universes:
                if uni != None:
                    if uni.mode == 'pixelOut':

                        uni.updateDMXData()


    def pixelCallback(self, packet):
        if not consoleEnable:
            dmx = packet.dmxdata
            sender[self.pixeloutputuni].dmx_data = dmx

    def updateDMXData(self):
        sender[self.number].dmx_data = self.dmxdata

def createUniverses(universeModel, maxUniverses, priority):

    global universes
    universes = []
    for i in range(maxUniverses+1):
        universes.append(None)
    #create universes

    for uni in universeModel:
        universes[uni.universeNumber]=universe(uni.universeNumber, uni.universeType, uni.multicast, priority=priority)
    
def createMap(pixelModel):
    for pixel in pixelModel:
        iUni = pixel.inputUniverse
        iAdd = pixel.inputAddress - 1
        oUni = pixel.outputUniverse
        oAdd = pixel.outputAddress - 1
        #red
        universes[iUni].map[iAdd].append((oUni, oAdd))
        #green
        universes[iUni].map[iAdd+1].append((oUni, oAdd+1))
        #blue
        universes[iUni].map[iAdd+2].append((oUni, oAdd+2))
        #white
        if pixel.pixelType == 'RGBW':
            universes[iUni].map[iAdd+3].append((oUni, oAdd+3))

            
            