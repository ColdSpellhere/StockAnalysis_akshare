#!/usr/bin/env python3
"""
真实情况测试：尝试获取一个可能不存在的股票代码
"""

import pandas as pd
import akshare as ak

def test_real_error_case(symbol):
    """测试真实的错误情况"""
    
    print(f"正在获取 {symbol} 的数据...")
    
    try:
        # 方法1: 尝试使用 stock_us_hist
        try:
            stock_data = ak.stock_us_hist(symbol=symbol)
            print(f"成功获取数据，列名: {stock_data.columns.tolist()}")
            return stock_data
        except Exception as e1:
            print(f"stock_us_hist 失败: {e1}")
            # 方法2: 尝试使用 stock_us_daily (如果存在)
            try:
                stock_data = ak.stock_us_daily(symbol=symbol)
                print(f"使用备用接口获取数据，列名: {stock_data.columns.tolist()}")
                return stock_data
            except Exception as e2:
                print(f"stock_us_daily 也失败: {e2}")
                print(f"提示: 请检查akshare是否支持该股票代码或尝试其他接口")
                print(f"可用的akshare美股相关函数:")
                us_functions = [func for func in dir(ak) if 'us' in func.lower() and 'stock' in func.lower()]
                print(us_functions[:10])
                return pd.DataFrame()
    
    except Exception as e:
        print(f"获取股票数据时出错: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    print("="*60)
    print("真实错误情况测试")
    print("="*60)
    
    # 测试一个不存在的股票代码
    print("\n测试1: 不存在的股票代码")
    result1 = test_real_error_case("NONEXISTENT123")
    print(f"结果: {'空DataFrame' if result1.empty else '有数据'}")
    
    print("\n" + "-"*60)
    
    # 测试一个真实的股票代码（应该成功）
    print("\n测试2: 真实的股票代码 (AAPL)")
    result2 = test_real_error_case("AAPL")
    print(f"结果: {'空DataFrame' if result2.empty else f'有数据 - {len(result2)} 行'}")
    if not result2.empty:
        print(f"数据列: {result2.columns.tolist()}")
        print(f"数据样例:\n{result2.head(2)}")
    
    print("\n" + "="*60)