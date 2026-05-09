from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path
import time

def get_driver():
    driver_path = get_driver_path()
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path))
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def form_operations():
    driver = get_driver()
    
    try:
        driver.get("https://www.baidu.com")
        
        search_input = driver.find_element(By.ID, "kw")
        search_input.send_keys("ChromeDriver学习")
        print("已输入搜索关键词")
        time.sleep(2)
        
        search_input.clear()
        print("已清空输入框")
        time.sleep(1)
        
        search_input.send_keys("Selenium Python" + Keys.ENTER)
        print("已提交搜索")
        time.sleep(3)
        
        print("搜索结果页面标题:", driver.title)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    form_operations()
