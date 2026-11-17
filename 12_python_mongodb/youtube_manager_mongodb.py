from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://saloni1314:abc@cluster0.66hgcsn.mongodb.net/", tlsAllowInvalidCertificates = True)

db = client["YtManager"]

video_collections = db["videos"]

print(video_collections)

def list_all_videos():
    for video in video_collections.find():
        print(f"Id = {video['_id']}, Name = {video['name']}, Time ={video['time']}")

def add_video(name, time):
    video_collections.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collections.update_one({'_id': ObjectId(video_id)},{"$set" : {'name': new_name, 'time':new_time}})

def delete_video(video_id):
    video_collections.delete_one({'_id' : ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager with Mongodb")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video detail")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter a choice: ")
        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video id to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()