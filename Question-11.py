
def SendMorseCose(MorseCode):
    plaintext = input("Enter your message (uppercase letters and spaces only)")
    plaintextlength = len(plaintext)
    MorseCode = ""
    for i in range(plaintextlength):
        plaintextletter = plaintext[i]
        if plaintextletter == " ":
            Index = 0
        else:
            Index = ord(plaintextletter) - ord('A') + 1