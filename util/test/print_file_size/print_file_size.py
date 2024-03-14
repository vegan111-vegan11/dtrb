import os

def get_folder_sizes(folder_path):
    for root, dirs, files in os.walk(folder_path):
        total_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        total_size += sum(os.path.getsize(os.path.join(root, name)) for name in dirs)
        print(f"Folder: {root}, Total Size: {total_size} bytes")

folder_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark'
get_folder_sizes(folder_path)
