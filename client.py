import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',4040))

running = True
while running:
    raw_cmd = raw_input("Enter the command you want to send: ")
    cmd = raw_cmd.split()
    if cmd[0] == "ls":
        socket.send(cmd[0])
        listElements = socket.recv(4096)
        print listElements
    elif cmd[0] == "cd":
        socket.send(raw_cmd)
    elif cmd[0] == "mkdir":
        socket.send(raw_cmd)
    elif cmd[0] == "get":
        socket.send(cmd[0])
        print(cmd[0])
        socket.send(cmd[1])
        print(cmd[1])
        f = open("other.txt","wb")
        chunk = socket.recv(4096)
        while(chunk):
            print("got stuff")
            print(chunk)
            f.write(chunk)
            chunk = socket.recv(4096)
        f.close()
        socket.recv(4096);
        #socket.close
    elif cmd[0] == "put":
        socket.send(cmd[0])
        f = open("Test.txt","r")
        chunk = f.read(4096)
        while(chunk):
            socket.send(chunk)
            print("sent stuff")
            chunk = f.read(4096)
        f.close
        #socket.shutdown(socket.SHUT_WR)
        print socket.recv(4096)
        #socket.close
    elif cmd[0] == "exit":
        socket.send("terminate")
        socket.close()
        running = False
    else:
        print ("Unkown command: "+cmd[0])