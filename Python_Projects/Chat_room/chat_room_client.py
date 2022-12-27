import socket
import threading

#Input Nickname
nickname = input("Choose your nickname:")

#Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

#Listening to Server and Sending Nickname
def recieve():
    while True:
        try:
            #Recieve message from server or send nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

#Sending messages to Server
def write():
    while True:
        message = '{}: {}'. format(nickname, input(""))
        client.send(message.encode('ascii'))

#Start threads for the functions.
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
