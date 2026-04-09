#!/usr/bin/env python3
"""
收益王策略 - 主运行脚本
AI增强的收益率优先策略，专为OKX交易大赛设计
"""

import sys
import json
import time
from datetime import datetime
from okx_client import OKXClient

def load_config():
    """加载配置文件"""
    try:
        # 这里可以加载配置文件
        config = {
            'api_key': '',
            'secret_key': '',
            'passphrase': '',
            'demo': False,
            'trading_pairs': ['BTC-USDT-SWAP', 'ETH-USDT-SWAP', 'SOL-USDT-SWAP'],
            'timeframe': '1H',
            'candle_limit': 100
        }
        return config
    except Exception as e:
        print(f"加载配置文件失败: {e}")
        sys.exit(1)

def initialize_client(config):
    """初始化OKX客户端"""
    try:
        client = OKXClient(
            api_key=config['api_key'],
            secret_key=config['secret_key'],
            passphrase=config['passphrase'],
            demo=config['demo']
        )
        
        if not client.is_authenticated():
            print("⚠️ 未配置API密钥，将使用公开API功能")
            print("如需完整交易功能，请在配置文件中填写API密钥")
        
        return client
    except Exception as e:
        print(f"初始化客户端失败: {e}")
        sys.exit(1)

def collect_market_data(client, config):
    """收集市场数据"""
    print(f"\n📊 收集市场数据 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    market_data = {}
    
    for symbol in config['trading_pairs']:
        try:
            # 获取价格
            ticker = client.get_ticker(symbol)
            if ticker:
                print(f"✅ {symbol} 价格: {ticker.get('last')}")
            else:
                print(f"⚠️ {symbol} 价格获取失败")
                continue
            
            # 获取K线数据
            candles = client.get_candles(symbol, config['timeframe'], config['candle_limit'])
            if candles:
                print(f"✅ {symbol} K线: 获取到 {len(candles)} 根")
            else:
                print(f"⚠️ {symbol} K线获取失败")
                continue
            
            market_data[symbol] = {
                'ticker': ticker,
                'candles': candles
            }
            
        except Exception as e:
            print(f"❌ {symbol} 数据收集失败: {e}")
    
    return market_data

def calculate_indicators(market_data):
    """计算技术指标"""
    print(f"\n🧠 计算技术指标")
    print("=" * 50)
    
    for symbol, data in market_data.items():
        try:
            candles = data['candles']
            
            # 计算ATR
            atr = client.calculate_atr(candles, period=14)
            if atr > 0:
                print(f"✅ {symbol} ATR: {atr}")
            else:
                print(f"⚠️ {symbol} ATR计算失败")
            
            # 这里可以添加更多技术指标计算
            # EMA, RSI, MACD 等
            
        except Exception as e:
            print(f"❌ {symbol} 指标计算失败: {e}")

def execute_strategy(market_data):
    """执行交易策略"""
    print(f"\n🎯 执行交易策略")
    print("=" * 50)
    
    # 这里实现完整的交易策略逻辑
    # 多因子评分、市场过滤、标的筛选、动态仓位等
    
    print("⚠️ 策略功能需要配置API密钥后才能完整运行")
    print("当前仅演示数据收集和指标计算功能")

def run_strategy():
    """运行策略主程序"""
    print("🚀 收益王策略启动")
    print("=" * 50)
    
    # 加载配置
    config = load_config()
    
    # 初始化客户端
    client = initialize_client(config)
    
    # 收集市场数据
    market_data = collect_market_data(client, config)
    
    if not market_data:
        print("❌ 未获取到市场数据，程序退出")
        sys.exit(1)
    
    # 计算技术指标
    calculate_indicators(market_data)
    
    # 执行策略
    execute_strategy(market_data)
    
    print("\n✅ 策略执行完成")
    print("=" * 50)

if __name__ == "__main__":
    try:
        run_strategy()
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断程序")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 程序执行出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)