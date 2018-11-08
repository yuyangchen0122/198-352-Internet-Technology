# Yuyang Chen  168008482 yc791
# Yuezhong Yan yy378

import numpy as mypy
import threading
import time
import random

import socket as mysoc


class count:
    counter = 0
    ctoTS = None


def connect_to_ts():
    try:
        ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        count.ctoTS = ts
        print("[C]: Connect to TS")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    port_ts = 50112
    sa_sameas_myaddr = mysoc.gethostbyname("grep.cs.rutgers.edu")
    server_binding1 = (sa_sameas_myaddr, port_ts)
    ts.connect(server_binding1)
    return ts


def client():
    try:
        cs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    # Define the port on which you want to connect to the server
    port = 50020
    sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())
    # connect to the server on local machine

    server_binding = (sa_sameas_myaddr, port)

    cs.connect(server_binding)

    # send a intro  message to the client.

    with open('PROJI-HNS.txt') as f:
        lines = f.readlines()
    f.close()

    # Make the output file
    f = open("RESOLVED.txt", "w")

    print(lines)
    for line in lines:
        if not line.endswith("\n"):
            line = line + "\n"

        cs.send(line.strip("\n").encode('utf-8'))
        time.sleep(1.5)

        data_from_server = cs.recv(1024)
        d = data_from_server.decode('utf-8')
        if d.endswith("A") or d.endswith("A\n"):
            time.sleep(1)
            print("[C]: Data received back from RS server and they were matched in the RS Table:", d)
            f.write(d)

        if d.endswith("NS") or d.endswith("NS\n"):
            time.sleep(1)
            print("[C]: Data received from RS server and end with 'NS':", d)
            if count.ctoTS is None:
                count.ctoTS = connect_to_ts()

            count.ctoTS.send(line.strip("\n").encode('utf-8'))
            time.sleep(1)

            data_from_ts_server = count.ctoTS.recv(1024)
            ts_message = data_from_ts_server.decode('utf-8')
            if ts_message.endswith('A') or ts_message.endswith('A\n'):
                print("[C]: Data received back from TS server and they were matched in the TS Table", ts_message)
                f.write(ts_message)
            else:
                print("[C]: HostName - Error: HOST NOT FOUND", ts_message)
                f.write(ts_message)
    f.close()

    # close the cclient socket
    cs.close()
    exit()


t2 = threading.Thread(name='client', target=client)
t2.start()
input("Hit ENTER  to exit")

exit()