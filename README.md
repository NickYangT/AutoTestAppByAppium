# AutoTestAppByAppium
一.配置相关工具
1.安装安卓模拟器:夜神模拟器(6.6.0.5)
2.python环境:3.6
3.appium版本:V1.5.1

二.运行
1.打开模拟器(模拟器需要开启debug模式)
2.打开appium 
3.打开cmd,输入adb connect 127.0.0.1:62001, 确认appium连接上模拟器
4.执行console脚本就行，当控制台输出：验证成功，则表示测试通过；当控制台输出：验证失败则表示，测试失败

三.思路
判断当页面到9-Day Forecast页面时，如果当前页面的第一项时间为明天，滑动到最底部，最后一项时间为后面的第九天，则页面数据正常
