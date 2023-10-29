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

<div align=left><img src="https://github.com/ferrarif1/HouyeProject/blob/main/pictures/1.png" width="680px"></div>  

用“conda路径/python”或“conda路径/python3”来执行你的python文件，就像这样：   
 ```
/Users/xxx/anaconda3/python3  Test.py
 ```
- 查看系统当前默认的python是哪个：
   ```
(base) xxx@MacBook-Pro ~ % python --version    
Python 3.11.5
(base) xxx@MacBook-Pro ~ % which python        
/Users/zhangyuanyi/anaconda3/bin/python
 ```
