import os
import pickle

def check_pickle_files(directory):
    pickle_files = [file for file in os.listdir(directory) if file.endswith('.pkl')]
    
    for file in pickle_files:
        file_path = os.path.join(directory, file)
        
        with open(file_path, 'rb') as f:
            try:
                data = pickle.load(f)
                if 'images' in data:
                    num_images = len(data['images'])
                    print("Pickle file {} contains {} images.".format(file, num_images))
                else:
                    print("Pickle file {} does not contain 'images' key.".format(file))
            except EOFError:
                print("Pickle file {} is empty or corrupted.".format(file))

# 指定包含pickle文件的目录路径
directory_path = '/home/jacktongmt/NDA/nda-tools/downloadcmd/packages/1225783/processed_image_data'

# 调用函数检查pickle文件
check_pickle_files(directory_path)