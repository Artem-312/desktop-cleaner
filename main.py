import os
import shutil
import time
from apscheduler.schedulers.background import BackgroundScheduler


# Define the mapping of file extensions to destination folders
destination_folders = {
    ".txt": os.path.join(os.path.expanduser("~"), "Desktop", "Sorting", "Text files"),
    ".pdf": os.path.join(os.path.expanduser("~"), "Desktop", "Sorting", "PDF files"),
    ".jpg": os.path.join(os.path.expanduser("~"), "Desktop", "Sorting", "JPG files"),
    # Add more extensions and corresponding destination folders as needed
}

source_directory = ""


def sort_files_by_extension(source_dir, destination_fold):
    try:
        # Get a list of files in the source directory
        files = os.listdir(source_dir)

        # Iterate through the files
        for file in files:
            # Get the file extension
            file_extension = os.path.splitext(file)[1]

            # Check if the file extension is in the destination folders mapping
            if file_extension in destination_fold:
                # Get the destination folder for the file extension
                destination_folder = destination_fold[file_extension]

                # Create the destination folder if it doesn't exist
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file to the destination folder
                source_path = os.path.join(source_dir, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(source_path, destination_path)
                print(f"Moved {file} to {destination_folder}")

        print("File sorting completed successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    # Get the user's home directory
    home_directory = os.path.expanduser("~")

    # Relative path to the source directory
    source_directory = os.path.join(home_directory, "Desktop")


# Create the destination folders if they don't exist
for folder in destination_folders.values():
    os.makedirs(folder, exist_ok=True)

# Create the scheduler
scheduler = BackgroundScheduler()

# Schedule the task to run every 30 minutes
scheduler.add_job(sort_files_by_extension, trigger='interval', minutes=30,
                  args=[source_directory, destination_folders])

# Start the scheduler
scheduler.start()

# Keep the script running to let the scheduler execute the tasks
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    scheduler.shutdown()
