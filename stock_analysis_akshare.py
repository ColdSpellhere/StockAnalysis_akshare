"""
Copyright (c) 2025.11.6 Coldspell 
MIT License

股票数据提取和可视化分析 (使用akshare库)
使用akshare提取美股股票数据，pandas进行数据清洗和分析，使用Plotly绘制图表
支持交互式查询任意美股股票代码

作者: Coldspell
协助工具: Claude Sonnet 4.5
思路来源：作者在Coursera完成的IBM数据科学专业课程第四节实践作业（下附链接）

主要修改思路：
本次对原Jupyter notebook代码进行了全面重构，转换为独立的Python脚本，增强了交互性和错误处理能力。主要改动包括：
1. 使用akshare库替代yfinance获取美股数据，解决了yfinance在中国大陆网络环境下需要使用代理的问题。
2. 增加了对用户输入的股票代码的支持，用户可以通过命令行输入任意美股股票代码进行查询。
3. 分析时不再通过使用requests和BeautifulSoup手动抓取网页数据，而是直接使用akshare提供的接口获取历史股票数据，简化了数据获取流程。
4. 增强了错误处理机制，捕获并报告数据获取和处理中的异常，提升用户体验。

本项目GitHub链接：https://github.com/ColdSpellhere/StockAnalysis_akshare
思路参考Jupyter notebook链接：https://github.com/ColdSpellhere/IBM-DataScienceCourse/blob/main/Course5-Python_Project_for_DataScience/PracticeProject/Final%20Assignment.ipynb
Coursera课程链接：https://www.coursera.org/professional-certificates/ibm-data-science
Akshare文档链接：https://akshare.readthedocs.io/zh_CN/latest/index.html
"""
## ------------------------------------------------------------------------------------------------------------------------------
## 准备程序
# 导入必要运行库
import warnings
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 忽略警告
warnings.filterwarnings("ignore", category=FutureWarning)

# 尝试导入akshare
try:
    import akshare as ak
except ImportError:
    print("需要安装akshare库: pip install akshare")
    exit(1)
## ------------------------------------------------------------------------------------------------------------------------------
## 创建绘图函数，此处我们只绘制股票每日收盘价走势图，故接受参数为包含Date和Close列的DataFrame
def make_graph(stock_data, stock_name):
    """
    创建股票价格图表

    参数:
        stock_data: 包含Date和Close列的DataFrame
        stock_name: 股票名称
    """
    fig = go.Figure()
    
    # 添加股票价格轨迹
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data['Date']), 
            y=stock_data['Close'].astype("float"), 
            name="Stock Price",
            line=dict(color='#1f77b4', width=2)
        )
    )
    
    # 更新布局
    fig.update_layout(
        title=f"{stock_name} Historical Stock Price",
        xaxis_title="Date",
        yaxis_title="Price ($US)",
        height=600,
        hovermode='x unified',
        xaxis_rangeslider_visible=True,
        template='plotly_white'
    )
    
    fig.show()
