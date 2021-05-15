#import functions
from FunctionList import *
from tkinter import *              # GUI Toolkit
#import tkinter as tk
from tkinter import filedialog     # Help you open, save files or directories
from PIL import ImageTk            # Image importing
import random



#GUI: initializing variables
PlatformMain = None # Variable to change Whole GUI
LabelPlatform = None

#Files
text = None
filename = None                 # uploading of file

#Labels
LabelCypherText = None          # Cypher text display
LabelDecypherText = None        # Cypher text display

# Text boxes
EKeyText = None                 # Text Box key field 1
EMessageText = None             # Text Box Message Field

DKeyText = None                 # Text Box key field 2
DCyphterText = None             #Text Box Cyphter Text



#Functions
def Platformmain():
    
    global PlatformMain
    global LabelPlatform

    global EKeyText                 # Text Box key field 1
    global EMessageText             # Text Box Message Field
    

    global DKeyText                 # Text Box key field 2
    global DCyphterText             # Text Box Cyphter Text

    global LabelCypherText          # Cypher text display
    global LabelDecypherText        # Cypher text display

   
    PlatformMain = Tk()   
    PlatformMain.geometry("990x880")
    
    #Top platform labels

     #library of basic elements of GUI: Set platform
    PlatformMain.title("Vernam Encryption program")
    PlatformMain.config(bg = "gray63")
    LabelPlatform = Label(PlatformMain,text="Vernam: Encrypt and Decrypt a message with a key",font="Arial 12 bold",bg='gray63')
    LabelPlatform.grid(row=0,column=2,padx=10, pady=12)
    

  


    #Encrypting section of GUI
    #Labels, text box, buttons for encryption

    # Labels
    encryptLabel = Label(PlatformMain,text="Encrypt:",bg="gray63",font="Arial 11 bold")

    LabelInstruction = Label(PlatformMain, text="Instructions: Enter a key with a message to receive encrypted message. \n File Encryption: Click Upload file button and enter a prefered key (leave message box open).",bg="gray63", font="Arial 12")

    LabelE = Label(PlatformMain, text="Key:",bg="gray63", font="Arial 12")
    LabelE1 = Label(PlatformMain, text="Message: Leave blank when uploading Text File",bg="gray63", font="Arial 11")
    LabelE2 = Label(PlatformMain, text = "Upload Text File to be encrypted:",bg="gray63", font="Arial 11")
    LabelE3 = Label(PlatformMain, text = "Encrypted message:",bg="gray63", font="Arial 11")

    LabelCypherText = Label(PlatformMain, text="", bg='gray63',font="Arial 12 bold")

    # Buttons
    EncryptBut = Button(PlatformMain, text="Encrypt", command=encryptionfinish)
    EncryptButUpload = Button(PlatformMain, text="Upload File", command=UploadTextFileEncrypt)
    

    EKeyText = Entry(PlatformMain)
    EMessageText = Entry(PlatformMain)

    #Labels,textbox and buttons Grid placing
    


    LabelInstruction.grid(row=4, column=2, sticky="W")
    encryptLabel.grid(row=3,column=2)
    LabelE.grid(row=7, column=1, sticky="W")
    LabelE1.grid(row=7, column=1, sticky="W")
    LabelE2.grid(row=8, column=1, sticky="W")
    LabelE3.grid(row=10, column=1, sticky="W")
    
    
    EKeyText = Text (fg="black", bg="powder blue",  height=5, width=25 )        # Key text box transform
    EKeyText.grid(row=6, column=2, ipadx=30, ipady=5)

    EMessageText = Text (fg="black", bg="powder blue",  height=5, width=25 )    # Message text box transform
    EMessageText.grid(row=7, column=2, ipadx=30, ipady=5)                            


    LabelCypherText.grid(row=10, column=2, padx=10, pady=10)

    
    EncryptButUpload.grid(row=8, column=2, padx=10, pady=6)
    EncryptBut.grid(row=9, column=2, padx=10, pady=2)
    LabelE.grid(row=6, column=1)
    
    
    #Decrypting Section of GUI
    #Labels,text box, buttons Decryption

    # Labels

    LabelInstructD = Label(PlatformMain, text="Instructions: Enter encryption key with encrypted message. \n File decryption: Upload encrypted file and enter encryption key (leave message box open).",bg='gray63', font="Arial 11")
    decryptLabel = Label(PlatformMain,text="Decrypt:",bg="gray63",font="Arial 12 bold")
    
    LabelD = Label(PlatformMain, text="Key:",bg='gray63', font="Arial 11")
    LabelD1 = Label(PlatformMain, text="Ciphertext:",bg='gray63', font="Arial 11")
    LabelD2 = Label(PlatformMain,text,text='Upload Encrypted Text file:',bg='gray63', font="Arial 11")
    LabelD3 = Label(PlatformMain, text="Decrypted message:", bg='gray63', font="Arial 11")

    LabelDecypherText = Label(PlatformMain, text="", bg='gray63', font="Arial 12 bold")
    DKeyText = Entry(PlatformMain)
    DCyphterText = Entry(PlatformMain)

    DecryptUploadBut = Button(PlatformMain, text="Upload File", command=UploadTextFileDecrypt)
    DecryptBut = Button(PlatformMain, text="Decrypt", command=decryptionfinish)


    #Labels, text and button Grid placing



    LabelInstructD.grid(row=12,column=2,padx=0, pady=1)
    decryptLabel.grid(row=11,column=2,padx=0, pady=1)


    LabelD.grid(row=15, column=1, sticky="W")
    LabelD1.grid(row=16, column=1, sticky="W")
    LabelD2.grid(row=17, column=1, sticky="W")
    LabelD3.grid(row =19,column=1, sticky="W")

    
    LabelDecypherText.grid(row=19, column=2)

    DKeyText = Text (fg="black", bg="powder blue",  height=5, width=25 )       # Key text box transform
    DKeyText.grid(row=15, column=2, ipadx=30, ipady=5)

    DCyphterText = Text (fg="black", bg="powder blue",  height=5, width=25 )   # Key text box transform
    DCyphterText.grid(row=16, column=2, ipadx=30, ipady=5)

    
    DecryptUploadBut.grid(row=17, column=2, padx=10, pady=10)
    DecryptBut.grid(row=18, column=2, padx=10, pady=3)

    PlatformMain.mainloop()




