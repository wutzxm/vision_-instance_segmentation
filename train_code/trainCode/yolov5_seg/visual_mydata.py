import numpy as np
import cv2
import os




# 当前路径
current_path = os.getcwd()
# 原始图片路径
pic_path = current_path + '/datasets/xm_ylg_data/images/train'
# 标签路径
txt_path = current_path + '/datasets/xm_ylg_data/labels/train'

label_path_list = [i.split('.')[0] for i in os.listdir(pic_path)]



for path in label_path_list:

    img = cv2.imread(f'{pic_path}/{path}.jpg')
    height, width, _ = img.shape




    # 勾勒多边形
    file_handle = open(f'{txt_path}/{path}.txt')




    cnt_info = file_handle.readlines()
    new_cnt_info = [line_str.replace("\n", "").split(" ") for line_str in cnt_info]



    # namelist = ["Drivable_road可行驶道路: 0蓝色", "roadway 道路 1黑色", "solid_lane实心车道:2红色", "double_lane"3 双车道 紫色, "dashed_lane虚线车道 4 白色", "crosswalk"5人行横道黄色]
    color_map = {"0": (255,0,0), "1": (0, 0, 0), "2": (0, 0, 255), "3": (255, 0, 255), "4": (255, 255, 255), "5":(0,255,255)}

    for new_info in new_cnt_info:
        s = []
        for i in range(1, len(new_info), 2):
            b = [float(tmp) for tmp in new_info[i:i + 2]]
            s.append([int(b[0] * width), int(b[1] * height)])
        cv2.polylines(img, [np.array(s, np.int32)], True, color_map.get(new_info[0]),2)


    scale_percent =80  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


    cv2.imshow('imgresize', resized )
    cv2.waitKey()



