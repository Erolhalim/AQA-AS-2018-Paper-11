def SendReceiveMessages():
  Dash = [20,23,0,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,0,22,13,0,0,10,0,0,0]
  Dot = [5,18,0,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
  Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

  MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
  OutputAlphabetWithTheCode(Letter,MorseCode)
 
  #question 13
def OutputAlphabetWithTheCode(Letter,MorseCode):
    counter = 0
    length = len(Letter) - 1
    for i in range(length):
      counter = counter + 1
      print(Letter[counter],MorseCode[counter], end = ' ')


SendReceiveMessages()

