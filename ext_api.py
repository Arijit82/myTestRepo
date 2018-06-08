import requests, json
data=({"userid": "abc123","title": "abc","projid": "123"})
url= "http://127.0.0.1:5000/api/v1/posts"
resp_dict = requests.post(url,json=data)
print (str(resp_dict))
resp_obj= resp_dict.json()
print (str(resp_obj))


# payload = {	"title": "accounts",
# 	"userid":	"arijit",
#     "projid": "23456"
# }
# # r1=requests.post('http://127.0.0.1:5000/api/v1/posts', json=payload)
# # print(r1.text)
# r2=requests.put('http://127.0.0.1:5000/api/v1/posts', json=payload)
# print(r2.text)