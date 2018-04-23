versionChat = '0.1.1'
print("# Author's: kulonful, pufit\n# Socket's-TCP chat\n# [!] Server [!]\n# [?] Version " + str(versionChat) + " [?]")

import sys
import socket as s

socket = s.socket()
socket.connect(('localhost', 3000))

while True:
    dSend = input().encode()
    socket.send(dSend)