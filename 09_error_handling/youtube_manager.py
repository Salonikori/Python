import json

def load_videos():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    print("*"*50)
    for index,video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']} , Duration = {video['time']}")
    print("*"*50)

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the time duration: ")
    videos.append({'name': name, 'time': time})
    save_videos(videos)

def update_video(videos):
    index = int(input("Enter the index of video to update"))
    name = input("Enter new name: ")
    time = input("Enter new time: ")
    if 1<= index <=len(videos):
        videos[index-1] = {'name':name, 'time':time}
        save_videos(videos)
    else:
        print("Invalid index")


def delete_video(videos):
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_videos(videos)
    else:
        print("Invalid index")

def save_videos(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def main():
    videos = load_videos()
  
    while True:
        print("\n Youtube Manager App | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1: list_all_videos(videos)
            case 2: add_video(videos)
            case 3: update_video(videos)
            case 4: delete_video(videos)
            case 5: break
            case _: print("Invalid choice")

if __name__ =="__main__":
    main()