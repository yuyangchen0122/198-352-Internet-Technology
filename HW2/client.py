import numpy as mypy
import threading
import time
import random

import socket as mysoc


def client():
    try:
        cs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

# Define the port on which you want to connect to the server
    port = 50010
    sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine

    server_binding = (sa_sameas_myaddr, port)

    cs.connect(server_binding)

# send a intro  message to the client.

    with open('PROJI-HNS.txt') as f:
        lines = f.readlines()
    f.close()

    print(lines)
    for line in lines:
        if not line.endswith("\n"):
            line = line + "\n"

        cs.send(line.strip("\n").encode('utf-8'))
        time.sleep(1.5)


# close the cclient socket
    cs.close()
    exit()


t2 = threading.Thread(name='client', target=client)
t2.start()
input("Hit ENTER  to exit")

exit()