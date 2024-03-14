import os

def get_folder_size(folder_path):
    folder_list = next(os.walk(folder_path))[1]
    for folder in folder_list:
        folder_size = sum(os.path.getsize(os.path.join(folder_path, folder, name)) for name in os.listdir(os.path.join(folder_path, folder)))
        folder_size_gb = folder_size / (1024 * 1024 * 1024)  # 바이트를 GB로 변환
        print(f"Folder: {folder}, Total Size: {folder_size_gb:.2f} GB")

folder_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark'
get_folder_size(folder_path)
