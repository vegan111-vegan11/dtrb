import os

def get_folder_size(folder_path):
    folder_list = next(os.walk(folder_path))[1]
    for folder in folder_list:
        folder_size = sum(os.path.getsize(os.path.join(folder_path, folder, name)) for name in os.listdir(os.path.join(folder_path, folder)))
        print(f"Folder: {folder}, Total Size: {folder_size} bytes")

folder_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark'
get_folder_size(folder_path)

