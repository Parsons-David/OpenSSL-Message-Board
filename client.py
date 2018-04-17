#!/usr/bin/python3
import argparse, json
import socket

def login(authentication_dict):
    # Takes in body of json dictionary used to authenticate
    # Sends GET request to the "/login" resource
    # Returns
    # {
    #     "authenticated" : True or False,
    #     "Response" : "<Response Message>"
    # }
    pass

def main():
    # parse all the arguments to the client
    parser = argparse.ArgumentParser(description='CS 419 OpenSSL Message Board Client')
    parser.add_argument('-d','--destination', help='Destination IP Host', required=False, default='127.0.0.1')
    parser.add_argument('-p','--remoteport', help='remote port', required=False, default='8080')

    args = vars(parser.parse_args())
    destinationIP = args['destination']
    remote_port = int(args['remoteport'])

    # Build Socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Attempt Connection to MessageBoardServer
    sock.connect((destinationIP, remote_port))

    message = "TEST"

    try:
        while True:

            # Sends Message to MessageBoardServer
            sock.send(message.encode('ascii'))

            # Recive Response Data from MessageBoardServer
            data = sock.recv(1024)

            # String reprsentation of data recieved from the server
            print('Received from the server :',str(data.decode('ascii')))

            # Wait for END command
            # TODO : Accept other commands
            ans = input("Enter a Command>> ")
            if ans == 'END':
                break
                
    except KeyboardInterrupt as e:
        print("\nGoodbye!")

    # Close Socket Connection
    sock.close()

if __name__ == '__main__':
    main()
