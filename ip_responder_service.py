import os
import socket

#find the system's IP
stream = os.popen("hostname -I | awk '{print $1}' | awk '{$1=$1};1'")
host_ip = socket.gethostbyname(socket.gethostname())
print(host_ip)
print(f"host ip: {host_ip}")

#check whether we have IP_RESPONDER_IP environment variable
CUSTOM_ENV_KEY = 'IP_RESPONDER_IP'

stored_host_ip = None
try:
    stored_host_ip = os.environ[CUSTOM_ENV_KEY]

except KeyError as ke:
    #environ variable not set
    print(f"no env variable {CUSTOM_ENV_KEY}")


if len(host_ip) is 1:
    #host doesn't have any IP addr
    print("machine is offline. Cannot send mail")
    exit()
else:
    if stored_host_ip is not None:
        pass
    else:
        #env variable was not set
        #setting env variable
        os.environ[CUSTOM_ENV_KEY] = host_ip


    print(f"stored ip : {stored_host_ip}")
    print(f"host ip; {host_ip}")

    #env variable was set
    if  stored_host_ip == host_ip:
        #stored is same as current
        print(f"same ip")
        pass
        exit()
    elif stored_host_ip != host_ip and host_ip != "127.0.1.1":
        os.environ[CUSTOM_ENV_KEY] = host_ip
        print(f"different ip")
        print(f"sending mail")
        #send a mail


