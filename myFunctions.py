import os

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        print('hello')
    return content

