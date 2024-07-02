import sqlite3

# connect DB
con = sqlite3.connect("youtube_videos.db")
cur = con.cursor()

# creating DB structure
cur.execute(
    """ 
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            
    )
"""
)


def list_videos():
    cur.execute("SELECT * FROM videos")

    for row in cur.fetchall():
        print("\n")
        print("*" * 70)

        print(row)

        print("\n")
        print("*" * 70)


def add_videos(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


def update_video(video_id, new_name, new_time):
    cur.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()


def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_videos(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Bye Bye !")
            break
        else:
            print("Invalid Choice !")

    # DB connection closed
    con.close()


if __name__ == "__main__":
    main()
