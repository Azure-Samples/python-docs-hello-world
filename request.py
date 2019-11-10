import requests
import json

url = 'https://ahbilalfifthapp.scm.azurewebsites.net/api'

data = [[1, 1, 70, 1, 1, 100.25]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)

#Pclass     1.0000
#Sex        1.0000
#Age        4.0000
#SibSp      0.0000
#Parch      2.0000
#Fare      81.8583