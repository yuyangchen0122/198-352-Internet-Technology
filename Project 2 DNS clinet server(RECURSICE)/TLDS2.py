# Yuyang Chen  168008482 yc791
# Yuezhong Yan yy378

import threading
import time
import random
import socket as mysoc


def server2():
    try:
        tssd2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    server_binding = ('', 50001)
    tssd2.bind(server_binding)
    tssd2.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid, addr = tssd2.accept()
    print("[S]: Got a connection request from a Root Server at", addr)

    with open('PROJ2-DNSEDU.txt') as f:
        lines = f.readlines()
    f.close()

    while 1:
        data_from_server = csockid.recv(1024)
        m = data_from_server.decode('utf-8')
        if not data_from_server:
            break
        print("[C]: Data received from Root Server:", m)
        time.sleep(1)
        temp = 0
        for line in lines:
            if line.startswith(m):
                print("Hostname IPaddress A: ", line)
                tssd2.send(line.encode('utf-8'))
                time.sleep(1)
                temp = 1
                break

        if temp == 0:
                t = m + ":Hostname - Erros: HOST NOT FOUND" + "\n"
                print(t)
                csockid.send(t.encode('utf-8'))


t1 = threading.Thread(name='server2', target=server2)
t1.start()
input("Hit ENTER  to exit")

exit()