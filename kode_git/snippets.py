# We can customize a URLs query string, i.e if we want to do a search. In requests we can use the params keyword argument which takes a dictionary of strings.
url = "https://www.google.com/maps/search/?api=1"

query = "Universitetet i Bergen/"
params = {"query": query}
# Make a GET request:
response = requests.get(url=url, params=params, allow_redirects=False)
# Print URL string used in the request above:
print(f"Requested URL: {response.url}")


###
# Authorization Header: When we dont have username+password, and want to use an access token instead.
url = "https://postman-echo.com/basic-auth"
headers = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
# The GET request:
response = requests.get(url=url, headers=headers)
print(f"The response status is {response.status_code}\n")
try:
    print(f'Response JSON:\n{response.json()}')
except:
    print('Response is not JSON')
  ###


###