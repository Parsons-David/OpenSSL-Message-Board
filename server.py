#!/usr/bin/python3
import argparse, json
import http.server
from http.server import HTTPServer

def main():
    # parse all the arguments to the server
    parser = argparse.ArgumentParser(description='CS 419 OpenSSL Message Board Server')
    parser.add_argument('-l','--localport', help='local port', required=False, default="8080")

    args = vars(parser.parse_args())
    local_port =  int(args['localport'])

    Handler = http.server.SimpleHTTPRequestHandler

    print('Starting Server...')
    server_address = ('', local_port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Running Server on port %d...' % (local_port))
    print('CTRL+C to close Server')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt as e:
        print('\nShutting Down Server....')

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(http.server.BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        # Determine if the user is trying to login
        if self.path == "/auth":
            message = "Logging In!"
        else:
            message = "Sending Command"

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

if __name__ == '__main__':
    main()
