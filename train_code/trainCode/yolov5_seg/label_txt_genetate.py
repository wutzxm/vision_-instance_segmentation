
import json
import os
import cv2

YX_CATEGORIES_0 = [
    {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "person"},
    {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "bicyclist"},
    {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "bicycle"},
    {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "motorcyclist"},
    {"color": [106, 0, 228], "isthing": 1, "id": 5, "name": "motorcycle"},
    {"color": [0, 60, 100], "isthing": 1, "id": 6, "name": "inWheelchair"},
    {"color": [0, 80, 100], "isthing": 1, "id": 7, "name": "wheelchair"},
    {"color": [0, 0, 70], "isthing": 1, "id": 8, "name": "tricycllist"},
    {"color": [0, 0, 192], "isthing": 1, "id": 9, "name": "tricycle"},
    {"color": [250, 170, 30], "isthing": 1, "id": 10, "name": "car"},
    {"color": [100, 170, 30], "isthing": 1, "id": 11, "name": "SUV"},
    {"color": [250, 141, 255], "isthing": 0, "id": 12, "name": "van"},
    {"color": [220, 220, 0], "isthing": 1, "id": 13, "name": "MPV"},
    {"color": [175, 116, 175], "isthing": 1, "id": 14, "name": "policeCar"},
    {"color": [250, 0, 30], "isthing": 1, "id": 15, "name": "truck"},
    {"color": [165, 42, 42], "isthing": 1, "id": 16, "name": "lorry"},
    {"color": [255, 77, 255], "isthing": 1, "id": 17, "name": "bus"},
    {"color": [0, 226, 252], "isthing": 1, "id": 18, "name": "schoolBus"},
    {"color": [182, 182, 255], "isthing": 1, "id": 19, "name": "saniSweeper"},
    {"color": [0, 82, 0], "isthing": 1, "id": 20, "name": "sprinkler"},
    {"color": [120, 166, 157], "isthing": 1, "id": 21, "name": "cementTruck"},
    {"color": [110, 76, 0], "isthing": 1, "id": 22, "name": "fireTruck"},
    {"color": [174, 57, 255], "isthing": 1, "id": 23, "name": "ambulance"},
    {"color": [199, 100, 0], "isthing": 1, "id": 24, "name": "roadRescuer"},
    {"color": [72, 0, 118], "isthing": 1,
        "id": 25, "name": "constructVehicle"},
    {"color": [102, 102, 156], "isthing": 0, "id": 26, "name": "forkLift"},
    {"color": [255, 179, 240], "isthing": 1,
        "id": 27, "name": "containerCrane"},
    {"color": [0, 125, 92], "isthing": 1, "id": 28, "name": "rubberTyreCrane"},
    {"color": [209, 0, 151], "isthing": 1, "id": 29, "name": "shelfCar"},
    {"color": [188, 208, 182], "isthing": 1, "id": 30, "name": "trolley"},
    {"color": [0, 220, 176], "isthing": 1, "id": 31, "name": "otherehicle"},
    {"color": [255, 99, 164], "isthing": 1, "id": 32, "name": "stonePier"},
    {"color": [92, 0, 73], "isthing": 1, "id": 33, "name": "curbStone"},
    {"color": [133, 129, 255], "isthing": 1, "id": 34, "name": "waterHorse"},
    {"color": [78, 180, 255], "isthing": 1, "id": 35, "name": "warningSign"},
    {"color": [0, 228, 0], "isthing": 1, "id": 36, "name": "trafficCone"},
    {"color": [174, 255, 243], "isthing": 1, "id": 37, "name": "crashpost"},
    {"color": [45, 89, 255], "isthing": 1, "id": 38, "name": "paperBox"},
    {"color": [134, 134, 103], "isthing": 1,
        "id": 39, "name": "plasticBottle"},
    {"color": [145, 148, 174], "isthing": 1, "id": 40, "name": "luggage"},
    {"color": [255, 208, 186], "isthing": 1,
        "id": 41, "name": "containerTwistLockBox"},
    {"color": [197, 226, 255], "isthing": 1, "id": 42, "name": "stone"},
    {"color": [171, 134, 1], "isthing": 1, "id": 43, "name": "cat"},
    {"color": [109, 63, 54], "isthing": 1, "id": 44, "name": "bird"},
    {"color": [207, 138, 255], "isthing": 1,
        "id": 45, "name": "floatePlastic"},
    {"color": [151, 0, 95], "isthing": 1, "id": 46, "name": "floateLeaf"},
    {"color": [9, 80, 61], "isthing": 1, "id": 47, "name": "trafficLight"},
    {"color": [84, 105, 51], "isthing": 1, "id": 48, "name": "trafficPanel"},
    {"color": [74, 65, 105], "isthing": 1, "id": 49, "name": "manholecover"},
    {"color": [166, 196, 102], "isthing": 1, "id": 50, "name": "speedbump"},
    {"color": [208, 195, 210], "isthing": 1, "id": 51, "name": "other"},
]

