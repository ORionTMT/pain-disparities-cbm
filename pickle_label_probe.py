import os
import pickle

def explore_pickle_structure(directory):
    pickle_files = [file for file in os.listdir(directory) if file.endswith('.pkl')]
    
    for file in pickle_files:
        file_path = os.path.join(directory, file)
        
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            
            print(f"Pickle file: {file}")
            print("Keys in the dictionary:")
            for key in data.keys():
                print(f"- {key}")
            
            print("Exploring 'images' key (if exists):")
            if 'images' in data:
                for i, image_data in enumerate(data['images']):
                    print(f"Image {i} keys:")
                    for key in image_data.keys():
                        print(f"  - {key}")
                        if isinstance(image_data[key], dict):
                            print(f"    Subkeys in '{key}':")
                            for subkey in image_data[key].keys():
                                print(f"      - {subkey}")
                    if i >= 4:  # 只探索前5个图像的结构
                        break
            else:
                print("'images' key not found in the dictionary.")
            
            print("---")

# 指定包含pickle文件的目录路径
directory_path = '/home/jacktongmt/NDA/nda-tools/downloadcmd/packages/1225783/processed_image_data'

# 调用函数探索pickle文件的结构
explore_pickle_structure(directory_path)