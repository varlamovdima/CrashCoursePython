from sys import argv
from os.path import exists
program_name, path_to_file = argv
print(exists(path_to_file))
