import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. 从Excel中读取临床医学统计数据
excel_file = "数据分析示例代码/clinical_data_test.xlsx"  # 将文件名替换为你的Excel文件名
df = pd.read_excel(excel_file)

# 2. 计算变量之间的关联性
correlation_matrix = df.corr()

# 3. 寻找强关联的变量对
strong_correlations = correlation_matrix[correlation_matrix.abs() > 0.7].stack()

# 4. 绘制点状图反映关联关系
for (var1, var2), correlation in strong_correlations.items():
    if var1 != var2:
        plt.scatter(df[var1], df[var2], label=f'{var1} vs {var2}, Corr={correlation:.2f}')

plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
plt.title("Correlation Scatter Plots")
plt.legend()
plt.show()

# 5. 计算关系的参数方程（假设为线性关系）
for (var1, var2), correlation in strong_correlations.items():
    if var1 != var2:
        slope, intercept, r_value, p_value, std_err = stats.linregress(df[var1], df[var2])
        print(f"The linear equation between {var1} and {var2}: y = {slope:.2f}x + {intercept:.2f}")
