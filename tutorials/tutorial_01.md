# 教程 1：ChromeDriver 入门（国内用户版）

## 目标

本教程将带你完成以下任务：
1. 安装必要的依赖
2. 配置 ChromeDriver（使用国内镜像）
3. 编写第一个自动化脚本（使用国内网站）
4. 理解基本的浏览器操作

## 步骤 1：安装依赖

确保已安装 Python 3.8+，然后安装 Selenium：

```bash
# 配置国内 pip 源（推荐）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装依赖
pip install selenium webdriver-manager
```

## 步骤 2：下载 ChromeDriver（国内用户指南）

### 2.1 查看 Chrome 版本

打开 Chrome 浏览器 → 设置 → 关于 Chrome

### 2.2 下载对应版本

**推荐使用国内镜像：**
- ✅ 淘宝镜像：https://npm.taobao.org/mirrors/chromedriver/
- 腾讯镜像：https://mirrors.cloud.tencent.com/chromedriver/

**下载步骤：**
1. 在镜像网站找到与你的 Chrome 版本匹配的目录
2. 下载对应系统的压缩包（如：chromedriver_win32.zip）
3. 解压到合适的位置

## 步骤 3：第一个脚本（使用国内网站）

创建 `first_script.py`：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 配置 ChromeDriver 路径（请修改为你的实际路径）
driver_path = "D:/APP/Chrome/chromedriver/chromedriver.exe"

# 创建浏览器实例
driver = webdriver.Chrome(service=Service(driver_path))

try:
    # 访问国内网站 - 百度首页
    driver.get("https://www.baidu.com")
    
    # 打印页面标题
    print("页面标题:", driver.title)
    
    # 打印当前URL
    print("当前URL:", driver.current_url)
    
    # 等待3秒
    import time
    time.sleep(3)
    
finally:
    # 关闭浏览器
    driver.quit()
```

运行脚本：
```bash
python first_script.py
```

**预期输出：**
```
页面标题: 百度一下，你就知道
当前URL: https://www.baidu.com/
```

## 步骤 4：浏览器窗口操作

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service("path/to/chromedriver"))

try:
    # 访问国内网站
    driver.get("https://www.baidu.com")
    
    # 最大化窗口
    driver.maximize_window()
    print("窗口已最大化")
    time.sleep(2)
    
    # 设置窗口大小
    driver.set_window_size(800, 600)
    print("窗口大小: 800x600")
    time.sleep(2)
    
    # 最小化窗口
    driver.minimize_window()
    print("窗口已最小化")
    time.sleep(2)
    
finally:
    driver.quit()
```

## 步骤 5：页面导航（使用国内网站）

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service("path/to/chromedriver"))

try:
    # 访问第一个国内网站
    driver.get("https://www.baidu.com")
    print("第1页:", driver.title)
    time.sleep(2)
    
    # 访问第二个国内网站
    driver.get("https://www.taobao.com")
    print("第2页:", driver.title)
    time.sleep(2)
    
    # 访问第三个国内网站
    driver.get("https://www.jd.com")
    print("第3页:", driver.title)
    time.sleep(2)
    
    # 返回上一页
    driver.back()
    print("后退:", driver.title)
    time.sleep(2)
    
    # 前进到下一页
    driver.forward()
    print("前进:", driver.title)
    time.sleep(2)
    
    # 刷新页面
    driver.refresh()
    print("已刷新")
    
finally:
    driver.quit()
```

## 国内用户小贴士

### 小贴士 1：常用国内测试网站

| 网站 | 网址 | 用途 |
|------|------|------|
| 百度 | https://www.baidu.com | 搜索测试 |
| 淘宝 | https://www.taobao.com | 电商测试 |
| 京东 | https://www.jd.com | 电商测试 |
| 知乎 | https://www.zhihu.com | 社交测试 |
| 豆瓣 | https://www.douban.com | 社交测试 |

### 小贴士 2：网络问题处理

如果遇到网络连接问题：
1. 使用国内网站进行测试
2. 检查网络设置
3. 尝试关闭 VPN/代理后再试

## 练习

1. 修改脚本，访问你喜欢的国内网站
2. 添加更多窗口操作
3. 尝试导航到多个国内网站

## 下一步

继续学习 [教程 2：元素定位与操作](tutorial_02.md)
