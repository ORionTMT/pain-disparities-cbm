import pickle

# Open the pickle file in binary read mode
with open('/home/jacktongmt/pain-disparities-cbm/processed_data_00m/test/show_both_knees_True_downsample_factor_None_normalization_method_our_statistics/image_codes.pkl', 'rb') as file:
    try:
        data = pickle.load(file)
        
        print(len(data))  # Print the length of the list
        print(data[0]) 
    except Exception as e:
        print(f"Error occurred while loading pickle file: {str(e)}")