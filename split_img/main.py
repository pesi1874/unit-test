import sys
import os
import shutil

raw_path = '/data/grade2/wallpaper/imgs_3_31544'
target_path = '/data/grade2/wallpaper'


files_raw = os.listdir(raw_path)
files_split = []
for i in files_raw:
    file = (i, int(i.split('.')[0].split('_')[1].split('x')[0]),
            int(i.split('.')[0].split('_')[1].split('x')[1]))
    files_split.append(file)


# ('p48205_1600x1200.jpg', '1600', '1200')


def get_2000():
    path = os.path.join(target_path, 'imgs_3_2000')

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.makedirs(path)

    files = [i for i in files_split if int(i[1]) >= 2560]
    print('2000: ', files.__len__())
    for i in files:
        old_path = os.path.join(raw_path, i[0])
        new_path = os.path.join(path, i[0])
        shutil.copyfile(old_path, new_path)


<<<<<<< HEAD
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
=======
def get_16_9():
    path = os.path.join(target_path, 'imgs_3_16_9')
>>>>>>> b962755c5bca307ce6123bc1622c513d944db864

    if os.path.exists(path):
        shutil.rmtree(path)
    else:
<<<<<<< HEAD
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
=======
        os.makedirs(path)
    files = [i for i in files_split if int(i[1]) >= 2560 and int(i[1]) >= 1.77 and int(i[1]) / int(i[2]) <= 2]
    print('16:9 : ', files.__len__())
>>>>>>> b962755c5bca307ce6123bc1622c513d944db864
    for i in files:
        old_path = os.path.join(raw_path, i[0])
        new_path = os.path.join(path, i[0])
        shutil.copyfile(old_path, new_path)

<<<<<<< HEAD
# get_4_3()
get_6_3()
# get_8_3()
=======

get_16_9()
# get_2000()
>>>>>>> b962755c5bca307ce6123bc1622c513d944db864
