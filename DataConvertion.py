import Collection

class ConvertData:

#------------- Convertions by sequence -----------

    def asciiToHexSeq(self, dataSeq):

        conv = ""
        
        for char in dataSeq:
            conv += self.asciiToHex(char)
        return conv
   
    def decimalToHexSeq(self, dataSeq, decimalSize):

        conv = ""
        convSeq = ""
        addNullNr = 0
        addNullNr = decimalSize - len(dataSeq)%decimalSize
        dataSeq = ("0")*addNullNr + dataSeq 
        
        for x in range(0, len(dataSeq)+addNullNr, decimalSize):
            conv = dataSeq[x:x+decimalSize]

            if (len(conv) != 0):
                
                conv = Collection.addNulls(self.decimalToHex(int(conv)),decimalSize)
                convSeq += conv[1:]
                

        convSeq = Collection.cutNull(convSeq, "HEX")
                    
        return convSeq


    def decimalToAsciiSeq(self, dataSeq):

        conv = ""
        
        for ch in str(dataSeq):
            conv += str(ord(ch))
        
        return conv

    def asciiToDecSeq(self, dataSeq):
        conv = ""
        
        for ch in dataSeq:
            conv += str(ord(ch))
        
        return conv
     

#------------- Convertions by one ----------------

    def asciiToHex(self, dataChar):
        conv = hex(ord(dataChar))
        conv = format(ord(dataChar), "x")
        return conv

    def decimalToHex(self, integer):
        return str(hex(integer))[2:]

    def decimalToAscii(self, integer):       
        integer = chr(integer)
        return integer

    def asciiToDec(self, char):
        return ord(char)

TEST = ConvertData()
TEST.decimalToAscii(120)
print(TEST.asciiToDecSeq("123654"))

