import numpy as np

source_address = "/home/jacktongmt/pain-disparities-cbm/processed_data_00m/train/show_both_knees_True_downsample_factor_None_normalization_method_our_statistics/image_890.npz"

# Load the .npz file
data = np.load(source_address)

# Get the keys (variable names) in the .npz file
keys = data.files

# Print the dimensions of each array in the .npz file
for key in keys:
    array = data[key]
    dimensions = array.shape
    print("Dimensions of array '{}': {}".format(key, dimensions))