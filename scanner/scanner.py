
# Imports
import networkscan
import ifaddr

import socket
import sys

import optparse

# variables
passphrase = "thisu"
port = 2222



def send_to_host(to_send,host):



    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set timeout to 2 seconds
    sock.settimeout(2.0)

    # Try to connect the socket to the port where the server is listening
    server_address = (host,port)

    can_connect = False

    try:
        # connect
        sock.connect(server_address)
        can_connect = True
    except:
        pass
    # if able to connect, try sending passphrase
    if can_connect:
        try:
            # Send data
            message = str.encode(passphrase)
            sock.sendall(message)

            try:
                # try to receive passphrase back
                data = sock.recv(len(passphrase))
                # make sure sent pack right passphrase again
                data = data.decode()
                if data == passphrase:
                    # if it is, then return true
                    sock.close()
                    return True

            except:
                # assume connection was closed on server end (wrong passphrase), and close my end
                sock.close()
                pass
            
        finally:
            sock.close()
    
    return False

# Main function
if __name__ == '__main__':


    # all hosts found
    hosts = set()

    # get all networks across all adapters
    adapters = ifaddr.get_adapters()
    # all networks found
    networks = []

    for adapter in adapters:
        for ip in adapter.ips:
            network = ("%s/%s" % (ip.ip, ip.network_prefix))
            # only ipv4, not localhost, not docker and not virsh network
            if ":" not in network and str(ip.ip) != "127.0.0.1" and "docker" not in adapter.nice_name and "vir" not in adapter.nice_name:
                # convert the network IP into the network ID (a.b.c.x/y -> a.b.c.0/y)
                network = network.replace(network[network.rfind("."):network.find("/")+1],".0/")
                networks.append(network)


    # scan each network for hosts
    for network in networks:
        # Create the object
        my_scan = networkscan.Networkscan(network)
        # Run the scan of hosts using pings
        my_scan.run()
        # add all hosts to host list
        for i in my_scan.list_of_hosts_found:
            #print(i)
            hosts.add(i)

    
    for host in hosts:
        if send_to_host(passphrase,host):
            # if it was the correct one, print and done
            print(host)
            
            break


