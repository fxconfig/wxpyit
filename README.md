# wxpyit: 用 Python 玩微信  

### 合并 wxpy + itchat-uos
原来项目作者未更新，我合并了 wxpy 和 itchat-uos 改名为 wxpyit

> 改动部分
- itchat config.py 文件中添加了一些 ***FAKE_HEADERS*** 
- wxpy 去掉 Python2 兼容层，移动了一些文件


> **强烈建议仅使用小号运行机器人！**

> 从 (17年6月下旬) 反馈来看，使用机器人存在一定概率被限制登录的可能性。
> 
> 主要表现为无法登陆 Web 微信 (但不影响手机等其他平台)。
>
>  17 年以后新注册的微信号需要  启用 ***微信支付*** 之后才能扫码登录微信



## 轻松安装-不轻松，作者整努力修改 setup.py 中

wxpyit 考虑只支持 Python 3.9 以上版本，因为语法糖确实香

由于没有发布 PyPi，所以需要手动安装
```sh
git clone https://github.com/fxconfig/wxpyit.git
```



## 简单上手
```sh
git clone 我
cd wxpy-itchat
python setup.py install
```



#### 登陆微信:

```python
    # 导入模块
    from wxpy-itchat import *
    # 初始化机器人，扫码登陆
    bot = Bot()
```
#### 找到好友:

```python
    # 搜索名称含有 "游否" 的男性深圳好友
    my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]
```

#### 发送消息:

```python
    # 发送文本给好友
    my_friend.send('Hello WeChat!')
    # 发送图片
    my_friend.send_image('my_picture.jpg')
```

#### 自动响应各类消息:

```python
    # 打印来自其他好友、群聊和公众号的消息
    @bot.register()
    def print_others(msg):
        print(msg)

    # 回复 my_friend 的消息 (优先匹配后注册的函数!)
    @bot.register(my_friend)
    def reply_my_friend(msg):
        return 'received: {} ({})'.format(msg.text, msg.type)

    # 自动接受新的好友请求
    @bot.register(msg_types=FRIENDS)
    def auto_accept_friends(msg):
        # 接受好友请求
        new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，我自动接受了你的好友请求')
```

#### 保持登陆/运行:

```python

    # 进入 Python 命令行、让程序保持运行
    embed()

    # 或者仅仅堵塞线程
    # bot.join()
```


## 模块特色
----------------

* 全面对象化接口，调用更优雅
* 默认多线程响应消息，回复更快
* 包含 聊天机器人、共同好友 等 `实用组件 <http://wxpy.readthedocs.io/zh/latest/utils.html>`_
* 只需两行代码，在其他项目中用微信接收警告
* `愉快的探索和调试 <http://wxpy.readthedocs.io/zh/latest/console.html>`_，无需涂涂改改
* 可混合使用 itchat 的原接口
* 当然，还覆盖了各类常见基本功能:

    * 发送文本、图片、视频、文件
    * 通过关键词或用户属性搜索 好友、群聊、群成员等
    * 获取好友/群成员的昵称、备注、性别、地区等信息
    * 加好友，建群，邀请入群，移出群

## 说明文档
----------------

<https://github.com/fxconfig/wxpyit>

更新日志
----------------

<https://github.com/fxconfig/wxpyit>

项目主页
----------------

<https://github.com/fxconfig/wxpyit>
