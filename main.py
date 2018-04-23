versionChat = '0.1.1'
print("# Author's: kulonful, pufit\n# Socket's-TCP chat\n# [!] Server [!]\n# [?] Version " + str(versionChat) + " [?]")

import socket as s
import sys as system
import time

socket = s.socket()
clients = []

def acceptUser(wsclient, address):
    clients.append([wsclient, address])
    print('/ new user connected /')

class serverSettings():
    port = int(input('[Settings] Input port: '))
    if port < 2000:
        print('Invalid port (2000 - 8000)')
        system.exit()
    elif port > 8000:
        print('Invalid port (2000 - 8000)')
        system.exit()
    valueClients = int(input('[Settings] Input int value of people which can connected at moment: '))
    if valueClients < 1:
        print("Clients can't be so small [> 1]")

print("Server settings:\n\tport = " + str(serverSettings.port) + '\n\tmax clients: ' + str(serverSettings.valueClients))
if input('Input [Y] for accept or [N] for decline: ').upper() == 'N':
    print('Starting canceled by admin')
    system.exit()

socket.bind(('', serverSettings.port))
socket.listen(serverSettings.valueClients)

print('Server started on ' + str(serverSettings.port) + ' port\nServer start working when all users will be connected.')

while len(clients) != serverSettings.valueClients:
    wsclient, address = socket.accept()
    print(wsclient)
    print(address)
    acceptUser(wsclient, address)

while True:
    for ws in clients:
        data = ws[0].recv(2048).decode()
        print(data)
