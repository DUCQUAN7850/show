import requests
url = 'http://10.5.37.84:4567/quannd/'
files = {'image': open('1.PNG', 'rb')}
r=requests.post(url, files=files)
print(r.text)