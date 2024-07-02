import json


# to load the data
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# data (video) saving (update / add) helper
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        return json.dump(videos, file)


# to list all the videos using enumerate to add the indexing
def list_all_videos(videos):
    print("\n")
    print("*" * 70)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

    print("\n")
    print("*" * 70)


# to add videos taking user input first
def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video length: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


# to update the video list
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Ivalid index selected")


# to delete the video from the list
def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected!")


videos = load_data()


# entry point of the application
def main():
    while True:
        print("\n Youtube Manager | choose an option below")
        print("1. List all youtube videos: ")
        print("2. Add youtube video")
        print("3. Update youtube video details")
        print("4. Delete youtube video")
        print("5. Exit the app")

        print("\n")

        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


# to call the main function
if __name__ == "__main__":
    main()
