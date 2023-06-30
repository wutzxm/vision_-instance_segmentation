import cv2
import matplotlib.pyplot as plt
import os 
import sys
import numpy as np
import json
import shutil
os.chdir(sys.path[0])
# 将标准的数据分成训练集,验证集和测试集

def mycopyfile(srcfile,dstpath):
    """ 复制函数
    
    """                       
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath +"/"+ fname)          # 复制文件
        print ("copy %s -> %s"%(srcfile, dstpath + "/"+fname))


def cut_dataset(type_,idx,dataset_images_path):
    """根据图片截取数据集
    Args:
        type_: 数据值类型
        idx (list): 索引区间  例如[0,1000]表示0~1000帧
        dataset_root_path (str): 图片存储的根目录name
        
    """
    new_path=dataset_images_path + "/" +type_
    origin_path=dataset_images_path + "/origin/" 
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    for file in os.listdir(origin_path):
        name = file.split(".")[0]
        if float(name) >=idx[0] and  float(name) < idx[1] :
            mycopyfile(origin_path+"/"+file,new_path)


if __name__=="__main__":
    
    # >>>>>>>>>cut images dir
    dataset_root_path="../../datasets/xwyd_10x10_road/images/"
    cut_dataset("train",[0,2700],dataset_root_path)
    cut_dataset("test",[2700,2835+1],dataset_root_path)
    cut_dataset("val",[2700,2835+1],dataset_root_path)

    # >>>>>>>>>cut label dir 
    dataset_root_path="../../datasets/xwyd_10x10_road/label_txt/"
    cut_dataset("train",[0,2700],dataset_root_path)
    cut_dataset("test",[2700,2835+1],dataset_root_path)
    cut_dataset("val",[2700,2835+1],dataset_root_path)
