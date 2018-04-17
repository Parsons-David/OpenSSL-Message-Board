#!/usr/bin/python3
import argparse, json
import socket, threading

# Correct Name?
MAX_CLIENTS = 10
# Connection Timeout in seconds
CONNECTION_TIMEOUT = 60
# Lock for accessing client data
# Authentication lock
# Lock for message data

class MessageBoardServer():
    def __init__(self, ip, port):
        print('Starting Server...')
        self.ip = ip
        self.port = port
        # TODO : !!!!!!!
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # TODO : !!!!!!!
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        print('Running Server on port %d...' % (self.port))

    def listen(self):
        self.sock.listen(MAX_CLIENTS)
        print('CTRL+C to close Server')
        try:
            while True:
                # Accept a new client connection
                client, address_port = self.sock.accept()
                # Set timeout for new client
                client.settimeout(CONNECTION_TIMEOUT)
                # Spawn thread to handle new client interations
                # Starts by authenticating the client
                threading.Thread(target = self.authenticate_client, args = (client, address_port)).start()
        except KeyboardInterrupt as e:
            print('\nShutting Down Server....')

    def authenticate_client(self, client, address_port):
        print("Authenticating Client: %s" % (str(address_port)))
        self.listenToClient(client, address_port)

    def listenToClient(self, client, address):
        BUFFER_SIZE = 1024
        while True:
            try:
                data = client.recv(BUFFER_SIZE)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    # parse all the arguments to the server
    parser = argparse.ArgumentParser(description='CS 419 OpenSSL Message Board Server')
    parser.add_argument('-l','--localport', help='local port', required=False, default="8080")

    args = vars(parser.parse_args())
    local_port =  int(args['localport'])


    MessageBoardServer('',local_port).listen()
    print('Goodbye!')
