import json

def load_data():
    """Loads videos data from the file."""
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    finally:
        print("Loaded data!")

def save_data(videos):
    """Saves videos data to the file."""
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    """Prints a formatted list of all videos."""
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

def add_video(videos):
    """Prompts the user to add a new video and saves it."""
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_video(videos):
    """Prompts the user to select and update a video's details."""
    list_all_videos(videos)
    index = int(input("Enter the number of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data(videos)
    else:
        print("Invalid index selected.")

def delete_video(videos):
    """Prompts the user to select and delete a video."""
    list_all_videos(videos)
    index = int(input("Enter the number of the video to delete: "))
    if 1 <= index <= len(videos):
        deleted_video = videos.pop(index - 1)
        print(f"Deleted video: {deleted_video['name']}")
        save_data(videos)
    else:
        print("Invalid index selected.")

def main():
    """Main program loop."""
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice in ('1', '2', '3', '4', '5'):
            match choice:
                case '1':
                    list_all_videos(videos)
                case '2':
                    add_video(videos)
                case '3':
                    update_video(videos)
                case '4':
                    delete_video(videos)
                case '5':
                    break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
