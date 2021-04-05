# Python script for the Python Demo Service
import socket
import sys

import systemd.daemon

passphrase = "thisu"
port = 2222


if __name__ == '__main__':

    print("starting with passphrase {} and listening on port {}".format(passphrase,str(port)))

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('', port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    # notify systemd ready
    systemd.daemon.notify('READY=1')

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()
        try:
            # Receive the data the size of expected passphrase
            while True:
                data = connection.recv(len(passphrase))
                # if data is the correct passphrase, echo it back
                if data.decode() == passphrase:
                    #print('sending data back to the client')
                    connection.sendall(passphrase)
                else:
                    break
        finally:
            # Clean up the connection
            connection.close()
