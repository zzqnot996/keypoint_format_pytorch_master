
## json2point.py

'''

img_path : 为所标注的point信息形成的json文件路径 （文件夹）

out_path  : 输出文件夹

'''

作用： 每个json文件对应一个txt文件 是同名的 

用于将json文件生成对应的x y 的txt 形式

txt格式： x y  只能对应一种物体

同时会输出有多少个物体

## remove_paired_json_jpg.py

'''
将图片与对应的json文件移动到相应的文件夹
'''

def find_and_move_files(scr_directory, target_directory):
    
    '''
    scr_directory : 源文件夹 里面含有图片 与 图片对应的json文件

    target_directory ： 目标文件夹 含有图片 与 图片对应的json文件
    '''
