import socket as mysoc
import sys
import hmac
import threading
import time


def client():
    try:
        rs_socket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket RS created\n")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    rs_port = 5001
    rs_ip = mysoc.gethostbyname(mysoc.gethostname())
    print(rs_ip)
    rs_socket.connect((rs_ip, rs_port))
    time.sleep(1)
    output_file = open('RESOLVED.txt', 'w')  # open the RESOLVED.txt file in write mode

    try:
        # Create socket for tlds_com Server
        tlds1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[RS]: Socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    port_tlds1 = 8002
    tlds1_ip = mysoc.gethostbyname("cpp.cs.rutgers.edu")
    server_binding1 = (tlds1_ip,port_tlds1)
    tlds1.connect(server_binding1)
    time.sleep(1)

    try:
        # Create socket for tlds_edu Server
        tlds2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[RS]: Socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))

    port_tlds2 = 9002
    tlds2_ip = mysoc.gethostbyname("java.cs.rutgers.edu")
    server_binding2 = (tlds2_ip,port_tlds2)
    tlds2.connect(server_binding2)
    time.sleep(1)

    with open('PROJ3-HNS.txt') as f:
        lines = f.readlines()
    f.close()

    for line in lines:
        array = line.split()
        time.sleep(1)
        c1 = array[1]
        key = array[0]
        hnshostname = array[2]
        d1 = hmac.new(key.encode(), c1.encode("utf-8"))
        digest = d1.hexdigest()
        message = c1 + " " + digest
        print(message)

        rs_socket.send(message.strip().encode('utf-8'))  # First sends the host name to the RS Server
        time.sleep(1.5)
        data_from_as = rs_socket.recv(100)
        servername = data_from_as.decode('utf-8')  # Then receives result
        time.sleep(1)
        if(servername.strip() == "TLDS1"):
            tlds1.send(hnshostname.strip().encode('utf-8'))
            tlds2.send("xxxx".encode('utf-8'))
            data_from_tlds1 = tlds1.recv(1024)
            name1 = data_from_tlds1.decode('utf-8')
            print("TLDS1" + " " + name1)
            output_file.write("TLDS1" + " " + name1)
        elif(servername.strip() == "TLDS2"):
            tlds2.send(hnshostname.strip().encode('utf-8'))
            tlds1.send("xxxx".encode('utf-8'))
            data_from_tlds2 = tlds2.recv(1024)
            name2 = data_from_tlds2.decode('utf-8')
            print("TLDS2" + " " + name2)
            output_file.write("TLDS2" + " " + name1)

    rs_socket.send('disconnecting'.encode('utf-8'))
    tlds1.close()
    tlds2.close()
    rs_socket.close()

    output_file.close()


t1 = threading.Thread(name='client', target=client)
t1.start()

input("Hit ENTER to exit")

exit()