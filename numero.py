import requests
import json

KEY = "542e149b960e373f919a006c90ff1492"
# numero = 40028922
numero = 00
code = "BR"
f = 2

url="http://apilayer.net/api/validate?access_key={}&number={}&country_code={}&format={}".format(KEY, numero, code, f)

reponse = requests.get(url)
data = reponse.json()
print(data)
try:
    if data["valid"] == True:
        print("Numero Existe!!!")
except Exception:
    print("Numero nao Existe!!!")