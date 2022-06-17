import os
import re

pattern = re.compile(r'^C:.+\\Rangsee\\(.+)')

location = r"C:\Users\Guest User\Desktop\rangsee"
print("****Start******")
vid_count = 0
import re
pattern = r"^rangsee vids(.+)"
path = r"C:\Users\Guest User\Desktop\rangsee vids"
for root_dir_path,sub_dirs,files in os.walk(path):
    for file in files:
        print(file)
        clean = re.match(pattern, file)

        new_filename = path + "\\" + clean[1]
        old = path + "\\" + file
        os.rename(old, new_filename)
for root_dir_path,sub_dirs,files in os.walk(path):
    print(files)

print(vid_count)


