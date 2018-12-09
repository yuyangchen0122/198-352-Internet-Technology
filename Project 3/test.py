with open('PROJ3-HNS.txt') as f:
    lines = f.readlines()
f.close()

for line in lines:
    array = line.split()
    hnshostname = array[2]
    print(hnshostname)