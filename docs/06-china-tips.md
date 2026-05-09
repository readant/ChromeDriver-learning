# ChromeDriver 国内用户专属技巧

## 1. 国内镜像资源汇总

### 1.1 ChromeDriver 国内镜像

| 镜像名称 | 地址 | 状态 |
|---------|------|------|
| 淘宝镜像 | https://npm.taobao.org/mirrors/chromedriver/ | ✅ 推荐 |
| 腾讯镜像 | https://mirrors.cloud.tencent.com/chromedriver/ | ✅ 可用 |
| 华为镜像 | https://mirrors.huaweicloud.com/chromedriver/ | ✅ 可用 |
| 阿里镜像 | https://mirrors.aliyun.com/chromedriver/ | ✅ 可用 |

### 1.2 Python 国内镜像

| 镜像名称 | 地址 |
|---------|------|
| 清华镜像 | https://pypi.tuna.tsinghua.edu.cn/simple |
| 阿里镜像 | https://mirrors.aliyun.com/pypi/simple |
| 豆瓣镜像 | https://pypi.douban.com/simple |

**配置方法：**
```bash
# 临时使用
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple

# 永久配置
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 1.3 Conda 国内镜像

编辑 `~/.condarc` 文件：

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

## 2. 国内常用测试网站

### 2.1 搜索类

| 网站 | 网址 | 测试用途 |
|------|------|---------|
| 百度 | https://www.baidu.com | 搜索功能测试 |
| 必应中国 | https://cn.bing.com | 搜索功能测试 |

### 2.2 电商类

| 网站 | 网址 | 测试用途 |
|------|------|---------|
| 淘宝 | https://www.taobao.com | 商品搜索、购物流程 |
| 天猫 | https://www.tmall.com | 商品搜索、购物流程 |
| 京东 | https://www.jd.com | 商品搜索、购物流程 |
| 拼多多 | https://www.pinduoduo.com | 商品搜索、购物流程 |

### 2.3 社交类

| 网站 | 网址 | 测试用途 |
|------|------|---------|
| 知乎 | https://www.zhihu.com | 问答、搜索 |
| 微博 | https://www.weibo.com | 社交、搜索 |
| 豆瓣 | https://www.douban.com | 图书、电影评论 |

### 2.4 新闻类

| 网站 | 网址 | 测试用途 |
|------|------|---------|
| 网易新闻 | https://news.163.com | 新闻浏览 |
| 新浪新闻 | https://news.sina.com.cn | 新闻浏览 |
| 腾讯新闻 | https://news.qq.com | 新闻浏览 |

## 3. 网络问题解决方案

### 3.1 无法访问 Google 网站

**问题描述：**
```
WebDriverException: unknown error: net::ERR_CONNECTION_TIMED_OUT
```

**解决方案：**
1. **使用国内网站**：将测试目标改为百度、淘宝等国内网站
2. **配置 hosts**（不推荐）：修改 hosts 文件
3. **使用代理**（如需）：
   ```python
   from selenium.webdriver.chrome.options import Options
   
   options = Options()
   options.add_argument("--proxy-server=http://127.0.0.1:1080")
   driver = webdriver.Chrome(options=options)
   ```

### 3.2 证书验证失败

**问题描述：**
```
SSL certificate error
```

**解决方案：**
```python
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
driver = webdriver.Chrome(options=options)
```

### 3.3 连接超时

**解决方案：**
```python
# 设置页面加载超时
driver.set_page_load_timeout(30)

# 设置脚本超时
driver.set_script_timeout(30)

# 设置隐式等待
driver.implicitly_wait(10)
```

## 4. 国内网站自动化实战

### 4.1 百度搜索自动化

```python
def baidu_search(keyword):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    
    driver = webdriver.Chrome(service=Service("path/to/chromedriver"))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.baidu.com")
        
        # 输入搜索关键词
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "kw")))
        search_box.send_keys(keyword)
        
        # 点击搜索按钮
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "su")))
        search_button.click()
        
        # 获取搜索结果
        results = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".result h3")
        ))
        
        print(f"搜索 '{keyword}' 的前5个结果：")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    finally:
        driver.quit()

# 使用示例
baidu_search("Python 教程")
```

### 4.2 豆瓣电影搜索

```python
def douban_movie_search(movie_name):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    
    driver = webdriver.Chrome(service=Service("path/to/chromedriver"))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://movie.douban.com")
        
        # 定位搜索框
        search_box = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input#inp-query")
        ))
        search_box.send_keys(movie_name)
        
        # 点击搜索按钮
        search_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        search_button.click()
        
        # 获取搜索结果
        results = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".movie-item-title a")
        ))
        
        print(f"电影 '{movie_name}' 的搜索结果：")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    finally:
        driver.quit()

# 使用示例
douban_movie_search("流浪地球")
```

### 4.3 知乎问答搜索

```python
def zhihu_search(topic):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    
    driver = webdriver.Chrome(service=Service("path/to/chromedriver"))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.zhihu.com")
        
        # 定位搜索框
        search_box = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input.SearchBar-input")
        ))
        search_box.send_keys(topic)
        
        # 按回车搜索
        from selenium.webdriver.common.keys import Keys
        search_box.send_keys(Keys.ENTER)
        
        # 获取搜索结果
        results = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".QuestionItem-title a")
        ))
        
        print(f"知乎关于 '{topic}' 的问答：")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    finally:
        driver.quit()

# 使用示例
zhihu_search("Python 学习")
```

## 5. 性能优化（国内网络环境）

### 5.1 禁用图片加载

```python
options = Options()
options.add_argument("--blink-settings=imagesEnabled=false")
driver = webdriver.Chrome(options=options)
```

### 5.2 禁用 JavaScript（谨慎使用）

```python
options = Options()
options.add_argument("--disable-javascript")
driver = webdriver.Chrome(options=options)
```

### 5.3 禁用 CSS（谨慎使用）

```python
options = Options()
options.add_argument("--disable-stylesheets")
driver = webdriver.Chrome(options=options)
```

### 5.4 无头模式

```python
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
```

## 6. 企业网络环境配置

### 6.1 配置代理服务器

```python
from selenium.webdriver.chrome.options import Options

options = Options()

# HTTP 代理
options.add_argument("--proxy-server=http://proxy.company.com:8080")

# HTTPS 代理
options.add_argument("--proxy-server=https://proxy.company.com:8443")

# SOCKS 代理
options.add_argument("--proxy-server=socks5://proxy.company.com:1080")

# 无需代理的地址
options.add_argument("--proxy-bypass-list=*.company.com")

driver = webdriver.Chrome(options=options)
```

### 6.2 配置认证代理

```python
import base64

proxy_user = "username"
proxy_pass = "password"
proxy_auth = base64.b64encode(f"{proxy_user}:{proxy_pass}".encode()).decode()

options = Options()
options.add_argument(f"--proxy-server=http://proxy.company.com:8080")
options.add_argument(f"--proxy-auth={proxy_auth}")

driver = webdriver.Chrome(options=options)
```

## 7. 常见问题汇总

### Q1: ChromeDriver 下载慢

**解决方案：** 使用淘宝镜像下载

### Q2: pip 安装慢

**解决方案：** 配置国内 pip 源

### Q3: 无法访问国外网站

**解决方案：** 使用国内网站测试

### Q4: 企业网络无法访问外部网站

**解决方案：** 配置代理服务器

### Q5: Chrome 版本太新，找不到对应 ChromeDriver

**解决方案：** 检查淘宝镜像是否有更新

---

[上一章：常见问题](./05-faq.md)
