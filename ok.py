import pandas as pd

# Assuming df1, df2, df3, ... are your dataframes
dataframes = [df1, df2, df3, df4, df5, df6, df7]  # Add all your dataframes to this list

identifier_dict = {}

# Loop through each dataframe and record the identifiers and their corresponding indices
for idx, df in enumerate(dataframes, start=1):
    identifier_column = df.columns[0]  # Assuming the identifier column is the first column
    for identifier in df[identifier_column]:
        if identifier in identifier_dict:
            identifier_dict[identifier].append(idx)
        else:
            identifier_dict[identifier] = [idx]

# Loop through the dictionary and print the overlapping indices for each identifier
for identifier, indices in identifier_dict.items():
    if len(indices) > 1:
        print(f"{identifier} : {', '.join(map(str, indices))}")
