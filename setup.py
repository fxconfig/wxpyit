# coding: utf-8
# from __future__ import unicode_literals

import re

from setuptools import find_packages, setup
from pkg_resources import parse_requirements

with open('wxpyit/__init__.py', encoding='utf-8') as fp:
    version = re.search(r"__version__\s*=\s*'([\w\-.]+)'", fp.read()).group(1)

with open('requirements.txt',encoding='utf-8') as fp:
    install_requires = [str(req) for req in parse_requirements(fp)]

with open('README.md', encoding='utf-8') as fp:
    readme = fp.read()

setup(
    name='wxpyit',
    version=version,
    packages=find_packages(),
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
