__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#1. write a function clean_cache: clean_cache: takes no arguments and creates an 
# empty folder named cache in the current directory. 
# If it already exists, it deletes everything in the cache folder.
import os
import shutil 

def clean_cache(): 
    new_path = os.path.join(os.getcwd(), "files", "cache")
    if os.path.exists(new_path): 
        shutil.rmtree(new_path) 
        os.mkdir(new_path) 
    else:
        os.mkdir(new_path)
    
#2.cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, 
# in that order. The function then unpacks the indicated zip file 
# into a clean cache folder.
import zipfile

def cache_zip(zip_file_path, cache_dir_path):   
    with zipfile.ZipFile(zip_file_path, 'r') as file:
        file.extractall(cache_dir_path) 

#3.cached_files: takes no arguments and returns a list of all the files in the 
# cache. The file paths should be specified in absolute terms. Search the web 
# for what this means! No folders should be included in the list. 
# You do not have to account for files within folders within the cache directory.
# Python program to explain os.listdir() method

def cached_files():
    cache = os.path.join(os.getcwd(), "files", "cache")
    file_paths = []
    for file in os.listdir(cache):
        file_path = os.path.join(cache,file)
        if os.path.isfile(file_path):
            file_paths.append(os.path.abspath(file_path))
    return file_paths

#4.find_password: takes the list of file paths from cached_files as an argument. 
# This function should read the text in each one to see if the password is in 
# there. Surely there should be a word in there to indicate the presence of the 
# password? Once found, find_password should return this password string.

files = cached_files()
def find_password(files):
    word = 'password'
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if word in line:
                    return line.strip().split(' ')[1]
    
print(find_password(files))