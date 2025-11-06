# 股票数据提取和可视化分析 | Stock Data Analysis Tool

[English](#english) | [中文](#中文)

---

## 中文

### 项目简介

这是一个基于akshare库的美股数据分析工具，支持交互式查询任意美股股票代码，并生成可视化图表。该项目从IBM数据科学专业课程的Jupyter notebook重构而来，转换为独立的Python脚本，并增强了交互性和错误处理能力。

### 主要特性

- 🚀 **简单易用**: 交互式命令行界面，输入股票代码即可分析
- 📊 **数据可视化**: 使用Plotly生成交互式股票价格走势图
- 🔧 **智能适配**: 自动处理不同数据源的列名格式
- 🌐 **网络友好**: 使用akshare库，解决了yfinance在中国大陆的网络问题
- ⚡ **错误处理**: 完善的异常处理机制，提升用户体验
- 📈 **实时数据**: 获取最新的美股历史数据

### 技术栈

- **数据获取**: akshare
- **数据处理**: pandas
- **数据可视化**: Plotly
- **开发语言**: Python 3.x

### 安装依赖

```bash
pip install akshare pandas plotly
```

### 使用方法

1. 克隆仓库:
```bash
git clone https://github.com/ColdSpellhere/StockAnalysis_akshare.git
cd StockAnalysis_akshare
```

2. 运行程序:
```bash
python stock_analysis_akshare.py
```

3. 输入股票代码（如TSLA, AAPL, GME等）并回车

### 支持的股票代码

支持所有在akshare库中可查询的美股股票代码，包括但不限于：
- TSLA (特斯拉)
- AAPL (苹果)
- GME (GameStop)
- MSFT (微软)
- GOOGL (谷歌)
- AMZN (亚马逊)

### 项目起源

本项目基于作者在Coursera完成的IBM数据科学专业课程第四节实践作业进行重构：

**主要改进**:
1. 使用akshare库替代yfinance，解决网络访问问题
2. 增加交互式用户输入支持
3. 简化数据获取流程，移除手动网页抓取
4. 增强错误处理和用户体验

### 相关链接

- [原始Jupyter Notebook](https://github.com/ColdSpellhere/IBM-DataScienceCourse/blob/main/Course5-Python_Project_for_DataScience/PracticeProject/Final%20Assignment.ipynb)
- [IBM数据科学专业课程](https://www.coursera.org/professional-certificates/ibm-data-science)
- [Akshare文档](https://akshare.readthedocs.io/zh_CN/latest/index.html)

### 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

### 作者

- **Coldspell** - *项目作者*
- **协助工具**: Claude Sonnet 4.5

---

## English

### Project Description

This is a US stock data analysis tool based on the akshare library, supporting interactive querying of any US stock symbol and generating visualization charts. This project is refactored from a Jupyter notebook from IBM's Data Science Professional Certificate course, converted to a standalone Python script with enhanced interactivity and error handling.

### Key Features

- 🚀 **Easy to Use**: Interactive command-line interface, analyze stocks by simply entering symbols
- 📊 **Data Visualization**: Generate interactive stock price charts using Plotly
- 🔧 **Smart Adaptation**: Automatically handles different column name formats from various data sources
- 🌐 **Network Friendly**: Uses akshare library, solving yfinance network issues in mainland China
- ⚡ **Error Handling**: Comprehensive exception handling for better user experience
- 📈 **Real-time Data**: Access to latest US stock historical data

### Tech Stack

- **Data Retrieval**: akshare
- **Data Processing**: pandas
- **Data Visualization**: Plotly
- **Programming Language**: Python 3.x

### Installation

```bash
pip install akshare pandas plotly
```

### Usage

1. Clone the repository:
```bash
git clone https://github.com/ColdSpellhere/StockAnalysis_akshare.git
cd StockAnalysis_akshare
```

2. Run the program:
```bash
python stock_analysis_akshare.py
```

3. Enter a stock symbol (e.g., TSLA, AAPL, GME) and press Enter

### Supported Stock Symbols

Supports all US stock symbols available in the akshare library, including but not limited to:
- TSLA (Tesla)
- AAPL (Apple)
- GME (GameStop)
- MSFT (Microsoft)
- GOOGL (Google)
- AMZN (Amazon)

### Project Origin

This project is refactored from the author's practice assignment in the IBM Data Science Professional Certificate Course 4 on Coursera:

**Key Improvements**:
1. Replaced yfinance with akshare library to solve network access issues
2. Added interactive user input support
3. Simplified data retrieval process, removed manual web scraping
4. Enhanced error handling and user experience

### Related Links

- [Original Jupyter Notebook](https://github.com/ColdSpellhere/IBM-DataScienceCourse/blob/main/Course5-Python_Project_for_DataScience/PracticeProject/Final%20Assignment.ipynb)
- [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science)
- [Akshare Documentation](https://akshare.readthedocs.io/zh_CN/latest/index.html)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Author

- **Coldspell** - *Project Author*
- **Assistant Tool**: Claude Sonnet 4.5

---

### Screenshot

*Interactive stock price chart generated by the tool*

![Stock Analysis Demo](https://via.placeholder.com/800x400?text=Interactive+Stock+Chart+Demo)

---

**Happy Analyzing! 📈**