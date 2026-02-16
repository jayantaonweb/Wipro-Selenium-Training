import requests
try:

    data ={
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    # make a post request to a api endpoint
    response = requests.post("https://videogamedb.uk:443/api/v2/videogame", json = data)
    print(response)

    # check if the status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        # parse the json file
        data = response.json()
        print(data)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
