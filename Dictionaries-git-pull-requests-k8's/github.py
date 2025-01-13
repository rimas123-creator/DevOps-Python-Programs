import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)

if response.status_code == 200:
    result = response.json()
    for i in result:
        username = i["user"]["login"]
        user_id = i["user"]["id"]
        print(f" logged in username: {username} and user_id: {user_id}")
else:
    print("Failed to get the response , Please Check the url...")
    