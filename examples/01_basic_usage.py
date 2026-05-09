from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_driver_path


def get_driver():
    """
    获取 Chrome 浏览器驱动实例
    
    优先使用配置文件中指定的 ChromeDriver 路径，
    如果未配置，则使用 webdriver-manager 自动下载匹配的 ChromeDriver
    
    Returns:
        webdriver.Chrome: Chrome 浏览器驱动实例
    """
    driver_path = get_driver_path()
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path))
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def basic_usage():
    """
    ChromeDriver 基础用法示例
    
    演示以下功能：
    1. 打开浏览器并访问网页
    2. 获取页面标题和 URL
    3. 窗口操作：最大化、设置大小、最小化
    4. 关闭浏览器
    """
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
