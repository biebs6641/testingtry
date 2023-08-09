import pandas as pd

# Number of dataframes you want to create
num_dataframes = 5

# Dictionary to store empty dataframes
empty_dataframes = {}

# Create empty dataframes in a loop
for i in range(1, num_dataframes + 1):
    dataframe_name = f"df_{i}"  # Change this to your naming convention
    empty_dataframes[dataframe_name] = pd.DataFrame(columns=['identifier'])  # Replace 'identifier' with your column name

# Print the created empty dataframes
for df_name, df in empty_dataframes.items():
    print(f"Empty DataFrame '{df_name}':\n{df}")
