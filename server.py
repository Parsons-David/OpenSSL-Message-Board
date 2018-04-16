#!/usr/bin/python3
import argparse, json
from http.server import HTTPServer

def test():
    print("Handled")

def main():
    # parse all the arguments to the server
    parser = argparse.ArgumentParser(description='CS 419 OpenSSL Message Board Server')
    parser.add_argument('-l','--localport', help='local port', required=False, default="8080")
    args = vars(parser.parse_args())
    local_port =  int(args['localport'])

    print('Starting Server...')
    server_address = ('', local_port)
    httpd = HTTPServer(server_address, test)
    print('Running Server on port %d...' % (local_port))
    httpd.serve_forever()

if __name__ == '__main__':
    main()
