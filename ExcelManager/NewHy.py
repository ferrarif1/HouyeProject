import pandas as pd
import os

# 加载Excel文件（请替换为您的文件路径）
file_path = '/Users/zhangyuanyi/Downloads/NAc-GPT改/NewIdea/hip-enrichment-kegg-all-Total.xlsx'

# 使用 'openpyxl' 引擎读取Excel文件
data = pd.read_excel(file_path, nrows=22, engine='openpyxl')

# 仅保留“geneID”列和“Term”列
data = data[['geneID', 'Term']]

# 创建一个字典，用于存储每个基因及其对应的功能
gene_to_terms = {}

# 遍历原始数据
for _, row in data.iterrows():
    genes = row['geneID'].split(';')
    for gene in genes:
        if gene not in gene_to_terms:
            gene_to_terms[gene] = set()
        gene_to_terms[gene].add(row['Term'])

# 将每个基因对应的功能列表转换为用分号分隔的字符串
for gene in gene_to_terms:
    gene_to_terms[gene] = ';'.join(gene_to_terms[gene])

# 将字典转换为DataFrame
restructured_data = pd.DataFrame(list(gene_to_terms.items()), columns=['geneID', 'Terms'])

# 构建新文件的文件名和路径
result_file_path = os.path.splitext(file_path)[0] + 'result.xlsx'

# 保存处理后的数据到新文件
restructured_data.to_excel(result_file_path, index=False, engine='openpyxl')

print(f"处理后的数据已保存到：{result_file_path}")
