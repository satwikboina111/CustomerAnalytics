import os
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.cluster.hierarchy import dendrogram, linkage

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

def read_config(config_file_name="config.yaml",config_folder="Config"):
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
    base_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),"..")  # Get the directory of the current file
    print(base_folder)
    config_path = os.path.join(base_folder, config_folder, config_file_name)
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    # Read and return the configuration file contents
    with open(config_path, 'r') as file:
        config_data = yaml.safe_load(file)
    
    return config_data


def plot_correlation_matrix(df,title = "Correlation Matrix", figsize=(10, 8)):
    """
    Plots a correlation matrix for the given DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame for which to plot the correlation matrix.
    - title (str): The title of the plot. Defaults to "Correlation Matrix".
    - figsize (tuple): The size of the figure. Defaults to (10, 8).
    """
    plt.figure(figsize=figsize)
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title(title)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

def plot_distribution(df,column, title="Distribution Plot", figsize=(10, 6)):
    """
    Plots the distribution of a specified column in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - column (str): The column for which to plot the distribution.
    - title (str): The title of the plot. Defaults to "Distribution Plot".
    - figsize (tuple): The size of the figure. Defaults to (10, 6).
    """
    plt.figure(figsize=figsize)
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.axvline(df[column].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    plt.axvline(df[column].median(), color='blue', linestyle='dashed', linewidth=1, label='Median')
    plt.legend()
    plt.tight_layout()
    plt.show()

def scatter_plot(df, x_column, y_column, title="Scatter Plot", figsize=(10, 6), hue=None):
    """
    Plots a scatter plot for two specified columns in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): The column for the x-axis.
    - y_column (str): The column for the y-axis.
    - title (str): The title of the plot. Defaults to "Scatter Plot".
    - figsize (tuple): The size of the figure. Defaults to (10, 6).
    """
    plt.figure(figsize=figsize)
    sns.scatterplot(data=df, x=x_column, y=y_column,hue= hue, palette='viridis')
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def box_plot(df, column, title="Box Plot", figsize=(10, 6)):
    """
    Plots a box plot for a specified column in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - column (str): The column for which to plot the box plot.
    - title (str): The title of the plot. Defaults to "Box Plot".
    - figsize (tuple): The size of the figure. Defaults to (10, 6).
    """
    plt.figure(figsize=figsize)
    sns.boxplot(x=df[column])
    plt.title(title)
    plt.xlabel(column)
    plt.show()

def plot_dendrogram(clusters, levels,method='ward', figsize=(10, 8)):
    """
    Plots a dendrogram for hierarchical clustering of the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - method (str): The linkage method to use for clustering. Defaults to 'ward'.
    - figsize (tuple): The size of the figure. Defaults to (10, 8).
    """
    
    
    plt.figure(figsize=figsize)
    
    dendrogram(clusters, orientation='top',truncate_mode="level",p=levels ,no_labels=True, distance_sort='descending', show_leaf_counts=True)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Observations')
    plt.ylabel('Distance')
    plt.show()

def plot_elbow(wcss, title="Elbow Method", figsize=(10, 6)):
    """
    Plots the elbow method for determining the optimal number of clusters.

    Parameters:
    - wcss (list): List of WCSS values for different numbers of clusters.
    - title (str): The title of the plot. Defaults to "Elbow Method".
    - figsize (tuple): The size of the figure. Defaults to (10, 6).
    """
    plt.figure(figsize=figsize)
    plt.plot(range(1, len(wcss) + 1), wcss, marker='o')
    plt.title(title)
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.xticks(range(1, len(wcss) + 1))
    plt.grid()
    plt.show()