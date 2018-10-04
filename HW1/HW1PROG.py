import numpy as mypy
import threading
import time
import random

import socket as mysoc


def server():
    try:
        ss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at", addr)
    # send a intro  message to the client.
    msg = "Welcome to CS 352"
    csockid.send(msg.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()


def client():
    try:
        cs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    # Define the port on which you want to connect to the server
    port = 50007
    sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())
    # connect to the server on local machine
    server_binding = (sa_sameas_myaddr, port)
    cs.connect(server_binding)
    data_from_server = cs.recv(100)
    # receive data from the server

    print("[C]: Data received from server::  ", data_from_server.decode('utf-8'))
    # close the cclient socket
    cs.close()
    exit()


t1 = threading.Thread(name='server', target=server)
t1.start()
time.sleep(random.random() * 5)
t2 = threading.Thread(name='client', target=client)
t2.start()

input("Hit ENTER  to exit")

exit()
