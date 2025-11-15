# import pandas as pd

# # Input/output files
# input_file = 'input.csv'
# output_file = 'output.csv'

# # Load CSV
# df = pd.read_csv(input_file)

# # Choose column by index (0-based)

# def oneHot(column_index):
#     column_name = df.columns[column_index]
#     one_hot_df = pd.get_dummies(df[column_name], prefix=column_name)
#     df = pd.concat([df, one_hot_df], axis=1)


# column_index_list = [0,1]
# for i in column_index_list:
#     oneHot(i)
# for i in column_index_list:
#         df = df.drop(i, axis=1)

# # Perform one-hot encoding

# # Drop the original column and concatenate the one-hot columns

# # Save to CSV
# df.to_csv(output_file, index=False)

# print(f"One-hot encoded column '{column_index_list}' merged and saved to {output_file}")

import pandas as pd

input_file = 'input.csv'
output_file = 'newOutput.csv'

df = pd.read_csv(input_file)

def oneHot(df, column_index):
    column_name = df.columns[column_index]
    one_hot_df = pd.get_dummies(df[column_name], prefix=column_name)
    df = pd.concat([df, one_hot_df], axis=1)
    return df

column_index_list = [0, 1]

# apply one-hot to each column
for i in column_index_list:
    df = oneHot(df, i)

# drop original columns
df = df.drop(df.columns[column_index_list], axis=1)

df.to_csv(output_file, index=False)

print("One-hot encoded columns saved to", output_file)


# import pandas as pd

# input_file = 'input.csv'
# output_file = 'output.csv'

# df = pd.read_csv(input_file)
# column_index_list = []
# for index,value in enumerate(df.iloc[0]):
#     try:
#         int(value)
#         pass  
#     except ValueError:
#         column_index_list.append(index)

        


# def oneHot(df, column_index):
#     column_name = df.columns[column_index]
#     one_hot_df = pd.get_dummies(df[column_name], prefix=column_name)
#     df = pd.concat([df, one_hot_df], axis=1)
#     return df


# # apply one-hot to each column
# for i in column_index_list:
#     df = oneHot(df, i)

# # drop original columns
# df = df.drop(df.columns[column_index_list], axis=1)

# df.to_csv(output_file, index=False)

# print("One-hot encoded columns saved to", output_file)

# import pandas as pd

# input_file = 'input.csv'
# output_file = 'output.csv'

# df = pd.read_csv(input_file)

# # Determine which columns are non-numeric in the first row
# column_index_list = []
# for index, value in enumerate(df.iloc[0]):
#     try:
#         int(value)
#     except:
#         column_index_list.append(index)

# def oneHot(df, column_index):
#     column_name = df.columns[column_index]
#     one_hot_df = pd.get_dummies(df[column_name], prefix=column_name)
#     df = pd.concat([df, one_hot_df], axis=1)
#     return df

# # Save column names to drop later (before df changes)
# cols_to_drop = [df.columns[i] for i in column_index_list]

# for i in column_index_list:
#     df = oneHot(df, i)

# df = df.drop(columns=cols_to_drop)

# df.to_csv(output_file, index=False)

# print("One-hot encoded columns saved to", output_file)

# import pandas as pd

# input_file = 'input.csv'
# output_file = 'output.csv'

# df = pd.read_csv(input_file)

# def oneHot(df, column_name):
#     one_hot_df = pd.get_dummies(df[column_name], prefix=column_name)
#     df = pd.concat([df, one_hot_df], axis=1)
#     return df

# # columns you want to encode (0 and 1 from the original dataframe)
# column_index_list = [0, 1]

# # save names BEFORE any modification
# cols_to_encode = [df.columns[i] for i in column_index_list]

# # apply one-hot encoding
# for col in cols_to_encode:
#     df = oneHot(df, col)

# # drop original columns by name (safe)
# df = df.drop(columns=cols_to_encode)

# df.to_csv(output_file, index=False)

# print("One-hot encoded columns saved to", output_file)