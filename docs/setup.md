# setup.py 学习

***开发详见 (4.4、以开发方式安装)***

## 1. 概述
在Python开发中，我们经常需要将自己的代码打包成可供其他人使用的库或应用程序。为了方便用户安装和使用，我们需要创建一个配置文件 setup.py，用于定义打包的相关信息和依赖项。本文将详细介绍如何编写 setup.py 文件，并展示每一步需要做什么。



### 1.1 为什么需要对项目分发打包？
平常我们习惯了使用 pip 来安装一些第三方模块，这个安装过程之所以简单，是因为模块开发者为我们默默地为我们做了所有繁杂的工作，而这个过程就是 打包。

打包，就是将你的源代码进一步封装，并且将所有的项目部署工作都事先安排好，这样使用者拿到后即装即用，不用再操心如何部署的问题（如果你不想对照着一堆部署文档手工操作的话）。

不管你是在工作中，还是业余准备自己写一个可以上传到 PyPI 的项目，你都要学会如何打包你的项目。

Python 发展了这么些年了，项目打包工具也已经很成熟了。他们都有哪些呢？

你可能听过 disutils、 distutils 、distutils2、setuptools等等，好像很熟悉，却又很陌生，他们都是什么关系呢？


### 1.2 包分发的始祖：distutils
distutils 是 Python 的一个标准库，从命名上很容易看出它是一个分发（distribute）工具（utlis），它是 Python 官方开发的一个分发打包工具，所有后续的打包工具，全部都是基于它进行开发的。

distutils 的精髓在于编写 setup.py，它是模块分发与安装的指导文件。

那么如何编写 setup.py 呢？这里面的内容非常多，我会在后面进行详细的解析，请你耐心往下看。

你有可能没写过 setup.py ，但你绝对使用过 setup.py 来做一些事情，比如下面这条命令，我们经常用它来进行模块的安装。

python setup.py install
这样的安装方法是通过源码安装，与之对应的是通过二进制软件包的安装，同样我也会在后面进行介绍。


### 1.3 分发工具升级：setuptools
setuptools 是 distutils 增强版，不包括在标准库中。其扩展了很多功能，能够帮助开发者更好的创建和分发 Python 包。大部分 Python 用户都会使用更先进的 setuptools 模块。

distribute，或许你在其他地方也见过它，这里也提一下。

distribute 是 setuptools 有一个分支版本，分支的原因可能是有一部分开发者认为 setuptools 开发太慢了。但现在，distribute 又合并回了 setuptools 中。因此，我们可以认为它们是同一个东西。

还有一个大包分发工具是 distutils2，其试图尝试充分利用distutils，setuptools 和 distribute 并成为 Python 标准库中的标准工具。但该计划并没有达到预期的目的，且已经是一个废弃的项目。

因此，setuptools 是一个优秀的，可靠的 Python 包安装与分发工具。


## 2. setup.py 文件的创建
首先，我们需要在项目的根目录下创建一个 setup.py 文件。这个文件将包含我们用于打包的配置信息。


## 3、详解 setup.py 的编写：
```python
import re

from setuptools import find_packages, setup
from pkg_resources import parse_requirements

with open('wxpy-itchat/__init__.py', encoding='utf-8') as fp:
    version = re.search(r"__version__\s*=\s*'([\w\-.]+)'", fp.read()).group(1)

with open('requirements.txt',encoding='utf-8') as fp:
    install_requires = [str(req) for req in parse_requirements(fp)]

with open('README.md', encoding='utf-8') as fp:
    readme = fp.read()
setup(
    name='wxpy-itchat',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wxpy-itchat = wxpy-itchat.utils:shell_entry'
        ]
    },
    install_requires=install_requires,
    tests_require=[
        'pytest',
    ],
    url='https://github.com/fxconfig/wxpy-itchat',
    license='MIT',
    author='Peter.Yang',
    author_email='youfou@wxpy.com',
    description='微信机器人 / 可能是最优雅的微信个人号 API',
    long_description=readme,
    keywords=[
        '微信',
        'WeChat',
        'API',
        'itchat',
        '机器人',
        'bot',
        'wx bot',
        'wxpy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9+',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Utilities',
    ]
)
```

### 3.1、基础描述信息：
* name: 包的名称
* version: (-V) 包的版本号
* author: 包的作者姓名
* author_email: 作者的电子邮件地址
* maintainer 维护者
* maintainer_email 维护者的邮箱地址
* description: 包的简要描述
* long_description 程序的详细描述
* url: 包的项目主页
* platforms 程序适用的软件平台列表


#### 3.1.1 程序分类信息
classifiers: 用于指定所属分类的列表，例如所支持的Python版本、所使用的许可证等.

所有支持的分类列表见：<https://pypi.org/pypi?%3Aaction=list_classifiers>


### 3.2、包的进阶信息：
* data_files：（如果没有可以不写）装过程中，需要安装的静态文件，如配置文件、service文件、图片等​​​​​​

* packages: （自动搜索 Python 包）包含的模块列表（包含__init__.py的文件夹），这里通常使用 find_packages()，它默认在和setup.py同一目录下搜索各个含有 __init__.py的包。 
  > 有些不想要进行打包的文件可以排除
  >
  > 我们指定 packages 后会自动将指定的 package 下的源代码进行打包。但是有的时候会有很多 subpackage，这个时候 setuptools 提 供了 find_packages 来找到所有的 subpackages。

