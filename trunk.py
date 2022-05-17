while True:
    print("*"*20)
    print("Menu Trunk")
    print("*"*20)
    print("a. Add New Trunk")
    print("b. Show Trunk")
    print("z. Exit")
    print("*"*20)
    y=input("Enter the choise: ")
    print("*"*20)
    if y == "a" or y == "A":
        while True:
            file = open ("trunk-databases.txt", "a")
            lanjut = input("Enter Switch Hostname or type z to stop: ")
            if lanjut == "z" :
                break
            elif lanjut != "z":
                inter_trunk = input("Enter Interface Trunk : ")
            file.write("Switch Hostname : " + lanjut +", \t interface Trunk : " + inter_trunk +"\n" )
    elif y == "b" or y == "B" :
        file = open ("trunk-databases.txt", "r")
        print("*"*20)    
        for item in file:
            item = item.strip()
            print(item)
    elif y == "z" or y == "Z":
        break
    elif y != "a" and "A" and "b" and "B" and "z" and "Z" :
        print("\n please provide valid input!\n")