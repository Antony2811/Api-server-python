import requests

# Define the base URL for the API server
base_url = "http://localhost:5000"

# Define the endpoints we want to consume
time_endpoint = base_url + "/time"
date_endpoint = base_url + "/date"
hello_endpoint = base_url + "/hello"

# Send requests to the API server and print the responses
time_response = requests.get(time_endpoint)
print("Current time:", time_response.text)

date_response = requests.get(date_endpoint)
print("Current date:", date_response.text)

hello_response = requests.get(hello_endpoint)
print("Server message:", hello_response.text)
