import requests

base = "http://127.0.0.1:5000"
household = "/households"
individual = "/individuals"

# Test get/ post/ put/ patch/ delete requests for household

response = requests.get(base + household +  "")
print(response.json())

response = requests.post(base + household +  "", {})
print(response.json())

response = requests.put(base + household +  "", {})
print(response.json())

response = requests.patch(base + household +  "", {})
print(response.json())

response = requests.delete(base + household +  "")
print(response.json())

# Test get/ post/ put/ patch/ delete requests for individual

response = requests.get(base + individual +  "")
print(response.json())

response = requests.post(base + individual +  "", {})
print(response.json())

response = requests.put(base + individual +  "", {})
print(response.json())

response = requests.patch(base + individual +  "", {})
print(response.json())

response = requests.delete(base + individual +  "")
print(response.json())