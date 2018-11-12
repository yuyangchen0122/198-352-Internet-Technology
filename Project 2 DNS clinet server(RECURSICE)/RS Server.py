# Yuyang Chen  168008482 yc791
# Yuezhong Yan yy378

import threading
import time
import socket as mysoc
import sys

port_tlds1 = 5000
port_tlds2 = 7777


#
# def connect_to_tlds1():
#     try:
#         tlds1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
#         count.ctoTLDS1 = tlds1
#         print("[C]: Connect to TLDS1")
#     except mysoc.error as err:
#         print('{} \n'.format("socket open error ", err))
#
#     port_tlds1 = 50000
#     sa_sameas_myaddr = mysoc.gethostbyname()
#     server_binding1 = (sa_sameas_myaddr, port_tlds1)
#     tlds1.connect(server_binding1)
#     return tlds1
#
#
# def connect_to_tlds2():
#     try:
#         tlds2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
#         count.ctoTLDS2 = tlds2
#         print("[C]: Connect to TLDS2")
#     except mysoc.error as err:
#         print('{} \n'.format("socket open error ", err))
#
#     port_tlds2 = 50001
#     sa_sameas_myaddr = mysoc.gethostbyname()
#     server_binding2 = (sa_sameas_myaddr, port_tlds2)
#     tlds2.connect(server_binding2)
#     return tlds2


def server():

    try:
        tlds1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Connect to TLDS1")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    # sa_sameas_myaddr1 = mysoc.gethostbyname()
    host1 = mysoc.gethostname(inputhostname1)
    server_binding1 = (mysoc.gethostbyname(host1), port_tlds1)
    tlds1.connect(server_binding1)


    try:
        tlds2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Connect to TLDS2")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    # sa_sameas_myaddr2 = mysoc.gethostbyname("kill.cs.rutgers.edu")
    host2 = mysoc.gethostname(inputhostname2)
    server_binding2 = (mysoc.gethostbyname(host2), port_tlds2)
    tlds2.connect(server_binding2)

    try:
        ss = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    server_binding = ('', 5004)
    ss.bind(server_binding)
    ss.listen(1)
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip = (mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ", localhost_ip)
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at", addr)

    with open(inputtextname) as f:
        lines = f.readlines()
    f.close()

    while 1:
        time.sleep(0.25)
        data_from_client = csockid.recv(1024)
        m = data_from_client.decode('utf-8')
        if not data_from_client:
            break
        print("[C]: Data received from client:", m)
        temp = 0
        for line in lines:
            if line.strip('\n').startswith(m):
                print("Hostname IPaddress A: ", line)
                csockid.send((line.strip('\n')+'\n').encode('utf-8'))
                temp = 1
        time.sleep(0.25)

        if temp == 0:
            if m.endswith(".com"):
                tlds1.send(m.strip("\n").encode('utf-8'))
                data_from_server1 = tlds1.recv(100)
                s1 = data_from_server1.decode('utf-8')

                print("[C]: Data received from TLDS1:", s1)
                csockid.send(s1.encode('utf-8'))

            elif m.endswith(".edu"):
                tlds2.send(m.strip("\n").encode('utf-8'))
                time.sleep(1)
                data_from_server2 = tlds2.recv(100)
                s2 = data_from_server2.decode('utf-8')

                print("[C]: Data received from TLDS2:", s2)
                csockid.send(s2.encode('utf-8'))

            else:
                csockid.send("Error: HOST NOT FOUND\n".encode('utf-8'))

        # data_from_server1 = tlds1.recv(100)
        # s1 = data_from_server1.decode('uft-8')
        # if not data_from_server1:
        #     break
        # print("[C]: Data received from TLDS1:", s1)
        # csockid.send(s1.encode('utf-8'))
        # time.sleep(1)
        #
        # data_from_server2 = tlds2.recv(100)
        # s2 = data_from_server2.decode('uft-8')
        # if not data_from_server2:
        #     break
        # print("[C]: Data received from TLDS2:", s2)
        # csockid.send(s2.encode('utf-8'))
        # time.sleep(1)

    # Close the server socket
    ss.close()
    exit()

# take user input
# your code


if __name__ == "__main__":
    inputhostname1 = sys.argv[1]
    inputhostname2 = sys.argv[2]
    inputtextname = sys.argv[3]

    t1 = threading.Thread(name='server', target=server)
    t1.start()

    input("Hit ENTER  to exit")

exit()