## ------------------------------------------------------------------------------------------------------------------------------
## 创建获取股票数据函数，使用akshare获取美股历史数据，并进行必要的数据清洗，由画图部分可知需要Date和Close列，故下面函数需确保返回的数据包含这两列
def get_stock_data_akshare(symbol):
    """
    使用akshare获取美股历史数据
    
    参数:
        symbol: 股票代码（如'TSLA', 'GME'）
    
    返回:
        DataFrame: 包含历史股票数据
    """
    try:
        print(f"正在获取 {symbol} 的数据...")
        
        # 方法1: 尝试使用 stock_us_hist
        try:
            stock_data = ak.stock_us_hist(symbol=symbol)
            print(f"成功获取数据，列名: {stock_data.columns.tolist()}")
        except:
            # 方法2: 尝试使用 stock_us_daily (如果存在)，此处由于akshare接口可能会变动，故增加备用方法
            try:
                stock_data = ak.stock_us_daily(symbol=symbol)
                print(f"使用备用接口获取数据，列名: {stock_data.columns.tolist()}")
            except:
                print(f"提示: 请检查akshare是否支持该股票代码或尝试其他接口")
                print(f"可用的akshare美股相关函数:")
                us_functions = [func for func in dir(ak) if 'us' in func.lower() and 'stock' in func.lower()]
                print(us_functions[:10])
                return pd.DataFrame()
        
        if stock_data is None or stock_data.empty:
            print("返回的数据为空")
            return pd.DataFrame()
        
        # 打印原始数据的前几行用于调试，head返回数据表的前五行
        print(f"\n原始数据预览:")
        print(stock_data.head())
        
        # 重命名列 - 支持多种可能的列名
        column_mapping = {}
        
        # 日期列
        for date_col in ['日期', 'date', 'Date', '时间', 'time']:
            if date_col in stock_data.columns:
                column_mapping[date_col] = 'Date'
                break
        # 收盘价列
        for close_col in ['收盘', 'close', 'Close', '收盘价', 'close_price']:
            if close_col in stock_data.columns:
                column_mapping[close_col] = 'Close'
                break
        """
        此处使用中英文语境下的多种常见数据表名进行枚举查询，若后续更换数据源或接口时，仍能方便适配不同的列名格式
        """
        
        if column_mapping:
            stock_data.rename(columns=column_mapping, inplace=True)
            print(f"列名映射: {column_mapping}")
        
        # 检查必需的列是否存在
        if 'Date' not in stock_data.columns or 'Close' not in stock_data.columns:
            print(f"错误: 数据缺少必需的列")
            print(f"当前列名: {stock_data.columns.tolist()}")
            print(f"需要的列: Date, Close")
            return pd.DataFrame()
        
        # 确保Date列是datetime类型
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])
        stock_data.sort_values('Date', inplace=True)
        stock_data.reset_index(drop=True, inplace=True)
        
        print(f"成功处理 {len(stock_data)} 条记录")
        return stock_data
        
    except Exception as e:
        print(f"获取股票数据时出错: {e}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame()
## ------------------------------------------------------------------------------------------------------------------------------
## 创建分析函数，调用获取数据和绘图函数

def analyze_stock(symbol, stock_name=None):
    """
    分析指定股票的数据
    
    参数:
        symbol: 股票代码（如'TSLA', 'GME', 'AAPL'等）
        stock_name: 股票显示名称（可选，默认使用symbol）
    """
    if stock_name is None:
        stock_name = symbol
    
    print(f"\n正在分析 {stock_name} ({symbol})...")
    
    # 获取股票数据
    stock_data = get_stock_data_akshare(symbol)
    
    if not stock_data.empty and 'Date' in stock_data.columns:
        print(f"数据范围: {stock_data['Date'].min()} 至 {stock_data['Date'].max()}")
        print(f"总记录数: {len(stock_data)}")
        
        # 绘制图表
        make_graph(stock_data, stock_name)
        
        return stock_data
    else:
        print(f"未能获取 {stock_name} 股票数据")
        return None
## ------------------------------------------------------------------------------------------------------------------------------
## 主函数，交互式输入股票代码并调用分析函数
def main():
    """主函数"""
    print("="*60)
    print("Copyright (c) 2025.11.6 Coldspell")
    print("MIT License")
    print()
    print("股票数据提取和可视化分析 (使用akshare库)")
    print("使用akshare提取美股股票数据，pandas进行数据清洗和分析，使用Plotly绘制图表")
    print("支持交互式查询任意美股股票代码")
    print()
    print("作者: Coldspell")
    print("协助工具: Claude Sonnet 4.5")
    print("思路来源：作者在Coursera完成的IBM数据科学专业课程第四节实践作业（下附链接）")
    print()
    print("主要修改思路：")
    print("本次对原Jupyter notebook代码进行了全面重构，转换为独立的Python脚本，增强了交互性和错误处理能力。主要改动包括：")
    print("1. 使用akshare库替代yfinance获取美股数据，解决了yfinance在中国大陆网络环境下需要使用代理的问题。")
    print("2. 增加了对用户输入的股票代码的支持，用户可以通过命令行输入任意美股股票代码进行查询。")
    print("3. 分析时不再通过使用requests和BeautifulSoup手动抓取网页数据，而是直接使用akshare提供的接口获取历史股票数据，简化了数据获取流程。")
    print("4. 增强了错误处理机制，捕获并报告数据获取和处理中的异常，提升用户体验。")
    print()
    print("原Jupyter notebook链接：https://github.com/ColdSpellhere/IBM-DataScienceCourse/blob/main/Course5-Python_Project_for_DataScience/PracticeProject/Final%20Assignment.ipynb")
    print("Coursera课程链接：https://www.coursera.org/professional-certificates/ibm-data-science")
    print("Akshare文档链接：https://akshare.readthedocs.io/zh_CN/latest/index.html")
    print("="*60)
    
    try:
        # 交互式输入股票代码
        symbol = input("\n请输入股票代码（如TSLA, AAPL, GME等）: ").strip().upper()
        
        # 检查输入是否为空
        if not symbol:
            print("错误：股票代码不能为空")
            return
        
        # 分析股票
        analyze_stock(symbol=symbol, stock_name=symbol)
        
        print("\n" + "="*60)
        print("分析完成！")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
## ------------------------------------------------------------------------------------------------------------------------------
## 主程序入口

if __name__ == "__main__":
    main()

## ------------------------------------------------------------------------------------------------------------------------------
"""
感谢使用本脚本！
本项目GitHub链接：https://github.com/ColdSpellhere/StockAnalysis_akshare
Copyright (c) 2025.11.6 Coldspell
MIT License
"""
