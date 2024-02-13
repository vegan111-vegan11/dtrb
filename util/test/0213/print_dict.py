import os

folder_path = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts'

file_names = os.listdir(folder_path)

for file_name in file_names:
    print(file_name)
