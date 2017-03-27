import os

def get_files(directory):
  return [f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]

def remove_file(f):
  os.remove(f)
