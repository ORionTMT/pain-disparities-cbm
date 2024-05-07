import numpy as np

source_address = "/home/jacktongmt/pain-disparities-cbm/processed_data_1224/test/show_both_knees_True_downsample_factor_None_normalization_method_our_statistics/image_783.npy"

# Load the .npy file
data = np.load(source_address)

# Get the dimensions of the loaded data
dimensions = data.shape

# Print the dimensions
print("Dimensions of the .npy file:", dimensions)