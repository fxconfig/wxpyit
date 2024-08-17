# coding: utf-8
# 使用 python setup。py develop 安装包为开发者模式，会在 site-packages 下创建包名字并 link 到本文件夹，
#       这样修改代码后，不用每次都重新打包安装，直接重启服务即可。
# 实际使用时，使用 python setup.py install 安装包，安装包会复制到 site-packages 下

import re

from setuptools import find_packages, setup
from pkg_resources import parse_requirements

# 查找 version 版本号
with open('wxpyit/__init__.py', encoding='utf-8') as fp:
    version = re.search(r"__version__\s*=\s*'([\w\-.]+)'", fp.read()).group(1)

# 列出 require 依赖
with open('requirements.txt',encoding='utf-8') as fp:
    install_requires = [str(req) for req in parse_requirements(fp)]

# 长文本描述
with open('README.md', encoding='utf-8') as fp:
    readme = fp.read()

# 使用find_packages(where='.')来查找所有子目录下的包。这里的where='.'表示从setup.py所在的目录开始查找。
packages = find_packages(where='.')

setup(
    name='wxpyit',
    version=version,    
    packages=packages,                 # 明确指定要安装的包
    package_dir={'wxpyit': 'wxpyit'},  # 指定包的位置
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wxpyit = wxpyit.utils:shell_entry'
        ]
    },
    install_requires=install_requires,
    tests_require=[
        'pytest',
    ],
    url='https://github.com/fxconfig/wxpyit',
    license='MIT',
    author='Peter.Yang',
    author_email='youfou@wxpy.com',
    description='微信机器人 / 可能是最优雅的微信个人号 API',
    long_description=readme, 
    long_description_content_type='text/markdown',  # 添加这一行以指定 Markdown 格式
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
