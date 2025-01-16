from data_preprossessing import check_missing_values_in_csv


data_folder = "./Data"
dataframes = check_missing_values_in_csv(data_folder)
print("\nDataFrames stored for each file:")
