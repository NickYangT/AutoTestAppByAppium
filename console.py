# -*- coding:utf8 -*-
_author_ = 'sky'



from utils.util import AutoDriver



if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "platformVersion": '5.1.1',
        "appPackage": 'hko.MyObservatory_v1_0',
        "appActivity": 'hko.homepage.Homepage2Activity'
    }
    a = AutoDriver(desired_caps)
    a.test_9_day_forecast()
