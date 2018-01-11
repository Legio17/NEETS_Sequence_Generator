#--------------- simple operation methods------------

def addSpace(size):
    return " "*size

def newLine():
    return "\n"

def addQuote():
    return '\"'

def addTabONE():
    return "    "

def addTab(number):
    return addTabONE()*number

def putInQuote(word):
    new_word = ""
    new_word += addQuote()
    new_word += word
    new_word += addQuote()

    return new_word

def addNulls(number, finalLen):
    number = str(number)
    
    while len(number) != finalLen:
        number = "0" + number
    
    return number

def cutNull(string, nrType):

    ingnoreRest = "false";
    new_string = "ERROR";
    
    if (nrType == "HEX"):
        diff = len(string) % 2 
        string = (("0")*diff) + string
        
        for x in range(0, len(string), 2):
            if(string[x:x+2]== "00"):
                pass
            else:
                string = string[x:]
                return string
            
    return new_string
            
