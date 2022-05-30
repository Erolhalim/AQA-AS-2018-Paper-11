import re
def sendsignals():
    dict = {
        ".":"=",
        "-":"===",
        " ":"  ",
    }
    print("Morse code opitons: space, ., -")
    User_input_morse = input("Enter Morse code")
    for i in dict.keys():
        User_input_morse = User_input_morse.replace(i,dict[i])
        print(User_input_morse)


sendsignals()