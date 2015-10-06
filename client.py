''' TCPClient.py
usage: python TCPClient.py HOSTNAMEorIP PORT
Reads text from user, sends to server, and prints answer
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line
serverName = 'localhost'

# Set port number by converting argument string to integer
serverPort = int(5555)

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

print 'Welcome to Hangman'
while 1:
    # Get sentence from user
    sentence = raw_input('Enter a letter: ')

    # Send it into socket to server
    clientSocket.send(sentence)

    # Receive response from server via socket
    msg = clientSocket.recv(1024)
    print msg
    if 'won' in msg:
        break
    else:
        if 'lost' in msg:
            break

clientSocket.close()
