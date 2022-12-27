import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = [] 

# Broadcasting message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
               index = clients.index(client)
               clients.remove(client)
               client.close()
               nickname = nicknames[index]
               broadcast('{} left!'. format(nickname).encode('ascii'))
               nicknames.remove(nickname)
               break

# Recieving/ Listening Function
def receive():
    while True:
        #Accept Connection
        client, address = server.accept()
        print("Conected with {}".format(str(address)))

        #Request Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        #Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!.'.encode('ascii'))

        #Thread for client.
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
