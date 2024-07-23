import socket

serverTotal = 0
serverTotal1 = 0
clientTotal = 0
clientTotal1 = 0

host = 'localhost'  # Use 'localhost' or '127.0.0.1'
port = 12345
socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
print(host)

socket.bind((host,port))

socket.listen(5)



while True:
    communation_socket ,address = socket.accept()
    print(f"Connected to {address}")
    clientName = communation_socket.recv(1024).decode('utf-8')
    nameRequest = communation_socket.recv(1024).decode('utf-8')
    name = input("What is your name:")
    communation_socket.send(name.encode('utf-8'))
    print(f"{clientName} connected to {name}")
    #communation_socket.send("what is your name ".encode("utf-8"))
    while True:
        clientNum = int(communation_socket.recv(1024).decode())

        serverNum = int(input("\nYou-Bat: "))
        if (serverNum < 1) | (serverNum > 6):
            print("Enter number between 1 and 6")
            exit()
        else:
            communation_socket.send(str(serverNum).encode('utf-8'))
            print(f"{clientName}-Bowled: ", clientNum)
            #print(serverNum)
            if int(serverNum) == int(clientNum):
                #communation_socket.send("out".encode('utf-8'))
                #communation_socket.send(str(serverTotal).encode('utf-8'))
                print("\nYou are out ")
                print("\nYour Total Score : ",int(serverTotal))
                serverTotal1 = serverTotal
                break
            serverTotal = int(serverNum) + int(serverTotal)

    print(f"\nNow {clientName} is bating")

    while True:
        serverNum1 = int(input("\nYou-Bowl : "))
        if (int(serverNum1 < 1)) | int((serverNum1 > 6)):
            print("Enter number between 1 and 6")
            exit()
        else:
            communation_socket.send(str(serverNum1).encode('utf-8'))
            print(f"\nWaiting for {clientName} to play.........")
            clientNum1 = str(communation_socket.recv(1024).decode())
            print(f"\n{clientName} - Bat : ", clientNum1)
            if int(serverNum1) == int(clientNum1):
                print(f"\n{clientName} is out ")
                print(f"\n{clientName} Total Score : {int(clientTotal)}")
                break
            clientTotal = int(clientNum1) + int(clientTotal)
            if clientTotal > serverTotal:
                break

    if clientTotal < serverTotal:
        print(f"\nYour Total Score {serverTotal}")
        print("\nYou wins")
    else:
        print(f"\n{clientName} Wins")

    communation_socket.close()
    print(f"\nConnection with {address} ended")