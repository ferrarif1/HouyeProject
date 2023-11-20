import os

import pandas as pd

def extract_unique_functions(df, column_name):
    unique_functions = set()
    for item in df[column_name].dropna():
        functions = item.split('|')
        unique_functions.update(functions)
    return unique_functions

def process_gene_data_with_empty_handling(df, column_name):
    unique_functions = sorted(extract_unique_functions(df, column_name))
    function_groups = {func: [] for func in unique_functions if func.strip()}
    function_groups['Other'] = []

    for index, row in df.iterrows():
        funcs = str(row[column_name]).split('|') if pd.notna(row[column_name]) and row[column_name].strip() else ['Other']
        for func in funcs:
            if func in function_groups:
                function_groups[func].append(index)
            else:
                function_groups['Other'].append(index)

    processed_data = pd.DataFrame()

    for func, indices in function_groups.items():
        subset = df.loc[indices].copy()
        subset.insert(0, 'Function_Group', func)
        subset.insert(1, 'Original_Row_Number', subset.index + 1)
        processed_data = pd.concat([processed_data, subset], ignore_index=False)

    return processed_data

def insert_blank_rows_for_groups(df, group_column):
    new_df = pd.DataFrame()
    for _, group_data in df.groupby(group_column):
        new_df = pd.concat([new_df, group_data], ignore_index=True)
        new_df = pd.concat([new_df, pd.Series(dtype='object').to_frame().T], ignore_index=True)
    if len(new_df) > 0:
        new_df = new_df.iloc[:-1]
    return new_df

def generate_output_file_path(file_path):
    """
    Generate the output file path by adding "_modified" before the file extension in the original file path.

    Args:
    file_path (str): The original file path.

    Returns:
    str: The modified file path with "_modified" appended before the file extension.
    """
    # Find the last dot, indicating the start of the file extension
    dot_index = file_path.rfind('.')
    # Append "_modified" before the file extension
    modified_file_path = file_path[:dot_index] + '_modified' + file_path[dot_index:]
    return modified_file_path






def rename_xls_to_xlsx(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(root, file)  # 获取文件的完整路径
                print(file_path)
                final_processed_output_file_path = generate_output_file_path(file_path)

                print(final_processed_output_file_path)

                # data = pd.read_excel(file_path)
                # 在读取 Excel 文件时显式指定引擎
                # 对于 .xlsx 文件，使用 'openpyxl'
                # 对于 .xls 文件，使用 'xlrd'
                engine = 'openpyxl' if 'xlsx' in file_path else 'xlrd'
                data = pd.read_excel(file_path, engine=engine)

                if 'GO' in file_path :
                    # Process the data based on the 'GO_term' column (assumed to be column 'D')
                    final_processed_data = insert_blank_rows_for_groups(
                        process_gene_data_with_empty_handling(data, 'GO_term'), #GO_term / pathway_description
                        'Function_Group'
                    )
                    final_processed_data.to_excel(final_processed_output_file_path, index=False)

                else:
                    final_processed_data = insert_blank_rows_for_groups(
                        process_gene_data_with_empty_handling(data, 'pathway_description'), #GO_term / pathway_description
                        'Function_Group'
                    )
                    final_processed_data.to_excel(final_processed_output_file_path, index=False)


# 指定目录路径
directory_path = "/Users/zhangyuanyi/Downloads/待整理文件/"

# 执行函数
rename_xls_to_xlsx(directory_path)
