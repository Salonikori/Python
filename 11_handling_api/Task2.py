# Fetch All Posts
import requests

def fetch_posts(post_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    if data:
        print(len(data))
        for i in range(5):
            print(data[i]["title"])
        print(f"Title is : {data[post_id-1]["title"]}")
        print(f"Body is : {data[post_id-1]["body"]}")
    else:
        raise Exception("Data not fetched")


def main():
    try:
        post_id = int(input("Enter post id: "))
        fetch_posts(post_id)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()