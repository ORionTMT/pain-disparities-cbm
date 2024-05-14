import os
import numpy as np
import sys

def convert_npy_to_npz(directory, excluded_dir = None):
    for root, dirs, files in os.walk(directory):
        #if excluded_dir and excluded_dir in dirs:
            #dirs.remove(excluded_dir)  # Exclude the specified directory from traversal
        
        for filename in files:
            if filename.endswith(".npy"):
                file_path = os.path.join(root, filename)
                array = np.load(file_path)
                
                new_filename = os.path.splitext(filename)[0] + ".npz"
                new_file_path = os.path.join(root, new_filename)
                
                #os.remove(file_path)
                if not os.path.exists(new_file_path):
                    np.savez_compressed(new_file_path, array)
                
                os.remove(file_path)
                #print(f"Converted {file_path} to {new_file_path}")

# Specify the directory path and the name of the directory to exclude
#directory = input("parent directory to traverse: ")
#excluded_dir = "BLINDED_HOLD_OUT_DO_NOT_USE"


if __name__ == '__main__':
# Call the function to convert .npy files to .npz files
    convert_npy_to_npz(sys.argv[1])
