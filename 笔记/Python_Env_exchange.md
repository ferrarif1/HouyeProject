# 背景知识
Conda是一个开源的包、环境管理系统和软件分发工具，主要用于在数据科学、机器学习和科学计算等领域中管理和部署软件环境。它可以帮助用户创建独立的Python环境，并在这些环境中安装和管理各种软件包。  
Anaconda： Anaconda 在安装时会预先包含大量的科学计算、数据分析、机器学习等常用包，因此它是一个完整的数据科学平台。  
Miniconda： Miniconda 只包含了一个最小的 Python 安装，没有预先安装其他任何包。但是，你可以使用 Conda 来安装所需的包，从而构建出类似于 Anaconda 的环境。  
不安装conda时，可以直接执行python，安装conda后，python将可以在conda环境中执行，此时就可以用conda环境提供的那些代码工具库，使开发者更容易去进行人工智能的研究。 

### 系统安装多个版本python时，特别是安装了anaconda/miniconda时，在不同python环境切换采用以下步骤：  
- #### 使用系统的python执行Test.py  
首先查看环境路径，环境路径PATH是用于告诉系统在哪找到python以执行你的python文件，或者其他编程语言的库文件等等：  
   ```
   echo $PATH
   ```
此时会看到很多路径，找到如下形式的一个路径：“/Library/Frameworks/Python.framework/Versions/<version_number>/”，就是mac系统目录下的python路径（非conda环境），以后用“这个路径/python”或python3来执行你的python文件，就像这样：
   ```
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 Test.py
 ```
- #### 使用conda的python执行Test.py  
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
python --version    #查看python的版本
返回：Python 3.11.5

which python        #查看现在默认是用哪个python，可以看到这里是用anaconda3环境下的python
返回：/Users/xxx/anaconda3/bin/python
 ```
### 依赖库安装了找不到的问题
对于 Anaconda 和 Miniconda 环境，你可以使用以下方法安装 Python 库：

### 使用 `conda` 命令：

Anaconda 和 Miniconda 提供了一个名为 `conda` 的包管理器，它可以用于安装、升级和管理软件包。你可以使用以下命令来安装 Python 库：

```bash
conda install package_name
```

例如，要安装 NumPy 库，你可以运行：

```bash
conda install numpy
```

### 使用 `pip` 命令：

除了使用 `conda` 命令外，你也可以在 Anaconda 或 Miniconda 环境中使用 `pip` 命令来安装 Python 库。这是因为 Anaconda 和 Miniconda 都包含了一个独立的 Python 环境，可以通过 `pip` 来安装库：

```bash
pip install package_name
```

例如，要使用 `pip` 安装 NumPy 库，你可以运行：

```bash
pip install numpy
```

请注意，如果你在使用虚拟环境时，建议使用与虚拟环境关联的 `pip` 版本，以确保库被正确安装在特定的环境中。

总的来说，你可以选择使用 `conda` 或 `pip` 来安装 Python 库，具体取决于你的偏好以及特定的环境设置。 

### 如果pip安装后发现还是提示找不到该库，就可能是下载的库和当前python不匹配的问题，例如pip安装给了系统的python，而使用conda的python执行Test.py，自然是找不到相应的库的，此时就需要尝试按本文提到的方法切换python来执行文件。
