import sys
import os

docstring = '''
Name: 64bit to 32bit a3x converter
Description: Old a3x decompilation tools do not support 64 bit versions. This script converts to 32 bit to allow old tools to work
'''

help_message = f'''
Usage: {sys.argv[0]} <AutoItSC.bin path> <a3x file to convert>
You can download the ZIP with AutoItSC.bin in it from here. https://www.autoitscript.com/autoit3/files/archive/autoit
You will find it in the path Aut2Exe\\AutoItSC.bin'''

if len(sys.argv) > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(f"{docstring}{help_message}")
        sys.exit(0)
else:
    print("Please provide a filename")
    sys.exit(1)

autoitsc = sys.argv[1]
filename = sys.argv[2]
with open(autoitsc, "rb") as f:
    data_a = f.read()

with open(filename, "rb") as f:
    data_d = f.read()

# Finding the pattern
pattern = b'\xA3\x48\x4B\xBE\x98\x6C\x4A\xA9\x99\x4C\x53\x0A\x86\xD6\x48\x7D'
index = data_d.find(pattern)

if index != -1:
    print(f"- Creating 32-bit version '{filename}.a32.exe'")
    with open(f"{filename}.a32.exe", "wb") as f:
        f.write(data_a + data_d[index:])
else:
    print("Script not found")
