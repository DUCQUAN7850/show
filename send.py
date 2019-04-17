import requests
url = 'http://2e2aef11.ngrok.io/upload/quan'
files = {'image': open('1.PNG', 'rb')}
r=requests.post(url, files=files)
print("https://ntimg.aiservice.vn/"+str(r.text))