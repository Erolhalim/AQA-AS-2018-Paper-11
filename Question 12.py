def sendsignals():
    dict = {
        ".":"=",
        "-":"===",
        " ":"  ",
    }
    print("Morse code opitons: space, ., -")
    MorseCodeString = input("Enter Morse code: s")
    for i in dict.keys():
        MorseCodeString = MorseCodeString.replace(i,dict[i])
        print(MorseCodeString)


sendsignals()