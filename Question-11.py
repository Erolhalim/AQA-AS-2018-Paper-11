

from pydoc import plain


def ReportError(plaintext):
    if plaintext.replace(' ','').isupper() == True:
        print("All character have to be uppercase\n")
    else:
        print("All character have to be in the alhpabet\n")
    SendMorseCose()

    





def SendMorseCose():
    plaintext = input("Enter your message (uppercase letters and spaces only)")
    if plaintext.replace(' ','').isupper() == True and plaintext.replace(' ','').isalpha() == True :
      plaintextlength = len(plaintext)
      MorseCode = ""
      print("eorl")
      for i in range(plaintextlength):
          plaintextletter = plaintext[i]
          if plaintextletter == " ":
              Index = 0
          else:
              Index = ord(plaintextletter) - ord('A') + 1
    else:
        ReportError()




SendMorseCose()

