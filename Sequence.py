import GenerateUUID
import Collection as cl

class ControlSeq():
    
    def __init__(self, seqCaption = "Hollow sequence", transmitLock = "200", keyLock = "2", posInSection = "-1", data1 = "", data2 = ""):
        self.seqType = "Control"
        self.seqUUID = GenerateUUID.generateUUID(self)
        self.seqCaption = seqCaption

        self.trasmitLock = transmitLock
        self.keyLock = keyLock

        self.data1 = data1
        self.data2 = data2
        self.posInSection = posInSection

        self.deviceMenu = "True"
        self.projectMenu = "True"
        self.selectable = "True"
        self.deletable = "True"
        self.hasData = "False"
        self.useFooter = "True"
        
        self.posInSection = -1         #position in seq nav from top down

    def toString(self):
        cmd = ""
        cmd += cl.addTab(3)
        cmd += "<Sequence Name=" + cl.putInQuote(self.seqUUID)
        cmd += " Caption=" + cl.putInQuote(self.seqCaption)
        cmd += " DeviceMenu=" + cl.putInQuote(self.deviceMenu)
        cmd += " ProjectMenu=" + cl.putInQuote(self.projectMenu)
        cmd += " Selectable=" + cl.putInQuote(self.selectable)
        cmd += " SequenceType=" + cl.putInQuote(self.seqType)
        cmd += " Deletable=" + cl.putInQuote(self.deletable)
        cmd += " HasData=" +cl.putInQuote(self.hasData)
        cmd += " UseHeaderFooter=" +cl.putInQuote(self.useFooter) +">"

        print(cmd)
        
        
        

class SourceSeq():
    
    def __init__(self, seqCaption = "Hollow sequence", transmitLock = "200", keyLock = "2", posInSection = "-1", data1 = "", data2 = ""):
        self.seqType = "Source"
        self.seqUUID = GenerateUUID.generateUUID(self)
        self.seqCaption = seqCaption

        self.trasmitLock = transmitLock
        self.keyLock = keyLock

        self.data1 = data1
        self.data2 = data2
        self.posInSection = posInSec

        self.deviceMenu = "True"
        self.projectMenu = "True"
        self.selectable = "True"
        self.deletable = "True"
        self.hasData = "False"
        self.useFooter = "True"
        
        self.posInSection = -1         #position in seq nav from top down

class PowerOnSeq():
    def __init__(self, seqCaption = "On", delay = "500", warmUpTime = "30", onToOffDevice = "45", posInSection = "-1", data1 = "", data2 = ""):
        self.seqType = "PowerOn"
        self.seqUUID = GenerateUUID.generateUUID(self)
        self.seqCaption = seqCaption

        self.delay = delay
        self.warmUpTime = warmUpTime
        self.onToOffTime = onToOffTime

        self.data1 = data1
        self.data2 = data2
        self.posInSection = posInSec

        self.deviceMenu = "True"
        self.projectMenu = "True"
        self.selectable = "True"
        self.useFooter = "True"


class PowerOffSeq():
    def __init__(self, seqCaption = "Off", delay = "500", keyLockTime = "90", posInSection = "-1", data1 = "", data2 = ""):
        self.seqType = "PowerOff"
        self.seqUUID = GenerateUUID.generateUUID(self)
        self.seqCaption = seqCaption

        self.delay = delay
        self.keyLockTime = keyLockTime

        self.data1 = data1
        self.data2 = data2
        self.posInSection = posInSec

        self.deviceMenu = "True"
        self.projectMenu = "True"
        self.selectable = "True"
        self.useFooter = "True"


class VolumeSeq():
    def __init__(self, seqCaption = "Volume", delay1 = "0", delay2 = "0",
                 countStart = "0", countStop = "0", maxVol = "100", minVol = "0", volStep = "1",
                 repeatSpeed = "200",typeValue = "Continous", countTypeValue = "String",
                 countFormat = "Decimal", secondCountStart = "0", secondCountStop = "0",
                 byteOrderValue = "LSB", data1 = "", data2 = "",
                 checkSumValue = "None", checkSumCaption = "", checkSumName = ""):
        
        self.seqType = "Volume"
        self.seqUUID = GenerateUUID.generateUUID(self)
        self.seqCaption = seqCaption

        self.countStart = countStart
        self.countStop = countStop
        self.secondCountStart = secondCountStart
        self.secondCountStop = secondCountStop
        self.delay1 = delay1
        self.delay2 = delay2
        self.minVol = minVol
        self.maxVol = maxVol
        self.volStep = volStep
        self.repeatSpeed = repeatSpeed
        
        self.typeValue = typeValue
        self.countTypeValue = countTypeValue
        self.byteOrderValue = byteOrderValue
        self.countFormat = countFormat

        self.checkSumValue = checkSumValue
        self.checkSumCaption = checkSumCaption
        self.checkSumName = chackSumName
        
        self.data1 = data1
        self.data2 = data2
        self.posInSection = posInSec

        self.deviceMenu = "True"
        self.projectMenu = "True"
        self.selectable = "True"
        self.useFooter = "True"   

class SequenceHolder:
    
    def __init__(self):
        self.address = ""
        self.fullList = ""

        self.irList = []
        self.rsList = []
        self.lanList = []

    
    def addSequence(self, seq, connType):

        if (connType == "IR"):
            self.irList.append(seq)
        if (connType == "IR"):
            self.rsList.append(seq)
        if (connType == "LAN"):
            self.lanList.append(seq)

    def getConnectionType(self, seq):

        lines = seq.split('\n')
        for line in lines:
            print(line)
        

        


        
