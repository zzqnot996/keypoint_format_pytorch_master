# keypoint_format_pytorch_master
这是关于关键点转换格式的文件

## tools 

关于格式转换

### json2point.py

作用： 每个json文件对应一个txt文件 是同名的 

用于将json文件生成对应的x y 的txt 形式
txt格式： x y  只能对应一种物体
同时会输出有多少个物体

**def jsonTopoint(img_path,out_path):**

'''
img_path : 为所标注的point信息形成的json文件路径 （文件夹）

out_path  : 输出文件夹
'''







