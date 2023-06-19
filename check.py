import os
from time import sleep
hostname = "192.168.10.124" #example
response = os.system('ping %s -n 1' % (hostname,))

#and then check the response...
if response == 0:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")
sleep(5)
