# ChromeDriver Learning

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/ChromeDriver-learning.svg)](https://github.com/yourusername/ChromeDriver-learning/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/yourusername/ChromeDriver-learning.svg)](https://github.com/yourusername/ChromeDriver-learning/issues)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

一个系统化的 ChromeDriver 学习仓库，从安装到原理，再到实践，全面掌握浏览器自动化技术。

**🌏 国内用户友好**：提供国内镜像下载地址、国内测试网站示例、网络问题解决方案

## 📚 目录结构

```
ChromeDriver-learning/
├── README.md                    # 项目说明
├── LICENSE                      # 许可证
├── CONTRIBUTING.md              # 贡献指南
├── .gitignore                   # Git 忽略配置
├── requirements.txt             # Python 依赖
├── config.py                    # 配置文件
├── docs/                        # 学习文档
│   ├── 01-installation.md       # 安装指南（国内镜像）
│   ├── 02-principle.md          # 原理介绍
│   ├── 03-api-reference.md      # API 参考
│   ├── 04-practice.md           # 实践指南
│   ├── 05-faq.md                # 常见问题
│   └── 06-china-tips.md         # 国内用户专属技巧
├── examples/                    # 示例代码
│   ├── 01_basic_usage.py        # 基础用法
│   ├── 02_element_locator.py    # 元素定位
│   ├── 03_navigation.py         # 页面导航
│   ├── 04_forms.py              # 表单操作
│   ├── 05_wait_strategies.py    # 等待策略
│   └── 06_advanced_features.py  # 高级功能
├── tutorials/                   # 教程目录
│   ├── tutorial_01.md           # 教程1：入门（国内版）
│   └── tutorial_02.md           # 教程2：实战（国内版）
└── utils/                       # 工具函数
    └── __init__.py
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Chrome 浏览器
- ChromeDriver（与 Chrome 版本匹配）

### 安装步骤（国内用户推荐）

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/ChromeDriver-learning.git
   cd ChromeDriver-learning
   ```

2. **创建虚拟环境**
   ```bash
   # 使用 Conda（推荐）
   conda create -n chromedriver-env python=3.10 -y
   conda activate chromedriver-env
   
   # 或使用 venv
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **配置国内 pip 源（避免下载慢）**
   ```bash
   pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   ```

4. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

5. **配置 ChromeDriver（国内镜像）**
   - ✅ **推荐下载地址**：https://npm.taobao.org/mirrors/chromedriver/
   - 修改 `config.py` 中的路径：
     ```python
     CHROME_DRIVER_PATH = "D:/path/to/chromedriver.exe"
     ```

6. **运行示例**
   ```bash
   python examples/01_basic_usage.py
   ```

## 📖 学习路径

| 阶段 | 章节 | 内容 |
|------|------|------|
| 入门 | [安装指南](docs/01-installation.md) | 环境配置、国内镜像 |
| 原理 | [原理介绍](docs/02-principle.md) | WebDriver 协议、ChromeDriver 架构 |
| API | [API 参考](docs/03-api-reference.md) | 浏览器控制、元素定位、等待机制 |
| 实践 | [实践指南](docs/04-practice.md) | 表单处理、高级技巧、性能优化 |
| 答疑 | [常见问题](docs/05-faq.md) | 问题排查、调试技巧 |
| 国内 | [国内技巧](docs/06-china-tips.md) | 国内镜像、网络配置、实战案例 |

## 🎯 示例代码

### 基础示例（国内网站）

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建浏览器实例
driver = webdriver.Chrome(service=Service("path/to/chromedriver"))

# 访问国内网站
driver.get("https://www.baidu.com")

# 打印页面标题
print(driver.title)

# 关闭浏览器
driver.quit()
```

### 元素定位

```python
from selenium.webdriver.common.by import By

# 通过 ID 定位
element = driver.find_element(By.ID, "kw")

# 通过 CSS 选择器定位
element = driver.find_element(By.CSS_SELECTOR, "input#kw")

# 通过 XPath 定位
element = driver.find_element(By.XPATH, "//input[@id='kw']")
```

### 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "su")))
element.click()
```

## 🌏 国内用户专属

### 常用国内测试网站

| 网站 | 网址 | 用途 |
|------|------|------|
| 百度 | https://www.baidu.com | 搜索测试 |
| 淘宝 | https://www.taobao.com | 电商测试 |
| 京东 | https://www.jd.com | 电商测试 |
| 知乎 | https://www.zhihu.com | 社交测试 |
| 豆瓣 | https://www.douban.com | 社交测试 |

### 国内镜像资源

| 资源 | 地址 |
|------|------|
| ChromeDriver | https://npm.taobao.org/mirrors/chromedriver/ |
| pip 源 | https://pypi.tuna.tsinghua.edu.cn/simple |
| Conda 源 | https://mirrors.tuna.tsinghua.edu.cn/anaconda/ |

## 🤝 贡献

欢迎贡献代码！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献流程。

## 📄 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE)。

## 🙏 致谢

- [Selenium](https://www.selenium.dev/) - 自动化测试框架
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) - Chrome 浏览器驱动

---

⭐ 如果这个项目对你有帮助，请给个 Star！
