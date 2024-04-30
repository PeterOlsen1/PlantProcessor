import requests as r

x = r.get('http://localhost:5000/userOverlap?username=peter')
print(x)