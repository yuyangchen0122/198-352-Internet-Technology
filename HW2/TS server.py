import numpy as mypy
import threading
import time
import random
import socket as mysoc


def readfile():
    text_file = open("PROJI-DNSTS.txt", "r")
    lines = text_file.readlines()
    text_file.close()


def ts_server():
    try:
        ss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    server_binding = ('', 60000)
    ss.bind(server_binding)
    ss.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at", addr)


    while 1:
        data_from_client = csockid.recv(1024)
        m = data_from_client.decode('utf-8')
        print("[C]: Data received from server:", m)
        csockid.sendall(reverse(m).encode('utf-8'))
        if not data_from_client:
            break
    # Close the server socket
    ss.close()
    exit()


t1 = threading.Thread(name='server', target=server)
t1.start()

input("Hit ENTER  to exit")

exit()