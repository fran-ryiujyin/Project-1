#Import Necessary Module
from socket import *
import time as t

startTime = t.time()
if __name__ == "_main_":
    host = input("Input Host to Scanned")
    ip = gethostbyname(host)
    print ('Starting scan on host: ', ip)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((ip, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()
print('Time taken:', t.time() - startTime)