# pathlib is a built in module that has classes defined for us to work with file systems
from pathlib import Path
p = Path()
# print(p.glob('*.xls'))
for file in p.glob('*'):
    print(file)
# Absolute path (start from root of hard disk)... c:\Program Files\Microsoft... /usr/local/bin
# relative path (starting from current directory)
