from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path


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


def wait_strategies():
    """
    等待策略示例
    
    演示两种等待方式：
    1. 隐式等待（implicitly_wait）：全局等待，对所有元素生效
    2. 显式等待（WebDriverWait）：针对特定元素，更灵活
    
    常用等待条件：
    - presence_of_element_located: 元素存在于 DOM 中
    - visibility_of_element_located: 元素可见
    - element_to_be_clickable: 元素可点击
    """
    driver = get_driver()
    
    try:
        driver.implicitly_wait(10)
        
        driver.get("https://www.baidu.com")
        
        wait = WebDriverWait(driver, 10)
        
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "kw"))
        )
        print("元素已存在")
        
        search_input = wait.until(
            EC.visibility_of_element_located((By.ID, "kw"))
        )
        print("元素可见")
        
        search_input.send_keys("Selenium")
        print("已输入内容")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    wait_strategies()
