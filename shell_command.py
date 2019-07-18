import os

print(os.getcwd())
print(type(os.system('cat {} | wc -l'.format('./util/file2list.py'))))
