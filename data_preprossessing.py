import os
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler

def check_missing_values_in_csv(data_folder):
    """
    Iterates through all CSV files in the specified folder and checks for missing values in their columns.

    Args:
        data_folder (str): Path to the folder containing CSV files.

    Returns:
        dict: A dictionary where keys are file names and values are their respective DataFrames.
    """
    if not os.path.isdir(data_folder):
        print(f"The folder '{data_folder}' does not exist.")
        return {}

    files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

    if not files:
        print(f"No CSV files found in the folder '{data_folder}'.")
        return {}

    dataframes = {}

    for file in files:
        file_path = os.path.join(data_folder, file)
        print(f"\nProcessing file: {file}")

        try:
            df = pd.read_csv(file_path)
            missing_values = df.isnull().sum()

            if missing_values.any():
                # Apply KNN imputation to numeric columns
                numeric_columns = df.select_dtypes(include=['number']).columns
                if not numeric_columns.empty:
                    imputer = KNNImputer(n_neighbors=5)
                    df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
                    # print(f"Missing values in numeric columns of '{file}' filled using KNN imputation.")

                # Save the updated DataFrame back to the CSV file
                df.to_csv(file_path, index=False)
                print(f"Updated file saved: {file}")

            else:
                print("No missing values found in this file.")

            # Save the updated DataFrame back to the dictionary
            dataframes[file] = df

        except pd.errors.EmptyDataError:
            print(f"The file '{file}' is empty.")
        except Exception as e:
            print(f"Error processing file '{file}': {e}")

    dataframes = scaler(dataframes)

    return dataframes

def scaler(dataframes):
    scaler = MinMaxScaler()

    for file_name, df in dataframes.items():

        numeric_columns = df.select_dtypes(include=["number"]).columns
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
        dataframes[file_name]=df
    return dataframes