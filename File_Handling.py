import os
from shutil import copyfile
statement = 'Hi, I am a Text file'
path = 'C:\\Users\\bilal\\OneDrive\\Desktop\\test.txt'
with open(path,'w') as file: file.write(statement)  #Write File
with open(path,'a') as file: file.write('\nThis is a new line')  #Append File
with open(path) as file: copy = file.read()  #Read File
print(copy)
if os.path.isfile('test.txt'): print('File already exists in Location')
else: os.replace(path,'test.txt')  #Move file to another Location
if os.path.isfile('c:\\Users\\bilal\\Downloads\\test_copy.txt'): print('File already exists in Location')
else: copyfile('test.txt','c:\\Users\\bilal\\Downloads\\test_copy.txt')  #Copy File to another Location
if os.path.isfile('test.txt'): os.remove('test.txt')  #Delete File
else: print('File Not Found')