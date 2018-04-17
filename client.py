#!/usr/bin/python3
import argparse, json
import requests

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
    remote_port = args['remoteport']

    # Authenticate
    response = requests.get("http://%s:%s/auth" % (destinationIP, remote_port))
    print(response.text)
    # Now Accept CLI commands until death
    try:
        while True:
            input("Enter a Command>> ")
            # Authenticate
            response = requests.get("http://%s:%s/" % (destinationIP, remote_port))
            print(response.text)

    except KeyboardInterrupt as e:
        print("\nGoodbye!")

if __name__ == '__main__':
    main()
