import os
import re

folders = os.listdir('./files')
phone_pattern = r'\d{3}-\d{3}-\d{4}'

# approach 01
for index, folder in enumerate(folders):
    files = os.listdir(f'./files/{folder}')
    for index, file in enumerate(files): 
        f = open(f'./files/{folder}/{file}', 'r')
        content = f.read()
        match = re.findall(phone_pattern, content)
        if match:
            print(f'A phone number {match} was found at ./files/{folder}/{file}')

# approach 02
result = []

for folders, subfolders, files in os.walk(os.getcwd()+'/files'):
    for file in files:
        f = open(folders+'/'+file, 'r')
        content = f.read()
        match = re.findall(phone_pattern, content)
        if match: 
            result.append(match)

print(result)
