import socket

host = 'localhost'

socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
socket.connect((host,12345))

clientTotal = 0
clientTotal1 = 0
serverTotal = 0
serverTotal1 = 0

name = input("Whats is your name")
socket.send(name.encode("utf-8"))

socket.send("What is Your name:".encode("utf-8"))
serverName = socket.recv(1028).decode('utf-8')
print(f"{name} connected to {serverName}")

while True:
    n = int(input(f"\nYou Are Bowling : "))
    if (n < 1) | (n > 6):
        print("\nEnter number between 1 and 6")
        exit()
    else:
        socket.send(str(n).encode('utf-8'))
        print(f"\nWaiting for {serverName} to play.........")
        clientNum = (socket.recv(1024).decode('utf-8'))
        print(f"\n{serverName}-Batted: ",clientNum)
        #print(socket.recv(1024).decode('utf-8'))
        if int(n) == int(clientNum):
            print(f"\n{serverName} is out ")
            print(f" \n{serverName} Total Score : {int(serverTotal)}")
            serverTotal1 = int(serverTotal)
            break
        serverTotal = int(clientNum) + int(serverTotal)

print(f"\nNow You Are batting")

while True:
    print(f"\nYou need {serverTotal - clientTotal} to win")

    serverNum = int(socket.recv(1024).decode())
    clientNum = int(input(f'\nYou -Bat: '))

    if (clientNum < 1) | (clientNum > 6):
        print("Enter number between 1 and 6")
        exit()
    else:
        socket.send(str(clientNum).encode('utf-8'))
        print(f"{serverName}:Bowled ", serverNum)
        # print(serverNum)
        if int(clientNum) == int(serverNum):
            socket.send("out".encode('utf-8'))
            # communation_socket.send(str(serverTotal).encode('utf-8'))
            print(f"\nYou Are out ")
            print(f"Your Total Score : {int(clientTotal)}")
            clientTotal1 = int(clientTotal)
            break
        clientTotal = int(clientNum) + int(clientTotal)

        if clientTotal > serverTotal:
            break

if clientTotal < serverTotal:
    print(f'\nYour Total : {clientTotal}')
    print(f"\n{serverName} Total Score : {int(serverTotal)}")
    print(f"\n{serverName} wins")
    print("\nYou Lost,Better luck next time.")
else:
    print(f'\nYour Total : {clientTotal}')
    print(f"\n{serverName} Total Score : {int(serverTotal)}")
    print(f"\nYou Won")


