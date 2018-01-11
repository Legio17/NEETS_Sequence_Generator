import Sequence

class DeviceDataLoader:

    seqholder = Sequence.SequenceHolder()
    
    def __init__(self):
        self.address = ""
        self.fullList = ""
    
    def setAddress(self, adr):
        self.address = adr

    def getAddress(self):
        return self.address

    def getFullList(self):
        return self.fullList

    def printList(self, seqList):

        for line in seqList:
            pass


    def loadDevice(self):
        lines = [line.rstrip('\n') for line in open(self.address)]
        self.fullList = lines

    def createSection(self):

        startFound = "False"
        irFound = "False"
        rsFound = "False"
        lanFound = "False"
        endFound = "False"
        currentLine = 0
        fullList = self.getFullList()
        filepath = self.getAddress()
        
        with open(filepath) as fp:  
            line = fp.readline()
            cCT = ""; #current connection type(IR,RS,LAN)
            
            while line:
                if ("<IR>" in line):
                    cCT = "IR"
                elif ("<RS232>" in line):
                    cCT = "RS"
                elif ("<LAN>" in line):
                    cCT = "LAN"
                
                if ("<Sequence " in line):
                    rawSeqBuffer = "";
                    rawSeqBuffer += line
                    line = fp.readline()

                    while("</Sequence>" not in line):
                        rawSeqBuffer += line
                        line = fp.readline()
                    rawSeqBuffer += line[:-1]

                    self.seqholder.addSequence(rawSeqBuffer,cCT)
                    
                line = fp.readline()
        
    def loadStart(self,currentLine):
        fullList = self.getFullList()
        
        while fullList[currentLine].find("<IR>") == -1:
            self.startList.append(fullList[currentLine])
            currentLine += 1
        
        return currentLine


    def loadEnd(self, currentLine):
        fullList = self.getFullList()
        while (fullList[currentLine].find("</Root>") == -1):
            try:
                self.endList.append(fullList[currentLine])
                
            except AttributeError:
                currentLine = len(fullList)-2
                return currentLine
            currentLine += 1
            
        currentLine = len(fullList)-2
        self.endList.append(fullList[currentLine+1])
        return currentLine 

    #------------- port section chunks ----------------------
    def loadIR(self, currentLine):
        fullList = self.getFullList()
        
        while fullList[currentLine].find("</IR>") == -1:
            self.irList.append(fullList[currentLine])
            currentLine += 1
        return currentLine
    
    def loadRS232(self, currentLine):
        fullList = self.getFullList()

        while fullList[currentLine].find("</RS232>") == -1:
            self.rsList.append(fullList[currentLine])
            currentLine += 1
        return currentLine
    
    def loadLAN(self, currentLine):
        fullList = self.getFullList()
        
        while fullList[currentLine].find("</LAN>") == -1:
            self.lanList.append(fullList[currentLine])
            currentLine += 1
        return currentLine

        

        
            
        
        
                



