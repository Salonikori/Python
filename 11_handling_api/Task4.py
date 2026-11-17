# GitHub Profile Finder

import requests

def github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, timeout=10)
    data = response.json()
    print(data)
    if response.status_code == 200:
        username = data["login"]
        name = data["name"]
        followers = data["followers"]
        following = data["following"]
        public_repo = data["public_repos"]
        profile_url = data["html_url"]
        print(username)
        print(name)
        print(followers)
        print(following)
        print(public_repo)
        print(profile_url)
    elif response.status_code == 404:
        print("Github user not found")
    else:
        print("Request failed:", response.status_code)

def main():
    username = input("Enter a github username")
    github_profile(username)

if __name__ == "__main__":
    main()