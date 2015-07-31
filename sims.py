# coding: utf-8
import numpy as np

def gen_sim_price(num_stocks=10, num_days=90):
    """주식 종목 가격 시뮬레이션. 
    지정된 종목 개수에 대한 지정된 일수만큼의 모의 가격 생성"""
    prices = np.random.randint(5,1000, size=num_stocks)
    changes = 1+np.random.uniform(low=-0.3, high=0.3, 
                                  size=(num_days, num_stocks))
    prices =  prices * changes.cumprod(0)

    return prices