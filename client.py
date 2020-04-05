import requests


response = requests.get('http://127.0.0.1:5000/status') #TODO: change to docker server connection
print(response.json())

response = requests.get('http://127.0.0.1:5000/messages') #TODO: change to docker server connection
print(response.json())

data = {username: 'Alex', 'text': 'Hello111'}
response = requests.post('http://127.0.0.1:5000/send', json=data) #TODO: change to docker server connection
print(response.json())
