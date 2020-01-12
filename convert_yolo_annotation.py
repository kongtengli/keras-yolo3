import xml.etree.ElementTree as ET
from os import getcwd
from PIL import Image

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

new_class  = "snowman"
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor","cai","snowman"]


def convert_annotation(year, image_id, list_file,img_path):
    in_file = open('VOCdevkit/VOC%s/Annotations/txt_wang/%s.txt'%(year, image_id))
    img = Image.open(img_path)
    img_w = img.width
    img_h = img.height

    #print("img_w：{}，img_h:{}".format(img_w,img_h))
    
    lines = in_file.readlines()
    for line in lines:
        line_list = line.split()          
        cls_id = classes.index(new_class)
        c_x = int(float(line_list[1])*img_w)
        c_y = int(float(line_list[2])*img_h)
        b_w = int(float(line_list[3])*img_w)
        b_h = int(float(line_list[4])*img_h)

        x_min = int(c_x - b_w/2)
        y_min = int(c_y - b_h/2)
        x_max = int(c_x + b_w/2)
        y_max = int(c_y + b_h/2)
        b = (x_min, y_min, x_max, y_max)
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s_wang.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s_wang.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        img_path = './VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(year, image_id)
        list_file.write(img_path)
        convert_annotation(year, image_id, list_file, img_path)
        list_file.write('\n')
    list_file.close()