* install_requires：（自动安装依赖）

    > install_requires = ["requests"]: 需要安装的依赖包。我们可以首先生成 requirements.txt 文件，接着使用生成的文件生成需要的参数。关于生成 requirements.txt 文件，可以参考Python自动生成requirements.txt文件。
    > 
    > 这个参数是在 setup.py 文件中指定依赖，然后在使用 setuptools 安装应用时，依赖包的相应版本就会被自动安装。但是通常情况下，手动写依赖会比较麻烦，我们可以使用 pipreqs 首先自动生成 requirement.txt 文件，接着读取这部分文件即可。
    > 
    > 关于 install_requires， 有以下五种常用的表示方法：

    - 'argparse'，只包含包名。这种形式只检查包的存在性，不检查版本。方便，但不利于控制风险。
    - 'setuptools==38.2.4'，指定版本。这种形式把风险降到了最低，确保了开发、测试与部署的版本一致，不会出现意外。缺点是不利于更新，每次更新都需要改动代码。
    - 'docutils >= 0.3'，这是比较常用的形式。当对某个库比较信任时，这种形式可以自动保持版本为最新。

    - 'Django &gt;= 1.11, != 1.11.1, <= 2'，这是比较复杂的形式。如这个例子，保证了Django的大版本在1.11和2之间，也即1.11.x；并且，排除了已知有问题的版本1.11.1（仅举例）。对于一些大型、复杂的库，这种形式是最合适的。

    - 'requests[security, socks] >= 2.18.4'，这是包含了额外的可选依赖的形式。正常安装requests会自动安装它的install_requires中指定的依赖，而不会安装security和socks这两组依赖。这两组依赖是定义在它的extras_require中。这种形式，用在深度使用某些库时。

* include_package_data: 引入非 Python 文件。默认情况下只会对 Python 源码进行打包，但是如果我们想要将其他静态文件，例如 css 文件，或是 qt 的一些 ui 文件打包进去，就需要使用这个参数。后面会有详细的介绍。

* ext_modules

 > ext_modules参数用于构建 C 和 C++ 扩展扩展包。其是 Extension 实例的列表，每一个 Extension 实例描述了一个独立的扩展模块，扩展模块可以设置扩展包名，头文件、源文件、链接库及其路径、宏定义和编辑参数等。如：
 > 
 > 详细了解可参考：2. Writing the Setup Script — Python 3.6.15 documentation


### 3.3、制作命令行工具：
> entry_points： 动态发现服务和插件，可以用来制作命令行工具。也就是我们可以通过一些简单的命令，来运行 Python 项目中的指定文件或是函数。下面会详细进行介绍。
> 
> entry_points 的说明
> entry_points 可以用来创建控制台脚本。我们看上面的例子就会非常好理解：
> 
> 这样在安装完毕之后，我们可以直接在控制台输入 wxpy-itchat ，这样是可以运行 wxpy-itchat.utils 模块下的 shell_entry 函数。
```python
    entry_points={
        'console_scripts': [
            'wxpy-itchat = wxpy-itchat.utils:shell_entry'
        ]
    },
```


## 4、执行安装文件
在有了上面的 setup.py 文件之后，我们就可以进行打包，也可以将应用安装在本地的 Python 环境中了。一共有以下的四种安装方式：


### 4.1、创建 egg 包
下面的命令会在当前目录下的 dist 目录内创建一个 egg 文件。文件名格式就是 应用名-版本号-Python版本.egg。同时你会注意到，当前目录多了 build 和 应用名.egg-info 子目录来存放打包的中间结果。（主要是看 dist 目录下的内容）
```sh
python setup.py bdist_egg
```

### 4.2、创建 tar.gz 包
这个命令和上例类似，只不过创建的文件类型是 tar.gz，文件名为 应用名-版本号.tar.gz。也是保存在 dist 文件夹下。
```sh
python setup.py sdist --format=gztar
```

### 4.3、安装应用
下面的安装命令会将当前的 Python 应用安装到当前 Python 环境的 site-packages 目录下，这样其他程序就可以像导入标准库一样导入该应用的代码了。
```sh
python setup.py install
# 或者
pip install . #(未测试)
```

这里我们如果想要删除安装的包，可以使用 pip uninstall xxx 来完成删除。


### 4.4、以开发方式安装
如果应用在开发过程中会频繁变更，每次安装还需要先将原来的版本卸掉，这样就会很麻烦。如果使用 develop 开发方式安装的话，应用代码不会真的被拷贝到本地 Python 环境的 site-packages 目录下，而是在 site-packages 目录里创建一个指向当前应用位置的链接。这样如果当前位置的源码被改动，就会马上反映到 site-packages 里。
```sh
python setup.py develop
# 或者
pip install -e . 
```

是 pip 命令的一种使用方式，它表示在当前目录下安装一个可编辑包。具体含义如下：

- pip 是 Python 的软件包管理器，用于安装、卸载和管理 Python 包；
- install 是 pip 命令的一个子命令，用于安装 Python 包；
- -e 表示使用可编辑模式安装包，即把包安装到当前目录，并且可以通过编辑包代码实时调试；
- . 表示安装当前目录下的包。
  
因此，pip install -e . 的含义是：在当前目录下安装一个包，并创建一个软连接引用该包（而不是将包复制到 site-packages 目录下）。这个软连接是一个指向包代码的符号链接，它可以使包的修改直接反映到当前目录下的项目中，从而方便开发和调试。