# ChromeDriver 安装指南（国内用户版）

## 1. 环境要求

### 1.1 安装 Python

确保已安装 Python 3.8+：

```bash
python --version
```

**国内下载地址：**
- 官方镜像：https://www.python.org/downloads/
- 国内镜像：https://mirrors.tuna.tsinghua.edu.cn/python/

### 1.2 安装 Chrome 浏览器

确保已安装 Google Chrome 浏览器：

**国内下载地址：**
- 官网：https://www.google.com/chrome/
- 国内镜像：https://www.google.cn/chrome/

**查看 Chrome 版本：**
- 打开 Chrome → 设置 → 关于 Chrome

### 1.3 下载 ChromeDriver

**⚠️ 重要：ChromeDriver 版本必须与 Chrome 版本完全匹配！**

**推荐下载地址（国内用户）：**

| 资源 | 地址 | 说明 |
|------|------|------|
| 官方地址 | https://sites.google.com/chromium.org/driver/ | 需要科学上网 |
| 淘宝镜像 | https://npm.taobao.org/mirrors/chromedriver/ | ✅ 推荐国内用户使用 |
| 腾讯镜像 | https://mirrors.cloud.tencent.com/chromedriver/ | 备用 |
| 华为镜像 | https://mirrors.huaweicloud.com/chromedriver/ | 备用 |

**版本对应关系示例：**
| Chrome 版本 | ChromeDriver 版本 |
|------------|------------------|
| 148.0.7778.x | 148.0.7778.10 |
| 124.x | 124.0.6367.60 |
| 123.x | 123.0.6312.105 |

**快速匹配方法：**
1. 查看 Chrome 版本（如：148.0.7778.97）
2. 在淘宝镜像中找到最接近的版本目录（如：148.0.7778.10/）
3. 下载对应系统的压缩包

## 2. 配置步骤

### 2.1 解压 ChromeDriver

将下载的压缩包解压到指定目录，例如：
- Windows: `D:\Tools\chromedriver.exe`
- macOS/Linux: `/usr/local/bin/chromedriver`

### 2.2 添加到系统 PATH（可选）

**Windows：**
1. 右键「此电脑」→ 属性 → 高级系统设置 → 环境变量
2. 在系统变量 PATH 中添加 ChromeDriver 所在目录

**macOS/Linux：**
```bash
echo 'export PATH="$PATH:/path/to/chromedriver"' >> ~/.bashrc
source ~/.bashrc
```

### 2.3 验证安装

```bash
chromedriver --version
```

## 3. 使用虚拟环境（推荐）

### 3.1 使用 Conda（推荐国内用户）

```bash
# 创建环境
conda create -n chromedriver-env python=3.10 -y

# 激活环境
conda activate chromedriver-env

# 配置国内 pip 源（避免下载慢）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装依赖
pip install selenium webdriver-manager
```

### 3.2 使用 venv

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 配置国内 pip 源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install selenium webdriver-manager
```

### 3.3 Conda 国内镜像配置

编辑 `~/.condarc` 文件（Windows：`C:\Users\你的用户名\.condarc`）：

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
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

## 4. 测试安装

创建测试文件 `test_chromedriver.py`：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 使用国内网站测试
driver = webdriver.Chrome(service=Service("D:/path/to/chromedriver.exe"))
driver.get("https://www.baidu.com")
print("页面标题:", driver.title)
driver.quit()
```

运行测试：
```bash
python test_chromedriver.py
```

**预期输出：**
```
页面标题: 百度一下，你就知道
```

## 5. 常见问题（国内用户专属）

### 5.1 无法访问 ChromeDriver 官方下载地址

**解决方案：** 使用淘宝镜像下载：https://npm.taobao.org/mirrors/chromedriver/

### 5.2 pip 下载速度慢

**解决方案：** 配置国内源：
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5.3 无法访问 Google 网站

**解决方案：** 使用国内网站进行测试，如百度、淘宝、京东等。

### 5.4 网络连接超时

**解决方案：**
1. 检查网络连接
2. 使用国内网站
3. 配置代理（如需）：
   ```python
   from selenium.webdriver.chrome.options import Options
   
   options = Options()
   options.add_argument("--proxy-server=http://代理地址:端口")
   driver = webdriver.Chrome(options=options)
   ```

### 5.5 ChromeDriver 版本不匹配

**错误信息：**
```
session not created: This version of ChromeDriver only supports Chrome version XX
```

**解决方案：** 在淘宝镜像中下载与 Chrome 版本匹配的 ChromeDriver。

---

[下一章：ChromeDriver 原理介绍](./02-principle.md)
