# 小鼠开颅手术前后智力评估研究项目

## 项目简介

本项目旨在研究小鼠在动开颅手术后智力水平的变化，通过实施动开颅手术并进行智力评估实验，我们将探讨手术对小鼠认知能力的潜在影响。

## 学习内容 🧑‍🎓

本项目涉及以下学习内容：

- Python编程语言 [菜鸟教程（推荐）](https://www.runoob.com/python/python-tutorial.html)    [莫烦Python](https://mofanpy.com/tutorials/python-basic/interactive-python/) 
- 基本的数据分析和统计学知识
- 人工智能基础概念

## 笔记--多种Python环境之间的切换
Anaconda： Anaconda 在安装时会预先包含大量的科学计算、数据分析、机器学习等常用包，因此它是一个完整的数据科学平台。  
Miniconda： Miniconda 只包含了一个最小的 Python 安装，没有预先安装其他任何包。但是，你可以使用 Conda 来安装所需的包，从而构建出类似于 Anaconda 的环境。  
安装这俩conda时，python将可以在conda环境中执行，简单说就是可以直接用conda环境提供的那些代码库，使开发者更容易去进行人工智能的研究。 
### 系统安装多个版本python时，特别是安装了anaconda/miniconda时，在不同python环境切换采用以下步骤：  
- （1）使用系统的python执行Test.py  
首先查看环境路径，这是用于告诉系统在哪找到python以执行你的python文件：  
   ```
   echo $PATH
   ```
此时会看到很多路径 找到其中这个：/Library/Frameworks/Python.framework/Versions/<version_number>/，就是系统目录下的python路径，以后用“这个路径/python”或python3来执行你的python文件，就像这样：
   ```
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 Test.py
 ```
- （2）使用conda的python执行Test.py  
安装anaconda或者miniconda后，一般会自动覆盖系统的，也就是默认输入的python就会是conda目录下的，可以这样查看其具体目录：
 ```
conda info --envs
 ```

<div align=center><img src="https://github.com/ferrarif1/HouyeProject/blob/main/pictures/1.png" width="680px"></div>  
   
 ```
# 2.：
/Users/zhangyuanyi/anaconda3/python3  Test.py
 ```

## 项目目录结构 📓

- `/data`：存放实验数据
- `/notebooks`：用于数据分析和实验记录
- `/scripts`：存放用于数据处理和分析的Python脚本
- `/results`：存放实验结果和可视化输出

## 如何开始 🚀

1. **克隆项目到本地环境：**
   ```
   git clone https://github.com/ferrarif1/HouyeProject
   ```

2. **安装所需的Python库：**  
   Pandas（用于数据处理）、Matplotlib（用于数据可视化）、NumPy（用于数值计算）
   ```
   pip install pandas matplotlib numpy
   ```

3. **开始实验和数据分析：**
   


# 相关资料 💾

## 安装依赖资源
- [Anaconda 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)


## 相关库链接 

- [DeepLabCut ：通过深度学习对所有动物（包括动物）进行用户定义特征的无标记姿势估计](https://github.com/DeepLabCut/DeepLabCut)

## GPT读论文神器
- [Chatpdf：上传论文给你解读](https://www.chatpdf.com/)

- [hammerscholar：能在线检索 给Doi号就能看论文](https://pdf.hammerscholar.net/)
