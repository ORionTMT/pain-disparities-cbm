import numpy as np

source_address = "/path/to/your/file.npz"

# Load the .npz file
data = np.load(source_address)

# Get the keys (variable names) in the .npz file
keys = data.files

# Print the dimensions of each array in the .npz file
for key in keys:
    array = data[key]
    dimensions = array.shape
    print(f"Dimensions of array '{key}': {dimensions}")