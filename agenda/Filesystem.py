import os

def get_files(directory):
  return [f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]

def remove_file(f):
  os.remove(f)

def add_line_to_file(file_name, line):
  with open(file_name, 'a+') as fp:
    fp.write('%s\n' % (line))
