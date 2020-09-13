import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(
#     BASE + "video/1", {"name": "The King", "likes": 10, "views": 10})
# print(response.json())
# input()

data = [{"likes": 78, "name": "Joe", "views": 10000},
        {"likes": 10, "name": "Tom", "views": 5555},
        {"likes": 34, "name": "Brian", "views": 2400}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# response = requests.delete(BASE + "video/0")
# print(response)
# input()
response = requests.get(BASE + "video/2")
print(response.json())
# response = requests.put(BASE + "video/6")
# response = requests.delete(BASE + "video/0")
# print(response.json())
