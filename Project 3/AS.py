import sys
import socket as mysoc
import threading
import time


def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
        
    server_binding=('', 5001)
    # Set up socket
    ss.bind(server_binding)
    ss.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid,addr=ss.accept()
    print("[S]: Got a connection request from a client at", addr)

    try:
        # Create socket for tlds_com Server
        tlds1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[RS]: Socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    try:
        # Create socket for tlds_edu Server
        tlds2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[RS]: Socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    # Define the port on which you want to connect to the com server
    tlds1_port = 8888
    tlds1_ip = mysoc.gethostbyname("cpp.cs.rutgers.edu")
    server_binding1 = (tlds1_ip,tlds1_port)
    tlds1.connect(server_binding1)

    # Define the port on which you want to connect to edu the server
    tlds2_port = 8891
    tlds2_ip = mysoc.gethostbyname("java.cs.rutgers.edu")
    server_binding2 = (tlds2_ip,tlds2_port)
    tlds2.connect(server_binding2)


# loop which receives data from the client

    more_messages = True
    while more_messages:
        data_from_client = csockid.recv(1024)
        msg = data_from_client.decode('utf-8')
        print("[S]: Data Received: ", msg)
        if(msg.strip() == "disconnecting"):
            # If disconnecting, break out of the loop and close the tlds_servers
            tlds1.send("disconnecting".encode('utf-8'))
            tlds2.send("disconnecting".encode('utf-8'))
            more_messages = False
        else:
            array = msg.split()
            challenge = array[0]
            digest = array[1]
            tlds1.send(challenge.strip().encode('utf-8'))
            time.sleep(1)
            tlds2.send(challenge.strip().encode('utf-8'))
            time.sleep(1)
            data_from_tlds1 = tlds1.recv(1024)
            D1 = data_from_tlds1.decode('utf-8')
            print(D1)
            data_from_tlds2 = tlds2.recv(1024)
            D2 = data_from_tlds2.decode('utf-8')
            print(D2)
            if(digest == D1):
                csockid.send("TLDS1".encode('utf-8'))
            elif(digest == D2):
                csockid.send("TLDS2".encode('utf-8'))

        # Close the server socket
    ss.close()
# close other sockets
# tlds_edu.close()
# tlds_com.close()


def contact_server(socket, message):
    socket.send(message.rstrip().encode('utf-8'))
    print("[RS]: Data sent to tlds server:", message)
    # Send the data to the Server and announce it
    data_from_server = socket.recv(1024).decode('utf-8')
    # Receive data from server, announce and decode it
    print("[RS]: Data received from tlds:", data_from_server)
    return data_from_server


def create_dict(filepath):
    dns = {}
    for x in open(filepath, "r"):
        if x == '':
            continue
        split_string = x.split();
        dns[split_string[0]] = [split_string[1], split_string[2]]
    return dns


t1 = threading.Thread(name='server', target=server)
t1.start()

input("Hit ENTER  to exit")

exit()