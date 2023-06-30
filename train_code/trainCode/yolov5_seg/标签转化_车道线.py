"""
说明：(json_label_2_txt) YX分割的json类型数据集的转换
只转换车道线数据 实线和虚线
"""
import json
import glob
import numpy as np
import cv2
import os


# categories_list : json标签文件中的标签类别
categories_list =["Drivable_road", "roadway", "solid_lane", "double_lane","dashed_lane", "crosswalk"]
# 原始json标签文件中的标签类别ID是从1开始的 YOLOV5-seg的txt文件中的类别ID从0开始
categories2id_dic = {'Drivable_road': 0, 'roadway': 1, "solid_lane": 2, "double_lane": 3,"dashed_lane": 4, "crosswalk":5}


# 当前路径
current_path = os.getcwd()

def convert_json_label_to_yolov_seg_label():
    # 存放原始json的文件夹的绝对路径
    json_path = current_path + "/lane_data_ylg/labels/segs"
    # 存放转换后的txt的文件夹绝对路径
    txt_outer_path = current_path + "/lane_data_ylg/labels/txt_only_lane/"

    # 获取原始json文件路径列表
    json_files_list = glob.glob(json_path + "/*.json")
    # print("json_files:", json_files_list,"\n",  type(json_files_list) )
    print("共有{}个json标签文件待转化".format(len(json_files_list)))

    # 遍历处理每个json文件
    flagcount = 0
    for json_file in json_files_list:
        # print("json_file: ",json_file)
        f = open(json_file)
        json_info = json.load(f)
        # print("json_info.keys(): ",json_info.keys())


        # 获取对应图像的高和宽
        image_key = json_info['images']
        # print(image_key, type(image_key))
        img_height = image_key[0]['height']
        img_width = image_key[0]['width']
        # print(img_height, img_width)
        np_w_h = np.array([[img_width, img_height]], np.int32)

        # 获取json文件名称
        json_name = json_file.split("/")[-1]
        # print(json_name)
        # 保存的txt文件
        txt_file =  txt_outer_path + json_name.replace(".json", ".txt")


        # 创建保存的txt文件
        f = open(txt_file, "a")
        # 遍历标注点信息
        for point_json in json_info['annotations']:
            # print("point_json: ",point_json)
            # 得到json中你标记的类名id
            label_name = point_json["category_id"]
            if label_name in [3,5]:
                categoriesid = str(categories2id_dic[categories_list[label_name-1]])
                # print("label_name: ", label_name,type(label_name), categories_list[label_name-1], categoriesid)
                # break
                # 提取分割标注点坐标信息
                txt_content = ""
                np_points = np.array(point_json["segmentation"], np.int32)[0]
                # print("np_points: ", np_points, type(np_points))
                # 坐标归一化处理
                norm_points = np_points / np_w_h
                # print("norm_points: ", norm_points)
                norm_points_list = norm_points.tolist()
                # print("norm_points_list: ", norm_points_list)
                txt_content += categoriesid + " " + " ".join([" ".join([str(cell[0]), str(cell[1])]) for cell in norm_points_list]) + "\n"
                # print("txt_content: ", txt_content)
                f.write(txt_content)
        flagcount += 1
        # break

    if flagcount== len(json_files_list):
        print('成功转化{}个json标签文件'.format(flagcount))
    else:
        print("还剩下{}个文件未转化".format(len(json_files_list) - flagcount))



convert_json_label_to_yolov_seg_label()