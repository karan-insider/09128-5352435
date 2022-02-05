import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import
from selenium.webdriver.common.keys import Keys
import time
from time import sleep


def test_lambdatest1_2():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://www.youtube.com/')
    chrome_driver.maximize_window()

    title = "Youtube"
    assert title == chrome_driver.title

    search_text = "arrahman"
    search_box = chrome_driver.find_element_by_xpath("//input[@name='q']")
    search_box.send_keys(search_text)

    time.sleep(5)

    # Option 1 - To Submit the search
    # search_box.submit()

    # Option 2 - To Submit the search
    search_box.send_keys(Keys.ARROW_DOWN)
    search_box.send_keys(Keys.ARROW_UP)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)


    time.sleep(5)
    assert title == chrome_driver.title

    chrome_driver.close()