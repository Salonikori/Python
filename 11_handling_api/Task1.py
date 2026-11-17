#Fetch Random User Details

import requests

def fetch_api():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    if data:
        name = data[0]["name"]
        email = data[0]["email"]
        city = data[0]["address"]["city"]
        company = data[0]["company"]["name"]
        return name,email,city,company
    else:
        raise Exception("Data not fetched")

def main():
    try:
        name, email, city, company = fetch_api()
        print(f"name = {name}, email ={email}, city = {city}, company = {company}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()



