from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path

def get_driver():
    driver_path = get_driver_path()
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path))
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def basic_usage():
    driver = get_driver()
    
    try:
        driver.get("https://www.baidu.com")
        print("当前页面标题:", driver.title)
        print("当前页面URL:", driver.current_url)
        
        driver.maximize_window()
        print("窗口已最大化")
        
        driver.set_window_size(800, 600)
        print("窗口大小已设置为 800x600")
        
        driver.minimize_window()
        print("窗口已最小化")
        
        driver.maximize_window()
        
    finally:
        driver.quit()

if __name__ == "__main__":
    basic_usage()
