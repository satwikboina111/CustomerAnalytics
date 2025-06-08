import os
import pandas as pd
import json

def save_dataframe_to_csv(df, file_name, folder="output"):
    """
    Saves a DataFrame to a CSV file in the specified folder.

    Parameters:
    - df (pd.DataFrame): The DataFrame to save.
    - file_name (str): The name of the file (with .csv extension).
    - folder (str): The folder where the file will be saved. Defaults to 'output'.

    If the folder doesn't exist, it will be created. If the file already exists, it will be overwritten.
    """
    # Ensure the folder exists
    file_name = file_name if file_name.endswith('.csv') else f"{file_name}.csv"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Construct the full file path
    file_path = os.path.join(folder, file_name)
    
    # Save the DataFrame to CSV
    df.to_csv(file_path, index=False)
    print(f"DataFrame saved to {file_path}")

def save_dict_to_excel(data_dict, file_name, folder="output"):
    """
    Saves a dictionary of DataFrames to an Excel file in the specified folder.

    Parameters:
    - data_dict (dict): A dictionary where keys are sheet names and values are DataFrames.
    - file_name (str): The name of the Excel file (with .xlsx extension).
    - folder (str): The folder where the file will be saved. Defaults to 'output'.

    If the folder doesn't exist, it will be created. If the file already exists, it will be overwritten.
    """
    # Ensure the folder exists
    file_name = file_name if file_name.endswith('.xlsx') else f"{file_name}.xlsx"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Construct the full file path
    file_path = os.path.join(folder, file_name)
    
    # Save the dictionary of DataFrames to Excel
    with pd.ExcelWriter(file_path) as writer:
        for sheet_name, df in data_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"Excel file saved to {file_path}")

def read_config(config_file_name="config.yaml", base_folder="CustomerAnalytics", config_folder="Config"):
    """
    Reads a configuration file from the Config folder within the CustomerAnalytics folder.

    Parameters:
    - config_file_name (str): The name of the configuration file (e.g., 'config.json').
    - base_folder (str): The base folder where the CustomerAnalytics folder is located. Defaults to 'CustomerAnalytics'.
    - config_folder (str): The name of the folder containing configuration files. Defaults to 'Config'.

    Returns:
    - dict: The contents of the configuration file as a dictionary.

    Raises:
    - FileNotFoundError: If the configuration file does not exist.
    """
    # Construct the full path to the configuration file
    config_path = os.path.join(base_folder, config_folder, config_file_name)
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    # Read and return the configuration file contents
    with open(config_path, 'r') as file:
        config_data = json.load(file)
    
    return config_data