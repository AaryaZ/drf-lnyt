import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/' 

# r= requests.get(url=URL)
# data = r.json()
# print('data',data)
# print('response',r)


data = {
    'name': 'Pradyumna',
    'age': 3,
    'email':'prd@gmail.com',
    'address': 'shimmi shimmi yay shimmi yay shimmi yay',
    'city': 'Khopoli'
}
json_data = json.dumps(data)

r=requests.post(url=URL,data= json_data)
d2= r.json()
print(d2)