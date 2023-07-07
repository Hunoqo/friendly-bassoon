import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import shutil

def move_modified_files(source_folder, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)  # 创建目标文件夹（如果不存在）
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.CR2'):
                cr2_file_path = os.path.join(root, file)
                jpg_file_name = file.replace('.CR2', '-1.jpg')
                jpg_file_path = os.path.join(root, jpg_file_name)
                xmp_file_name = file.replace('.CR2', '.xmp')
                xmp_file_path = os.path.join(root, xmp_file_name)
                if os.path.exists(jpg_file_path) and os.path.exists(xmp_file_path):
                    shutil.copy2(cr2_file_path, dest_folder)
                    shutil.copy2(jpg_file_path, dest_folder)
                    shutil.copy2(xmp_file_path, dest_folder)
                    print(f'Copied: {file}')

# 使用对话框选择源文件夹路径
Tk().withdraw()
source_folder = askdirectory(title='选择包含相片的文件夹')

# 使用对话框选择目标文件夹路径
Tk().withdraw()
dest_folder = askdirectory(title='选择保存文件的新文件夹')

# 调用函数进行文件复制
move_modified_files(source_folder, dest_folder)
