import time
from datetime import datetime as dt

temphost = "hosts" #host file used by windows firewall
hostpath = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1" #localhost ip address
sitelist = ["www.facebook.com", "facebook.com", "mail.google.com", ] #list of sites to be blocked

start = int(input("Enter starting time for site blocker\n"))
end = int(input("Enter ending time for site blocker\n"))

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end): #condition to check if current time is between the user defined blocking period
        with open(temphost, "r+") as hostfile:
            content = hostfile.read()
            for site in sitelist:
                if site in content:
                    pass
                else:
                    hostfile.write("\n" + redirect + " 	" + site) #add site to hosts file
    else: #if the current time is not between the user defined period
        with open(temphost, "r+") as hostfile:
            content = hostfile.readlines()
            hostfile.seek(0)
            for line in content:
                if not any(site in line for site in sitelist):
                    hostfile.write(line) #remove the blocked sites from the hosts file
            hostfile.truncate() #delete the repeated lines from the file
    time.sleep(5) #pause for this duration before checking the condition again