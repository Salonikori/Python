import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
''')

def list_videos():
    cursor.execute(" SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) values (?,?)" , (name,time))
    conn.commit()

def update_video(index, name, time):
    cursor.execute("UPDATE videos SET name= ?,time=? where id = ?" , (name,time,index))
    conn.commit()

def delete_video(index):
    cursor.execute("DELETE FROM videos where id = ?", (index))
    conn.commit()

def main():
    while True:
        print("\nYoutube Manager App | Choose an option ")
        print("1. List all youtube videos")
        print("2. Add a video")
        print("3. Update a video detail")
        print("4. Delete a video")
        print("5. Exit the app")

        choice = input("Enter a choice")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the time duration: ")
            add_video(name,time)
        elif choice == '3':
            index = input("Enter the index of the video: ")
            name = input("Enter the video name: ")
            time = input("Enter the time duration: ")
            update_video(index, name, time)
        elif choice == '4':
            index = input("Enter the index of video to delete: ")
            delete_video(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
    conn.close()

if __name__ == '__main__':
    main()