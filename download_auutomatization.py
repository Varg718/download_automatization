import os
import shutil

default_download_folder = r'/home/robertw/Downloads/'

rar_files = r"/home/robertw/Videos/"
ebook_files = r"/home/robertw/Documents/"

try:
    for plik in os.listdir(default_download_folder):
        if plik.endswith((".rar", '.zip', '.7z')):
            source_path = os.path.join(default_download_folder, plik)
            destination_path = os.path.join(rar_files, plik)
            shutil.move(source_path, destination_path)
    
    for ebook in os.listdir(default_download_folder):
        if ebook.endswith(('.epub', '.mobi', '.pdf')):
            source_path = os.path.join(default_download_folder, ebook)
            destination_path = os.path.join(ebook_files, ebook)
            shutil.move(source_path, destination_path)
    
except Exception as error:
    print(f"There is an error: {error}")
