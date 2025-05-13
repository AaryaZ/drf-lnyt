import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/' 

# r= requests.get(url=URL)
# data = r.json()
# print('data',data)
# print('response',r)


data = {
    'name': 'Srushti',
    'age': 14,
    'email':'chinu@gmail.com',
    'address': 'Tere liyeee charoon aur dhundha meine mil gayiiii jo tu mujhe mil gaya saara jahaan sara yahaan ab chahooon mein kya. Mere liye sapna tha ye pyaar tera kholu aankhen samne tha mere liye yaar mera pyaar mera ab chahoon mein kya',
    'city': 'Khopoli'
}
json_data = json.dumps(data)

r=requests.post(url=URL,data= json_data)
d2= r.json()
print(d2)