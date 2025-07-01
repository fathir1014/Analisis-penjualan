import os

def pastikan_folder_output(path):
    if not os.path.exists(path):
        os.makedirs(path)
