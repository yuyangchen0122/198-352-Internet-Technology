# Yuyang Chen  168008482 yc791
# Yuezhong Yan yy378

import threading
import time
import random

import socket as mysoc


class count:
    counter = 0
    ctoTS = None


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

    with open('/Users/yuyangchen0122/Desktop/Rutger-352-Internet-Technology/Project\ 2\ DNS\ clinet\ server\(RECURSICE\)/\ PROJ2-HNS.txt') as f:
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
        time.sleep(1)
        print("[C]: Data received back from RS server and they were matched in the RS Table:", d)
        f.write(d)

    f.close()

    # close the cclient socket
    cs.close()
    exit()


t2 = threading.Thread(name='client', target=client)
t2.start()
input("Hit ENTER  to exit")

exit()