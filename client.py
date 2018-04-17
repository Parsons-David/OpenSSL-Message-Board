#!/usr/bin/python3
import argparse, json
import socket
import pickle
import state, copy

def encrypt(data):
    return data

def decrypt(data):
    return data

def print_groups(grps):
    if len(grps) < 1:
        return
    output = grps[0]
    for g in grps[1:]:
        output += " - " + g
    print()
    print(output)

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

    authenticated = False
    BUFFER_SIZE = 1024

    GROUPS = []

    try:
        while True:
            # Are you authenticated?
            if not authenticated:
                # Accept username
                usr = input("Username: ")
                # Accept password
                pwd = input("Password: ")

                u_and_p = copy.deepcopy(state.username_password)
                u_and_p['USERNAME'] = usr
                u_and_p['PASSWORD'] = pwd

                message = copy.deepcopy(state.MESSAGE)
                message['COMMAND'] = state.AUTHENTICATE
                message['BODY'] = u_and_p

                print("\tSending: %s" % (message))

                sock.send(encrypt(pickle.dumps(message)))

                # TODO : BUFFER_SIZE
                data = sock.recv(BUFFER_SIZE)

                response = pickle.loads(decrypt(data))

                print("\tReceiving: %s" % (response))

                if response['COMMAND'] != state.AUTHENTICATE:
                    print('AUTHENTICATE Reponse Error')
                    print('Recieved Reponse to Command: %s' % (response["COMMAND"]))

                authenticated = response['BODY']['AUTHENTICATED']
                GROUPS = response['BODY']['GROUPS']
                print('Authentication %s!' % ("Succesful" if authenticated else "Failed"))

            # If you are authenticated
            else:
                # TODO : Accept other commands
                print_groups(GROUPS)
                command = input("Enter a Command>> ")
                if command == 'END':
                    message = copy.deepcopy(state.MESSAGE)
                    message['COMMAND'] = state.END
                    message['BODY'] = copy.deepcopy(state.end_message)
                    print("\tSending: %s" % (message))

                    sock.send(encrypt(pickle.dumps(message)))

                    # TODO : BUFFER_SIZE
                    data = sock.recv(BUFFER_SIZE)
                    response = pickle.loads(decrypt(data))

                    print("\tReceiving: %s" % (response))

                    if response['COMMAND'] != state.END:
                        print('END Reponse Error')
                        print('Recieved Reponse to Command: %s' % (response["COMMAND"]))

                    authenticated = not response['BODY']['SESSION_ENDED']
                    print('END %s!' % ("Failed" if authenticated else "Succesful"))

                elif command == "GET":
                    pass
                elif command == "PUT":
                    pass
                else:
                    if command != '':
                        print("\'%s\' command not recognized." % (command))

    except KeyboardInterrupt as e:
        print("\nGoodbye!")

    # Close Socket Connection
    sock.close()

if __name__ == '__main__':
    main()
