import os

counter = 0
fileList = []
# traverse root directory, and list directories as dirs and files as files


for root, dirs, files in os.walk("."):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']

    path = root.split(os.sep)

    for file in files:
        fullPath = root + '/' + file
        if os.path.getsize(fullPath) != 0:
            if " " in file:
                os.remove(fullPath)
                print(file)
            counter = counter + 1
            fileList.append(fullPath)

fileList.sort()
# for file in fileList:
#     print(file)

# print(counter)
