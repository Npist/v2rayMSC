# v2rayMSC 跨平台多用户v2ray客户端
本项目基于v2rayMS项目：https://github.com/Npist/v2rayMS<br />
使用Python3.6+pyQT5进行开发<br />
优点跨平台、缺点打包出来程序较大<br />
UI及CSS参考修改自：https://github.com/892768447/QtSkin<br />
使用v2rayMS项目的clientapi.php进行通讯<br />
通讯过程使用RSA加密<br />
业余练手之作，欢迎交流 npist35@gmail.com<br />
<br />
# 进度
界面：50%<br />
数据交互：80%<br />
v2ray客户端调用: 0%<br />
<br />
# 更新日志
## 2018.10.19
初始版本<br />
界面基本确定，后续优化及完善中。。<br />
服务器交互大部分完成<br />
下次更新不知道什么时候<br />
<br />
# 部分截图
![Login](./source/1.png)
![Main1](./source/2.png)
![Main2](./source/3.png)
![Main3](./source/4.png)
# 使用说明
1.使用项目中提供的create_rsa_key.py生成RSA密钥对（建议使用两对）<br />
2.将生成的密钥对的内容分别对应填写进./CoreInclude/CoreLogic.py及clientapi.php的对应位置中<br />
3.运行v2rayMSC.py执行主程序（可使用pyinstaller或py2app打包成exe或app）<br />