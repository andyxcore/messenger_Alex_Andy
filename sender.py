import requests


response = requests.get('http://127.0.0.1:5000/status') #TODO: change to docker server connection
print(response.json())

username = 'Andrey'
password = '54321'

login_data = {
    'username': username,
    'password': password
}
response = requests.post('http://127.0.0.1:5000/login', json=login_data) #TODO: change to docker server connection
print(response.json())

while True:
    text = input()
    data = {
        'username': username,
        'password': password,
        'text': text}
    requests.post('http://127.0.0.1:5000/send', json=login_data)
    response = requests.post('http://127.0.0.1:5000/send', json=data) #TODO: change to docker server connection
print(response.json())
