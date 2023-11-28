import pandas as pd

# 定义文件路径
result_file_path = '/Users/zhangyuanyi/Downloads/NAc-GPT改/NewIdea/hip-enrichment-kegg-all-Totalresult.xlsx'
new_file_path = '/Users/zhangyuanyi/Downloads/NAc-GPT改/NewIdea/NPs-1.2FC-hip-SN-C-DEG.xlsx'

# 从结果文件中读取基因，创建基因集合A
result_data = pd.read_excel(result_file_path)
genes_set_A = set(result_data['geneID'].str.split(';').explode())

# 加载新文件
new_data = pd.read_excel(new_file_path)

# 现在新文件中的基因列已被更正为'geneID'
# 仅保留集合A中的基因行
filtered_data = new_data[new_data['geneID'].isin(genes_set_A)]

# 为新文件中的每行添加原始行号
filtered_data['OriginalRowNumber'] = filtered_data.index + 1

# 定义输出文件的路径
output_file_path = new_file_path.replace('.xlsx', '') + 'Result.xlsx'

# 将过滤后的数据保存到输出文件
filtered_data.to_excel(output_file_path, index=False)

print("处理后的数据已保存到文件：", output_file_path)
