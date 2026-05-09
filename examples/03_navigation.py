from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path
import time


def get_driver():
    """
    获取 Chrome 浏览器驱动实例
    
    Returns:
        webdriver.Chrome: Chrome 浏览器驱动实例
    """
    driver_path = get_driver_path()
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path))
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def navigation():
    """
    页面导航示例
    
    演示浏览器导航功能：
    1. 访问多个网页
    2. 后退到上一页
    3. 前进到下一页
    4. 刷新当前页面
    """
    driver = get_driver()
    
    try:
        driver.get("https://www.baidu.com")
        print("第1页 -", driver.title)
        time.sleep(2)
        
        driver.get("https://www.qq.com")
        print("第2页 -", driver.title)
        time.sleep(2)
        
        driver.back()
        print("后退到 -", driver.title)
        time.sleep(2)
        
        driver.forward()
        print("前进到 -", driver.title)
        time.sleep(2)
        
        driver.refresh()
        print("刷新后 -", driver.title)
        
    finally:
        driver.quit()


if __name__ == "__main__":
    navigation()
