import json
import os
import scipy.io as scio
import numpy as np
import scipy.io as scio

import h5py
import scipy.io as io
import PIL.Image as Image
import numpy as np
import os
import glob
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import scipy.spatial
import scipy
import json
from matplotlib import cm as CM
import os
import torch

'''
img_path : 为所标注的point信息形成的json文件路径 （文件夹）
out_path  : 输出文件夹
作用： 每个json文件对应一个txt文件 是同名的 

用于将json文件生成对应的x y 的txt 形式
txt格式： x y  只能对应一种物体
同时会输出有多少个物体
'''


def jsonTopoint(img_path,out_path):

    image_path = []

    image_json  = os.listdir(img_path)  # 遍历每类文件夹中的图片json
    root_path =  img_path


    for i in range (0,len(image_json)):
        print(image_json[i])
        # 获取每个json文件的路径
        json_path = os.path.join(root_path,image_json[i])

        with open(json_path, 'r', encoding='UTF-8') as load_f:  # encoding='UTF-8'

            load_dict = json.load(load_f)  # 载入该文件

            # 获取图片中的有物体的坐标点
            object_info = load_dict['shapes']

            # object_info  是一个看列表类型
            # 获取列表的长度 即一共有多少oBject 一共有多少个有物体的点
            object_numeber = len(object_info)
            print(r'{}图片中有{}个物体'.format(image_json[i],object_numeber) )

            with open(os.path.join(out_path,'\{}.txt'.format(image_json[i]).split('\\')[-1].split('.')[0] + '.txt'),"w" )as f:
            # with open("{}.txt".format(image_json[i]).split('.')[0],"w") as f:
            
            # 获取每张图片中所有的point信息
                for point_idx in range (0,object_numeber):
                    point_item = object_info[point_idx]['points'][0]
                    # print(point_item)
                    f.write('{} {}'.format(point_item[0],point_item[1] ))
                    f.write('\n')

    print('done')


if __name__ == "__main__":

    img_path = r"I:\flower_dataset\json"
    out_path = r"I:\flower_dataset\txt"
    jsonTopoint(img_path,out_path)