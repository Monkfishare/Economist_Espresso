import os
from datetime import datetime, timedelta

def get_latest_date_folder(directory):
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    if not folders:
        return None
    folders.sort(reverse=True)
    latest_date_folder = folders[0]
    return latest_date_folder

def remove_old_folders(directory, latest_date_folder):
    latest_date = datetime.strptime(latest_date_folder, '%Y-%m-%d')
    threshold_date = latest_date - timedelta(days=15)
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            folder_date = datetime.strptime(folder, '%Y-%m-%d')
            if folder_date < threshold_date:
                print(f"Removing old folder: {folder}")
                os.system(f"rm -r {folder_path}")

if __name__ == "__main__":
    WB_dir = "WB"
    latest_date_folder = get_latest_date_folder(WB_dir)
    if latest_date_folder:
        print(f"Latest date folder: {latest_date_folder}")
        remove_old_folders(WB_dir, latest_date_folder)
    else:
        print("No folders found in WB directory.")
