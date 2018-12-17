import sys
import threading
import socket as mysoc
import hmac
import time

# NOTE: this file is identicle to TSCOM.py except for the port number


def server():
    try:
        ss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',8888) # Set up socket
    ss.bind(server_binding)
    ss.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    # Accept connection request
    print("[S]: Got a connection request from a client at", addr)

    try:
        tlds1client=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding = ('', 8002) # Set up socket
    tlds1client.bind(server_binding)
    tlds1client.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    cs,addr=tlds1client.accept()
    # Accept connection request
    print("[S]: Got a connection request from a client at", addr)

    with open('PROJ3-TLDS1.txt') as f:
        lines = f.readlines()
    f.close()

    with open('PROJ3-KEY1.txt') as f:
        keys = f.readlines()
    f.close()

    more_messages = True
    while more_messages:
        data_from_as = csockid.recv(1024)
        # Receive data from client
        msg = data_from_as.decode('utf-8')
        print("[S]: Data Received: ", msg)

        if(msg.strip() == "disconnecting"):
            more_messages = False
        else:
            print(msg)
            key = keys[0]
            d1 = hmac.new(key.encode(), msg.encode("utf-8"))
            digest = d1.hexdigest()
            print(digest)
            csockid.send(digest.encode('utf-8'))
            time.sleep(1)
            data_from_client = cs.recv(1024)
            hnshostname = data_from_client.decode('utf-8')
            time.sleep(1)
            print(hnshostname)
            temp = 0
            if not (hnshostname.strip() == "xxxx"):
                for line in lines:
                    if line.startswith(hnshostname):
                        print("Hostname IPaddress A: ", line)
                        cs.send(line.encode('utf-8'))
                        temp = 1

                if temp == 0:
                    error = "Error: HOST NOT FOUND\n"
                    print(error)
                    cs.send(error.encode('utf-8'))

    ss.close()


t2 = threading.Thread(name='server', target=server)
t2.start()
input("Hit ENTER  to exit")

exit()