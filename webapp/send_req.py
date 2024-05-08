import requests

# Define the request payload (body)
payload = {
    "username": "peter",
    "password": 1
}

# Define the request headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post('http://127.0.0.1:5000/api/login', json=payload, headers=headers)

# Print the response
print(response)
