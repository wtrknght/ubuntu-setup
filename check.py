import os
hostname = "192.168.10.124" #example
response = os.system("ping -n 1 " + hostname)

#and then check the response...
if response == 0:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")
