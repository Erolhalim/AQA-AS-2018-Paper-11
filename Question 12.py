def sendsignals():
    dict = {
        ".":"=",
        "-":"===",
        " ":"  ",
    }
    print("Morse code opitons: space, =, ===")
    User_input_morse = input("Enter Morse code")
    for i in range(len(User_input_morse)):
        dict.cmp(User_input_morse)


sendsignals()