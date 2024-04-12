import requests

server_request = requests.get("https://www.google.com")
status_code = server_request.status_code
print(status_code)

if status_code == 200:
    print ("You are connected")
else:
    print("You are not connected")
