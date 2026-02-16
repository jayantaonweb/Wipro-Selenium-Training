#1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.

import requests
from requests.exceptions import Timeout

try :
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        user = response.json()
        for i in user:
            print("Name->",i["name"],"-> Email->",i["email"])

    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")


#2. Send a GET request with query parameter userId=2 and print number of posts returned.

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts",{"userId": 2})

    if response.status_code == 200:
        posts = response.json()
        print("Number of posts:", len(posts))
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#3. Write a POST request to create a new resource and verify status code 201.

try:
    data = {
        "title": "New Post",
        "body": "This is a test post",
        "userId": 2
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

    if response.status_code == 201:
        print("Resource created successfully")
    else:
        print("Failed with status:", response.status_code)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#Explain the difference between data= and json= in requests.post().

#5. Write code to check if response status code is not 200 and raise an exception.

response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code != 200:
    raise Exception(f"Request failed with status {response.status_code}")

print("Success")


#Section 2: Intermediate Level
# 6. Fetch all users and print usernames in uppercase.
try :
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        user = response.json()
        for i in user:
            print(i["name"].upper())

    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")


# 7. Implement timeout handling (2 seconds) and catch Timeout exception.

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
    print(response.status_code)

except Timeout:
    print("Request timed out!")
# 8. Use Session object to send multiple requests and demonstrate cookie persistence.



# 9. Upload a file using requests and print server response.


# 10. Fetch posts and save response JSON into a file named posts.json.