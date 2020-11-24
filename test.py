import requests

base = 'http://localhost:5000'

household = '/households'
individual = '/individuals'

# Test get/ post/ put/ patch/ delete requests for individual

# response = requests.get(base + individual +  '')
# print(response.json())

response = requests.post(base + individual, {'nric': 's1234567d', 'name': 'abc', 'gender': 'male', 'maritalstatus': 'married', 'occupationtype': 'employed', 'annualincome': 100000, 'dateofbirth': '1990-01-01'})
print(response.json()) # 201

response = requests.post(base + individual, {'nric': 't1234567j', 'name': 'def', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 's1234567d', 'occupationtype': 'employed', 'annualincome': 200000, 'dateofbirth': '1990-02-02'})
print(response.json()) # 201

response = requests.post(base + individual, {'nric': 'f1234567n', 'name': 'ghi', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 's1234567d', 'occupationtype': 'employed', 'annualincome': 300000, 'dateofbirth': '1990-03-03'})
print(response.json()) # 409

response = requests.post(base + individual, {'nric': 'g1234567x', 'name': 'jkl', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 'g1234567x', 'occupationtype': 'employed', 'annualincome': 400000, 'dateofbirth': '1990-04-04'})
print(response.json()) # 409 

response = requests.post(base + individual, {'nric': 's2345678h', 'name': 'jkl', 'gender': 'male', 'maritalstatus': 'married', 'occupationtype': 'employed', 'annualincome': 500000, 'dateofbirth': '1990-05-05'})
print(response.json()) # 201

response = requests.post(base + individual, {'nric': 'x', 'name': 'mno', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 's2345678h', 'occupationtype': 'employed', 'annualincome': 600000, 'dateofbirth': '1990-06-06'})
print(response.json()) # 400

response = requests.post(base + individual, {'nric': 't2345678d', 'name': 'mno', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 'x', 'occupationtype': 'employed', 'annualincome': 700000, 'dateofbirth': '1990-07-07'})
print(response.json()) # 400

response = requests.post(base + individual, {'nric': 't2345678d', 'name': 'mno', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 's2345678h', 'occupationtype': 'employed', 'annualincome': 'x', 'dateofbirth': '1990-08-08'})
print(response.json()) # 400

response = requests.post(base + individual, {'nric': 't2345678d', 'name': 'mno', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 's2345678h', 'occupationtype': 'employed', 'annualincome': 900000, 'dateofbirth': 'x'})
print(response.json()) # 400

response = requests.post(base + individual, {'nric': 't2345678d', 'name': 'mno', 'gender': 'female', 'maritalstatus': 'single', 'spouse': 's2345678h', 'occupationtype': 'employed', 'annualincome': 1000000, 'dateofbirth': '1990-10-10'})
print(response.json()) # 409

response = requests.post(base + individual, {'nric': 't2345678d', 'name': 'mno', 'gender': 'female', 'maritalstatus': 'married', 'spouse': 's2345678h', 'occupationtype': 'employed', 'annualincome': 1000000, 'dateofbirth': '2100-11-11'})
print(response.json()) # 400

response = requests.get(base + individual + "?nric=s1234567d")
print(response.json()) # 200

response = requests.get(base + individual + "?annualincomebelow=500000")
print(response.json()) # 200

# response = requests.put(base + individual +  '', {})
# print(response.json())

# response = requests.patch(base + individual +  '', {})
# print(response.json())

# response = requests.delete(base + individual +  '')
# print(response.json())

# Test get/ post/ put/ patch/ delete requests for household

# response = requests.post(base + household +  '', data=
# {
#     'id': 1, 
#     'individuals': ['s1234567d'], 
#     'housingtype': 'hdb'
# })

# print(response)

# response = requests.get(base + household +  '/1')
# print(response.json())

# response = requests.put(base + household +  '', {})
# print(response.json())

# response = requests.patch(base + household +  '', {})
# print(response.json())

# response = requests.delete(base + household +  '')
# print(response.json())