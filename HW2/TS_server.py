# Yuyang Chen  168008482 yc791
# Yuezhong Yan yy378

import numpy as mypy
import threading
import time
import random
import socket as mysoc


def server():
    try:
        tssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    server_binding = ('', 50012)
    tssd.bind(server_binding)
    tssd.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid, addr = tssd.accept()
    print("[S]: Got a connection request from a client at", addr)

    with open('PROJI-DNSTS.txt') as f:
        lines = f.readlines()
    f.close()

    while 1:
        data_from_client = csockid.recv(1024)
        m = data_from_client.decode('utf-8')
        if not data_from_client:
            break
        print("[C]: Data received from client:", m)
        time.sleep(1)
        temp = 0
        for line in lines:
            if line.startswith(m):
                print("Hostname IPaddress A: ", line)
                csockid.send(line.encode('utf-8'))
                time.sleep(1)
                temp = 1
                break

        if temp == 0:
                t = m + ":Hostname - Erros: HOST NOT FOUND" + "\n"
                print(t)
                csockid.send(t.encode('utf-8'))


t1 = threading.Thread(name='server', target=server)
t1.start()
input("Hit ENTER  to exit")

exit()
