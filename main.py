from data_preprossessing import check_missing_values_in_csv


data_folder = "./Data"
dataframes = check_missing_values_in_csv(data_folder)
print("\nDataFrames stored for each file:")
for file, df in dataframes.items():
    print(f"- {file}: {df.shape[0]} rows, {df.shape[1]} columns")