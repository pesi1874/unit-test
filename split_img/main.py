import sys
import os
import shutil

raw_path = '/data/grade2/wallpaper/imgs_3_31544'

files_raw = os.listdir(raw_path)
files_split = []
for i in files_raw:
    file = (i, i.split('.')[0].split('_')[1].split('x')[0], i.split('.')[0].split('_')[1].split('x')[1])
    files_split.append(file)


def get_2000():
    path = os.path.join('/data/grade2/wallpaper', 'imgs_3_2000')

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)

    files = [i for i in files_split if int(i[1]) >= 2560]
    print('2000: ', files.__len__())
    for i in files:
        old_path = os.path.join(raw_path, i[0])
        new_path = os.path.join(path, i[0])
        shutil.copyfile(old_path, new_path)


def get_16_9():
    path = os.path.join('/data/grade2/wallpaper', 'imgs_3_16_9')

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)
    files = [i for i in files_split if int(i)>= 2560 and [1] >= 1.77 <= int(i[1]) / int(i[2]) <= 2]
    print('16:9 : ', files.__len__())
    for i in files:
        old_path = os.path.join(raw_path, i[0])
        new_path = os.path.join(path, i[0])
        shutil.copyfile(old_path, new_path)

# get_16_9()
get_2000()