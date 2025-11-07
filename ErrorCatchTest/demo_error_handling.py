#!/usr/bin/env python3
"""
演示错误处理逻辑的测试脚本
"""

import pandas as pd
import akshare as ak

def simulate_error_handling(symbol):
    """模拟股票数据获取失败时的错误处理逻辑"""
    
    print(f"正在获取 {symbol} 的数据...")
    
    try:
        # 模拟第一个方法失败
        try:
            # 这里我们故意让它失败
            raise Exception("模拟 stock_us_hist 失败")
            stock_data = ak.stock_us_hist(symbol=symbol)
            print(f"成功获取数据，列名: {stock_data.columns.tolist()}")
        except:
            # 模拟第二个方法也失败
            try:
                # 这里我们也故意让它失败
                raise Exception("模拟 stock_us_daily 失败")
                stock_data = ak.stock_us_daily(symbol=symbol)
                print(f"使用备用接口获取数据，列名: {stock_data.columns.tolist()}")
            except:
                # 这里就是您代码中第103行会执行的部分
                print(f"提示: 请检查akshare是否支持该股票代码或尝试其他接口")
                print(f"可用的akshare美股相关函数:")
                us_functions = [func for func in dir(ak) if 'us' in func.lower() and 'stock' in func.lower()]
                print(us_functions[:10])  # 只显示前10个
                return pd.DataFrame()
    
    except Exception as e:
        print(f"获取股票数据时出错: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    print("="*60)
    print("演示错误处理逻辑 - 当股票数据获取失败时")
    print("="*60)
    
    # 模拟一个可能不存在或获取失败的股票代码
    test_symbol = "INVALID_STOCK"
    result = simulate_error_handling(test_symbol)
    
    print(f"\n返回结果: {'空DataFrame' if result.empty else '有数据'}")
    print("="*60)