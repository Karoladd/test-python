import os

# folder path
dir_path = r'C:\Users\Karol\Desktop\python\image-text\image'
# list to store files
res = []
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)