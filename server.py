#!/usr/bin/python3
import argparse, json
import socket, threading
import pickle
import state, copy

def encrypt(data):
    return data

def decrypt(data):
    return data

def authenticate(data):
    return True

def get_groups():
    return ["CS", "Math", "Physics", "Security", "Art", "Music", "Sports"]

def get_messages(group):
    return [{
        "USER": "PK",
        "TIMESTAMP" : "NOW",
        "MESSAGE" : "WHAT IS UP!!"
    }]

def post_message(group, message):
    pass

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
                threading.Thread(target = self.serve_client, args = (client, address_port)).start()
        except KeyboardInterrupt as e:
            print('\nShutting Down Server....')

    def serve_client(self, client, address_port):
        authenticated = False
        BUFFER_SIZE = 1024
        while True:
            try:
                message = pickle.loads(decrypt(client.recv(BUFFER_SIZE)))
                if message:
                    print("\tReceiving: %s" % (message))
                    # Is client authenticated?
                    if not authenticated:
                        if message['COMMAND'] != state.AUTHENTICATE:
                            print('Command Error!')
                            print('Recieved \'%s\' Command. Expecting \'%s\' Command' % (response["COMMAND"], state.AUTHENTICATE))

                        u_and_p = message["BODY"]

                        authenticated = authenticate(u_and_p)

                        a_rep = copy.deepcopy(state.authentication_response)
                        a_rep['AUTHENTICATED'] = authenticated
                        a_rep['GROUPS'] = get_groups() if authenticated else []

                        response = copy.deepcopy(state.MESSAGE)
                        response['COMMAND'] = state.AUTHENTICATE
                        response['BODY'] = a_rep

                        print("\tSending: %s" % (response))
                        client.send(encrypt(pickle.dumps(response)))

                    # If Client is authenticated
                    else:
                        # TODO : Accept other commands
                        command = message["COMMAND"]
                        if command == 'END':
                            authenticated = False

                            response = copy.deepcopy(state.MESSAGE)
                            response['COMMAND'] = state.END
                            response['BODY'] = copy.deepcopy(state.end_response)
                            print("\tSending: %s" % (response))

                            client.send(encrypt(pickle.dumps(response)))

                        elif command == "GET":
                            group = message["BODY"]["GROUP"]

                            response = copy.deepcopy(state.MESSAGE)
                            response['COMMAND'] = state.GET
                            response['BODY'] = copy.deepcopy(state.get_response)

                            response['BODY']['GROUP'] = group
                            response['BODY']['MESSAGES'] = get_messages(group)
                            response['BODY']['GROUPS'] = get_groups()

                            print("\tSending: %s" % (response))

                            client.send(encrypt(pickle.dumps(response)))
                        elif command == "POST":
                            group = message["BODY"]["GROUP"]
                            new_message = message["BODY"]["MESSAGE"]

                            post_message(group, new_message)

                            response = copy.deepcopy(state.MESSAGE)
                            response['COMMAND'] = state.POST
                            response['BODY'] = copy.deepcopy(state.get_response)

                            response['BODY']['GROUPS'] = get_groups()

                            print("\tSending: %s" % (response))

                            client.send(encrypt(pickle.dumps(response)))
                        # TODO : FIXED
                        else:
                            print("\'%s\' command not recognized." % (command))
                            client.close()
                            return False

                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False



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
