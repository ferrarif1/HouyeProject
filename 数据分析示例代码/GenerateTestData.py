import pandas as pd
import numpy as np

# 生成随机测试数据
np.random.seed(0)

# 创建一个包含30个变量的随机测试数据
data = {
    f'Variable{i}': np.random.rand(1000) for i in range(1, 31)
}

# 添加统计学关系
data['Variable2'] = 2 * data['Variable1'] + np.random.normal(0, 0.1, 1000)
data['Variable3'] = 0.5 * data['Variable1'] + 0.7 * data['Variable2'] + np.random.normal(0, 0.1, 1000)
data['Variable5'] = 3 * data['Variable2'] + np.random.normal(0, 0.1, 1000)

# 创建DataFrame
df = pd.DataFrame(data)

# 保存数据到 Excel 文件
df.to_excel('数据分析示例代码/clinical_data_test.xlsx', index=False)
