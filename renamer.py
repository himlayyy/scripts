import os
import re


def get_files(path):
    start = path
    file_list = []
    for path, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(".mp4"):
                print(file)
                # relative_path = os.path.join(path, file)
                # file_list.append(relative_path)

    print(f"Files {len(file_list)}")
    # renamer(file_list)

def renamer(files_list):
    count = 0
    # pattern = re.compile(r"pindl\\(.* Crystals)\\(.* TPU Case)\\(.* Series)")
    new_folder = r"C:\Users\Guest User\Desktop\ig2"
    str_list = ["Case","Holder","Mirror"]
    pattern = re.compile(r"pindl\\(.* Crystals)\\(.*" + "|".join(map(re.escape, str_list)) + ")")
    for file in files_list:
        matches = pattern.findall(file)
        if matches:
            print(matches)
            for item in matches:
                try:
                    new_name = os.path.join(new_folder," ".join(item))
                    os.rename(file, new_name + ".mp4")
                except FileExistsError:
                    pass
        count += 1
        print(f"{count} done")
get_files(r'C:\Users\Guest User\Desktop\IG Videos')