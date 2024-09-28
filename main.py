import requests
import time
while True:
  valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  rancookie = ''.join((random.choice(valid_letters) for i in range(1356)))
  finalcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie
  print(finalcookie)
  time.sleep(3)
