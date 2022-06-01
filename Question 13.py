from typing import Counter


def DisplayMenu():
  print()
  print("Main Menu")
  print("=========")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print("A - Display")
  print("X - Exit program")
  print()

  
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
      if 3 == counter:
        counter = counter + 1
        print(Letter[counter],MorseCode[counter],'\n')
      elif 7 == counter:
        counter = counter + 1
        print(Letter[counter],MorseCode[counter],'\n')
      elif 11 == counter:
        counter = counter + 1
        print(Letter[counter],MorseCode[counter],'\n')
      elif 15 == counter:
        counter = counter + 1
        print(Letter[counter],MorseCode[counter],'\n')
      elif 19 == counter:
        counter = counter + 1
        print(Letter[counter],MorseCode[counter],'\n')
      elif 23 == counter:
        counter = counter + 1
        print(Letter[counter],MorseCode[counter],'\n')
      else:
        counter = counter + 1 
        print(Letter[counter],MorseCode[counter],end = '')


def DisplayMenu():
  print("Main Menu")
  print("=========")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print("X - Exit program")
  print("A - Exit program")


def GetMenuOption():
  MenuOption = ''
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption




DisplayMenu() 
MenuOption = input("Enter your choice: ")
if MenuOption == 'R':
  ReceiveMorseCode(Dash, Letter, Dot)
elif MenuOption == 'S':
  SendMorseCode(MorseCode) 
elif MenuOption == 'X':
  ProgramEnd = True
elif MenuOption == 'A':
  SendReceiveMessages()











