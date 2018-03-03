def evenOrOddLassi(b,type):
    if (type == "even") or (type == "odd"):
        x = 1 if type == "odd" else 0
        pass
    else:
        return

    for lassi in range(1,b):

        if lassi%2 == x:
            print("Lassi: ", lassi)


def myFunction():
    for lassi in range(1,11):
        if lassi > 5:
            print("Lassi: "+str(lassi))


def lassiBet(b):
    for lassi in range(1,b):
        if lassi > 5:
            print("Lassi: "+ str(lassi))



evenOrOddLassi(10, "even")