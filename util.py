# -*- coding:utf8 -*-
_author_ = 'sky'

from appium import webdriver
import datetime
import time




class AutoDriver:

    def __init__(self, app_conf):
        """
        app_conf = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "platformVersion": '5.1.1',
            "appPackage": '',
            "appActivity": ''
        }
        :param app_conf:
        """
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', app_conf)
        # 等主页面activity出现
        self.driver.wait_activity(".base.ui.MainActivity", 10)
        self.month_dict = {
            1: " January",
            2: " February",
            3: " March",
            4: " April",
            5: " May",
            6: " June",
            7: " July",
            8: " Aguest",
            9: " September ",
            10: " October",
            11: " November",
            12: " December"
        }


    def __del__(self):
        self.driver.quit()


    def get_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return (x, y)

    def swipe_up(self, t=1000):
        """
        向上滑动
        :return:
        """
        screen_info = self.get_size()
        self.driver.swipe(int(screen_info[0]*0.187), int(screen_info[1]*0.775), int(screen_info[0]*0.187), int(screen_info[1]*0.417),  t)

    def jugde_element_is_exsit(self, text):
        """
        判断目标元素是否存在
        :return:
        """
        path = "//android.widget.TextView[contains(@text, '{0}')]".format(text)
        try:
            self.driver.find_element_by_xpath(path)
            return True
        except Exception as e:
            print(e)
            return False

    def test_9_day_forecast(self):
        """
        执行
        :return:
        """
        today = datetime.date.today()
        tomorrow = today - datetime.timedelta(days=-1)
        nine_day_later = today - datetime.timedelta(days=-9)
        start = str(tomorrow.day) + self.month_dict[tomorrow.month]
        end = str(nine_day_later.day) + self.month_dict[nine_day_later.month]
        for i in range(4):
            self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip').click()
            time.sleep(1)
        time.sleep(5)
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()
        self.driver.find_element_by_id("hko.MyObservatory_v1_0:id/decor_content_parent")
        self.driver.find_element_by_id("android:id/content")
        self.swipe_up()
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '9-Day Forecast')]").click()
        self.driver.find_elements_by_id("hko.MyObservatory_v1_0:id/drawer_layout")
        result1 = self.jugde_element_is_exsit(start)
        self.swipe_up(200)
        result2 = self.jugde_element_is_exsit(end)
        if result1 and result2:
            print("验证成功")
        else:
            print("验证失败")

