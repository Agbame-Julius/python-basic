import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit() # exit the program if the name of the artist is not provided
 

# Making a http request to itunes server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

#saving the response as a json
obj = response.json()

for result in obj["results"]:
    print(result["trackName"])