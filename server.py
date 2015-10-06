''' TCPServer.py
usage: python TCPServer.py PORT
Reads in text, changes all letters to uppercase, and returns
the text to the client
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library

from socket import *

#word
word = "arkansas"

#guesses,number of wrong, number of attempts
guesses = []
wrong = []
attempts = 7
output = ""


# Set port number by converting argument string to integer
serverPort = int(5555)

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

print "The server is ready to receive"

def checkduplicate(letter):
    if letter in guesses:
        return True
    else:
        return False

def checkletter(letter):

    global word
    if letter in word:
        return True
    else:
        return False

def inalpha(letter):
    if letter.isalpha():
        return True
    else:
        return False

def addword(print_word):
    global output, guesses

    word_contents = ''
    #loop through each word
    for i in range(0,len(word)):

        if word[i] in guesses:
            #if macthed add the letter to the output
            word_contents += word[i]
        else:
            #if not fill in with _
            word_contents += "_"

    if (print_word == True):
        output += word_contents
    print 'Current word: ' + word_contents
    return word_contents

#checking if the word is completed, returns BOOLEAN
def checkword():

    if word == addword(False):
        return True
    else:
        return False

def validate(letter):
    global guesses, attempts
    if inalpha(letter):
        if len(letter) > 1:
            print"letter is too long"
            addmessage("too many letters")
            return False
        else:
            if checkduplicate(letter):
                print"Client has already guessed letter"
                addmessage('already guessed that letter: ')
                return False
            if checkletter(letter):
                print"letter is in the word"
                addmessage('letter is in the word: ')
            else:
                print("letter is not in word")
                addmessage('letter is not in word: ')
                attempts -= 1
            guesses += letter
    else:
        print"letter not in the alphabet"
        addmessage('letter is not in alpha: ')

def addmessage(msg):
    global output
    output += "\n" + msg;


def sendmessage():
    global output, connectionSocket
    connectionSocket.send(output)
    output = ''




# Forever, read in sentence, convert to uppercase, and send
# Wait for connection and create a new socket
# It blocks here waiting for connection
connectionSocket, addr = serverSocket.accept()

while 1:
    letter = connectionSocket.recv(1024)
    validate(letter)

    if attempts <= 0:
        addmessage('You ran out of attempts and lost. The word was ' + word + '.')
        #sendmessage()
        #connectionSocket.close()

    else:
        if checkword():
            addmessage('You gussed the word ' + word + ' and won the game')
            #sendmessage()
            #connectionSocket.close()

        else:
            addword(True)
            addmessage('You have ' + str(attempts) + ' attempts left')
    sendmessage()


# Close connection to client but do not close welcome socket
connectionSocket.close()
