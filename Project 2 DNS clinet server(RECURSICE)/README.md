# Rutger-CS352-Internet-Technology
Rutger CS352 Internet Technology

@Author: Yuyang Chen  168008482   yc791
@Author: Yuezhong Yan 166000555 yy378

1. I will start both TS servers followed by the name of the input file(on two random ilab machines)
like this:
python ./TSCOM.py PROJ2-DNSCOM.txt 
python ./TSEDU.py PROJ2-DNSEDU.txt
2. I will start the RS server and pass it a command line argument containing the hostname of the .com server followed by the hostname of the .edu server  followed by the name of the input file(On a third Ilab machine)
like this:
python ./RS.py $TSCOMHOSTNAME $TSEDUHOSTNAME  PROJ2-DNSRS.txt
(Replace $TSCOMHOSTNAME with the hostname of the computer you started the COM ts server on)
(Replace $TSEDUHOSTNAME with the hostname of the computer you started the EDU ts server on)
3. I will start the client on a fourth ilab machine passing the hostname of the RS server as a command line argument followed by the name of the input file
like this
python ./CLIENT.py $RSHOSNAME PROJ2-HNS.txt
(Replace $RSHOSNAME with the hostname of the computer you started the RS server on)
4. I will check a file called RESOLVED.txt and see if the correct answers are there (note the correct answers should be one answer per line  either hostname ipadress A or Error: HOST NOT FOUND)
