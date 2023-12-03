
import pandas as pd
import os

# 设置文件路径
file_path = '/Users/zhangyuanyi/Downloads/111.xlsx'

# 读取Excel文件
df = pd.read_excel(file_path)

# 检查第B列（即索引为1的列）是否存在
if df.shape[1] > 1:
    # 拆分第B列的数据，并将其扩展为新的行
    new_rows = []
    for index, row in df.iterrows():
        genes = str(row.iloc[1]).split(';')  # 第B列数据以';'分隔
        for gene in genes:
            new_row = row.copy()
            new_row.iloc[1] = gene
            new_rows.append(new_row)

    # 创建新的DataFrame
    new_df = pd.DataFrame(new_rows, columns=df.columns)

    # 获取新文件的名称
    base_name = os.path.splitext(file_path)[0]
    new_file_name = base_name + "result.xlsx"

    # 将处理后的数据保存到新的Excel文件
    new_df.to_excel(new_file_name, index=False)

    output_file_path = new_file_name
else:
    output_file_path = "Insufficient columns in the Excel file."

output_file_path
