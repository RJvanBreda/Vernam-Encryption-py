#Vernam Cypher

import binascii # module contains a number of methods to convert between binary and various ASCII-encoded binary representations.
import docx
from docx import Document


def eMain(key,plaintext):                                           # text fields
    binaryDict = Dictionary()                                       # Dictionary created...creation of dictionary
    nuweKey = LengtheningKey(key,plaintext)                         # lengthening of key
    binarylistKey = ConversionToBinary(nuweKey,binaryDict)          # Key conversion to binary if necessary
    binarylistPlaintext = ConversionToBinary(plaintext,binaryDict)  # conversion to binary
    binarylistCipher = XORFunction(binarylistKey,binarylistPlaintext) # Xor function uses convertet binaries and compares them,
    return ConversionText(binarylistCipher,binaryDict)                # Cypher text -- die encrypted text




alphabet = "abcdefghijklmnopqrstuvwxyz"
#upper = "ABCDEFGHIJKLMNTOPGR"


#create Dictionary
# Dictionary is created that assigns each letter to binary, that will used to calculate and provide the end result of the vernam cypher.
#-	A dictionary was created that allows the letters to be converted to binary, that will allow is to complete it with a XOR function.
# list from a-z Upper and Lower letters and punctutation.
def Dictionary():
    Dict = {'a': '000000', 'b': '000001', 'c': '000010', 'd': '000011', 'e': '000100', 'f': '000101', 'g': '000110', 'h': '000111', 'i': '001000', 'j': '001001',
     'k': '001010', 'l': '001011', 'm': '001100','n': '001101', 'o': '001110', 'p': '001111', 'q': '010000', 'r': '010001', 's': '010010', 't': '010011',
     'u': '010100', 'v': '010101','w': '010110', 'x': '010111', 'y': '011000', 'z': '011001', 'A': '011010', 'B': '011011', 'C': '011100', 'D': '011101',
     'E': '011110', 'F': '011111', 'G': '100000', 'H': '100001', 'I': '100010','J': '100011', 'K': '100100', 'L': '100101', 'M': '100110', 'N': '100111',
     'O': '101000', 'P': '101001', 'Q': '101010', 'R': '101011', 'S': '101100', 'T': '101101', 'U': '101110', 'V': '101111', 'W': '110000', 'X': '110001',
      'Y': '110010', 'Z': '110011', ' ': '110100', '.': '110101', ',': '110110', '?': '110111', '!': '111000','"': '111001', ';': '111010', ':': '111011',
      '(': '111100', ')': '111101', '-': '111110', '\n': '111111', '{':'1000000'}

    return Dict # returns completed Dictionary list



# Lengthening of key takes place, lengthes the key to the message for encryption
# -	The encryption requires the key to be the same size as the message field. 
def LengtheningKey(key,plaintext):                 #This function expects 2 arguments, and gets 2 arguments
    keyLength = len(key)                           #lengt of the key, length of textfield. key = 6 (101110)
    messageLength = len(plaintext)                 # plain text (message) length. message = hello: Legth = 5
    reiteration = messageLength // keyLength       #repitition = 6 // 5 = 0
    remainder = messageLength % keyLength          # mod. remainder = 6 % 5 = 1
    nuweKey = key * reiteration + key[0:remainder] #key     *   repition + key[0:remainder]: 101110  *   0        + key[0:1]: = 10111010
    return nuweKey


# conversion of Text and numbers to binary
def ConversionToBinary(text,dict):              #convert to bin function
    Outlist = []
    for char in text:
        if char in "1234567890'&":              # converts of numbers to binary, keeps existing binary code
            Outlist.append(char)                # appends to list = Outlist
        else:
            numBin = dict[char]                 # Converts of characters. Take characters and converts to binary
            Outlist.append(numBin)              # appends to list = Outlist. Appends to Outlist from dictionary
    return Outlist


# Conversion of binary to text, Cypher Text
def ConversionText(binarylist,dict):            # xor binary to cypher text
    outString = ""
    newDict = {}
    for (k,v) in dict.items():
        newDict[v] = k
    for binNum in binarylist:
        if binNum in "1234567890'&":
            outString = outString + binNum
        else:
            char = newDict[binNum]
            outString = outString + char
    return outString

#open of textfile
def readDoc(txtfile):
    outtext = ""
    file = open(txtfile,'r', encoding='ISO-8859-1')  # open of text file
    if txtfile.endswith('.docx'):
        document = Document(txtfile)
        for outtext in document.paragraphs:
            print(outtext.text)
        print(type(outtext))
        return str(outtext.text)

    lines = file.readlines()                         # reading of lines
    for line in lines:
        outtext = outtext + line                     # reading of lines in text file
    return outtext

def readWord(filename):
    print("Asdadasdsd")
    file = open(filename,'r', encoding='ISO-8859-1')
    outtext = ""





    #with open(filename) as f:
    #    lines = f.readlines()
    #out = []
    #for line in lines:
    #    out.append(line.rstrip("\n"))
    #return out


# encryption system -- XOR (exlusive or) Truth table
# A Truth gate: true or false: Works with binary: Carry out the XOR operation, applying it to each corresponding pair of bits:
# Truth Table: 0:0 = 0 (false): 0:1 = 1(true): 1:0 = 1 (true): 1:1 = 0(false)
# XOR works on both encrypt and decrypt

def XORFunction(binKey, binText):
    LengthBin=len(binKey)                             # Length of my binary key 10111 = 5
    OutList=[] # declare list
    for i in range(LengthBin):                        # 0,1,2,3,4,5 so 6 times it wil go through it. 6 times loop to binary text = hello
        if binText[i] in "1234567890'&":              # Check to see if characters or binary = "1234567890'&" if not then go else
            OutList.append(binText[i])
        else:
            y = int(binKey[i],2) ^ int(binText[i],2)  # ^ (XOR),truth comparrison: binary: text becomes decimal. Becomes decimal and then plus decimal to receive end value.
            TempBin=(bin(int(y))[2:].zfill(6))        # Converts decimal to binary.
            OutList.append(TempBin)
    return OutList



# ^ (XOR),truth comparrison: binary: text becomes decimal....binary key 1011 base 2 (base 2 wat binary is) dan XOR text = hello wat mos converted is h se value 7...
# .die is 1 0f 7.....die is reg-------word decimaal en word geplus om einde som te gee wat die finale antwoord gee