YX_CATEGORIES_0_map = [
    {"name": "person", 'id': 0, 'id_map': [1]},
    {"name": "cycle", 'id': 1, 'id_map': [2, 5]},
    {"name": "tricycle", 'id': 2,  'id_map': [8, 9]},
    {"name": "vehicle", 'id': 3,  'id_map': [10, 31]},
    {"name": "trafficLight", 'id': 4, 'id_map': [47, 48]},
    {"name": "manholecover", 'id': 5, 'id_map': [49]},
    {"name": "speedbump", 'id': 6, 'id_map': [50]},
]


thing_ids = [k["id"] for k in YX_CATEGORIES_0_map]
print("thing_ids:  ", thing_ids)
thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
 
def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = box[0] + box[2] / 2.0 
    y = box[1] + box[3] / 2.0 
    w = box[2]
    h = box[3]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
 
def decode_json(json_floder_path,txt_outer_path, json_name, image_path):
    visua_path = "/home/zxm/yangluogang/visual/"
    visua_path = os.path.join(visua_path, json_name[:-9] + '.jpg')

    print("visua_path: ", visua_path)
 
    txt_name = txt_outer_path + json_name[:-9] + '.txt'

    print("txt_name: ", txt_name)
    iamge_full_path = os.path.join(image_path, json_name[:-9] + '.jpg')
    image = cv2.imread(iamge_full_path)
    id_dict_map = {}
    for num in range(1, 52):
        for k in YX_CATEGORIES_0_map:
            if k["id_map"][0] <= num <= k["id_map"][-1]:
                id_dict_map[num] = k["id"]
                
    with open(txt_name,'w') as f:
        json_path = os.path.join(json_floder_path, json_name)
        data = json.load(open(json_path, 'r', encoding='gb2312',errors='ignore'))
        img_w = data['images'][0]["width"]
        img_h = data['images'][0]["height"]
      
        for i in data['annotations']:
            category_id = i['category_id']
            if category_id in id_dict_map.keys():
        
                x1 = float(i['bbox'][0])
                y1 = float(i['bbox'][1])
                w = float(i['bbox'][2])
                h = float(i['bbox'][3])
                box = (x1, y1, w, h)
            
                cv2.rectangle(image, (int(box[0]),int(box[1])), (int(box[2]+x1),int(box[3]+y1)), (255, 0, 255), 2)
                cv2.putText(image, str(id_dict_map[category_id]), (int(box[0]),int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 1)
                bbox = convert((img_w, img_h), box)
                try:
                    f.write(str(id_dict_map[i['category_id']]) + " " + " ".join([str(a) for a in bbox]) + '\n')
                except:
                    pass
    cv2.imwrite(visua_path, image)
 
if __name__ == "__main__":
    json_floder_path = '/home/zxm/yangluogang/json/'#
    image_path = "/home/zxm/yangluogang/images/"
    txt_outer_path = "/home/zxm/yangluogang/txt/"

    json_names = os.listdir(json_floder_path)
    print("json_names: ", json_names)
    print("共有：{}个文件待转化".format(len(json_names)))
    flagcount=0
    for json_name in json_names:
        decode_json(json_floder_path,txt_outer_path,json_name, image_path)
        flagcount+=1
        print("还剩下{}个文件未转化".format(len(json_names)-flagcount))

    print('转化全部完毕')


# if __name__ == "__main__":
#
#     image_path = "/home/zxm/yangluogang/images/"
#     train_path = "/data/xuyun/training_data/train/"
#     test_path = "/data/xuyun/training_data/test/"
#
#     json_names = os.listdir(json_floder_path)
#     print("共有：{}个文件待转化".format(len(json_names)))
#     flagcount=0
#     for json_name in json_names:
#         decode_json(json_floder_path,txt_outer_path,json_name, image_path)
#         flagcount+=1
#         print("还剩下{}个文件未转化".format(len(json_names)-flagcount))
#
#        # break
#     print('转化全部完毕')