#Calling of functions
#uploading of text file for encryption and decryptuon
  # Call for upload of file encrypt
def UploadTextFileEncrypt():
  
    global PlatformMain
    global EMessageText

    global text
    global filename

    filename = filedialog.askopenfilename(title = "Select File",filetypes= (("text files","*.txt"),("Word files","*.docx"),("all files","*.*")),initialdir = "/") #uploading of file text, Allowing of files type
    text = readDoc(filename)

    uploadLabel = Label(PlatformMain, text="Document Uploaded",bg='gray63')
    uploadLabel.grid(row=8,column=2, sticky="E")


 # Call for upload of file decrypt
def UploadTextFileDecrypt():
   
    global PlatformMain
    global EMessageText

    global text
    global filename
    filename = filedialog.askopenfilename(title = "Select File",filetypes= (("text files","*.txt"),("Word files","*.docx"),("all files","*.*")),initialdir = "/") # Allowing of files type
    text = readDoc(filename)
    
    uploadLabel = Label(PlatformMain, text="Document Uploaded",bg='gray63')
    uploadLabel.grid(row=17, column=2, sticky="E")


# Call for functions to encrypt
def encryptionfinish():
    
    global EKeyText
    global EMessageText

    global PlatformMain
    global text
    global filename
    global LabelCypherText
    
    key = EKeyText.get("1.0", "1.0 lineend")
    plaintext = EMessageText.get("1.0","end-1c")

    LabelCypherText.config(text="")

    #If there is text then encrypt
    if EMessageText.get("1.0","end-1c") != "":                # get message from text box for encryption, if not message then upload of text file message encryption
        ciphertext = eMain(key,plaintext)                     # calling of main function, encryption 
        LabelCypherText.config(text=ciphertext)               # Display cipher text
    elif filename.endswith('.txt'):
        docText = text
        texttowrite = eMain(key,docText)
        toWrite = open(filename[:-4]+'_encrypted.txt','w')         #Write to text file of encrypted message
        for char in texttowrite:
            toWrite.write(char)
        toWrite.close()
        display = Label(PlatformMain, text= "Document has been exported",bg='gray63')
        display.grid(row=9, column=2, sticky="E")
    else:
        docText = text
        texttowrite = eMain(key, docText)
        toWrite = open(filename[:-4] +'_encrypted.docx', 'w')
        for char in texttowrite:
            toWrite.write(char)
        toWrite.close()
        display = Label(PlatformMain, text= "Document has been exported",bg='gray63')
        display.grid(row=9,column=2, sticky="E")
    
    print("encryption finished")


    # call for fynctions to decrypt
def decryptionfinish():

    global DKeyText
    global DCyphterText

    global PlatformMain
    global text
    global filename
    global LabelDecypherText

    LabelDecypherText.config(text="")
    key = DKeyText.get("1.0", "1.0 lineend")
    ciphertext = DCyphterText.get("1.0","end-1c")


    if DCyphterText.get("1.0","end-1c") != "":
        
        message = eMain(key,ciphertext)
        LabelDecypherText.config(text=message)
    elif filename.endswith('.txt'):
        docText = text
        texttowrite = eMain(key, docText)
        toWrite = open(filename[:-4] +'_decrypted.txt', 'w')
        for char in texttowrite:
            toWrite.write(char)
        toWrite.close()
        display = Label(PlatformMain, text= "Document has been exported",bg='gray63')
        display.grid(row=19,column=2, sticky="E")
    else:
        docText = text
        texttowrite = eMain(key, docText)
        toWrite = open(filename[:-4] +'_decrypted.docx', 'w')
        for char in texttowrite:
            toWrite.write(char)
        toWrite.close()
        display = Label(PlatformMain, text= "Document has been exported",bg='gray63')
        display.grid(row=18,column=2, sticky="E")


    print("Decryption finished")


#Main function call
Platformmain()
