#!/usr/bin/env python3
"""
测试脚本：演示akshare函数库查看功能
"""

import akshare as ak

def test_akshare_function_discovery():
    """测试akshare函数发现功能"""
    
    print("="*60)
    print("测试akshare函数库查看功能")
    print("="*60)
    
    # 1. 显示所有akshare函数（前20个）
    print("\n1. 所有akshare函数（前20个）:")
    all_functions = [func for func in dir(ak) if not func.startswith('_')]
    print(f"总共有 {len(all_functions)} 个公开函数")
    for i, func in enumerate(all_functions[:20]):
        print(f"  {i+1:2d}. {func}")
    print("  ...")
    
    # 2. 过滤美股相关函数
    print("\n2. 美股相关函数（包含'us'和'stock'的函数）:")
    us_functions = [func for func in dir(ak) if 'us' in func.lower() and 'stock' in func.lower()]
    print(f"找到 {len(us_functions)} 个美股相关函数:")
    for i, func in enumerate(us_functions):
        print(f"  {i+1:2d}. {func}")
    
    # 3. 更宽泛的美股相关函数搜索
    print("\n3. 所有包含'us'的函数:")
    us_only_functions = [func for func in dir(ak) if 'us' in func.lower()]
    print(f"找到 {len(us_only_functions)} 个包含'us'的函数（前15个）:")
    for i, func in enumerate(us_only_functions[:15]):
        print(f"  {i+1:2d}. {func}")
    if len(us_only_functions) > 15:
        print("  ...")
    
    # 4. 所有包含'stock'的函数
    print("\n4. 所有包含'stock'的函数:")
    stock_functions = [func for func in dir(ak) if 'stock' in func.lower()]
    print(f"找到 {len(stock_functions)} 个包含'stock'的函数（前15个）:")
    for i, func in enumerate(stock_functions[:15]):
        print(f"  {i+1:2d}. {func}")
    if len(stock_functions) > 15:
        print("  ...")
    
    print("\n" + "="*60)
    print("函数发现测试完成")
    print("="*60)

if __name__ == "__main__":
    test_akshare_function_discovery()