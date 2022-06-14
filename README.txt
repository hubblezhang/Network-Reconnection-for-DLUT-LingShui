该脚本用于解决DUTers'服务器断网无法连接网络的问题，实现了检测网络状态，自动重连等功能，相关参数在auto_lingshui.py中可见
使用前务必先修改auto_lingshui.py中的username和psd变量，即自己的学号和密码

由于各种包的版本问题，在运行时有些函数的名字可能已经改变，如果无法正常使用请尝试查找code中对应你Python版本的正确函数
当然，为了避免麻烦，你也可以按以下推荐安装相关依赖包：
-python 3.8+
-selenium
-geckodriver

geckodriver是Firefox浏览器的驱动，本项目基于linux64系统，其他系统的浏览器驱动可前往https://github.com/mozilla/geckodriver/releases下载
当然，你也可以用其他浏览器的驱动

祝您使用愉快！

From: Hubble Zhang
