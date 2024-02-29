import os
import shutil


'''
将图片与对应的json文件移动到相应的文件夹
'''

def find_and_move_files(scr_directory, target_directory):
    
    '''
    scr_directory : 源文件夹 里面含有图片 与 图片对应的json文件

    target_directory ： 目标文件夹 含有图片 与 图片对应的json文件
    '''

    count = 0

    # 遍历目标文件夹中的所有文件
    for filename in os.listdir(scr_directory):
        if filename.endswith('.json'):

            count = count + 1

            # 找到与json文件同名的jpg文件
            jgg_filename = filename[:-5] + '.jpg'
            jgg_filepath = os.path.join(scr_directory, jgg_filename)

            if os.path.exists(jgg_filepath):


                # 移动json文件和jpg文件到目标文件夹
                shutil.move(os.path.join(scr_directory, filename), os.path.join(target_directory, scr_directory + filename))
                shutil.move(jgg_filepath, os.path.join(target_directory, scr_directory + jgg_filename))

                print(f"Moved {filename} and {jgg_filename} to {target_directory}")
                print(f"total of {count} json file")

if __name__ == "__main__":
    #---------------------------------------------------------------------------------------------------------------------------------------
    # scr_directory=r"20231229_124445_1080p"  89
    # scr_directory=r"20231229_145126_1440p"  121
    # scr_directory=r"20231229_152008_1080p"  97
    #-------------------------------------------------------------------------------------------------------------------------------------------
    scr_directory=r"20231229_152008_1080p"
    target_directory = r'I:\flower_dataset'

    find_and_move_files(scr_directory,target_directory)
