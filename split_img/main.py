import sys
import os
import shutil

raw_path = '/data/grade2/wallpaper/imgs_3_31544'

files_raw = os.listdir(raw_path)
files_split = []
for i in files_raw:
    file = (i, int(i.split('.')[0].split('_')[1].split('x')[0]),
            int(i.split('.')[0].split('_')[1].split('x')[1]))
    files_split.append(file)


# ('p48205_1600x1200.jpg', '1600', '1200')


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


def get_4_3():
    path = os.path.join('/data/grade2/wallpaper', 'imgs_3_4_3')

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)
    files = [i for i in files_split if (i[2] >= 1440 and i[1] >= 2560 and 1.33 <= i[1] / i[2] < 2)]
    print('4:3 : ', files.__len__())
    copy_file(files, path)


def get_6_3():
    path = os.path.join('/data/grade2/wallpaper', 'imgs_3_6_3')

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)
    files = [i for i in files_split if (i[2] >= 1440 and i[1] >= 2560 and 2 <= i[1] / i[2] < 2.66)]
    print('6:3 : ', files.__len__())
    copy_file(files, path)


def get_8_3():
    path = os.path.join('/data/grade2/wallpaper', 'imgs_3_8_3')

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)
    files = [i for i in files_split if (i[2] >= 1440 and i[1] >= 2560 and i[1] / i[2] >= 2.66)]
    print('8:3 : ', files.__len__())
    copy_file(files, path)


def copy_file(files, path):
    for i in files:
        old_path = os.path.join(raw_path, i[0])
        new_path = os.path.join(path, i[0])
        shutil.copyfile(old_path, new_path)

# get_4_3()
get_6_3()
# get_8_3()
