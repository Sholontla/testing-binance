from binance_f import *
import pandas as pd
import numpy as np

def Parse_data(result, limit):
    """

    :param result:
    :param limit:
    :return:
    """
    data = []
    for i in range(limit):
        vela = []
        vela.append(result[i].openTime)
        vela.append(result[i].open)
        vela.append(result[i].high)
        vela.append(result[i].low)
        vela.append(result[i].close)
        vela.append(result[i].volume)
        data.append(vela)
    df = pd.DataFrame(data)
    col_names = ['time', 'open', 'high', 'low', 'close', 'volume']
    df.columns = col_names
    for col in col_names:
        df[col] = df[col].astype(float)
    df['start'] = pd.to_datetime(df['time'] * 1000000)

    return df


def Get_Capital(result, ref):
    
    for i in range(len(result.assets)):
        asset_1 = "------assests-----: ", result.assets[i].asset
        if result.assets[i].asset == ref:
            asset_2 = "-----------: ", result.assets[i].marginBalance
            return result.assets[i].marginBalance, asset_1, asset_2



def Get_Exchange_filters(result, S):
    for i in range(len(result.symbols)):
        if result.symbols[i].symbol == S:
            minQty = float(result.symbols[i].filters[2].get('minQty'))
            stepSize = float(result.symbols[i].filters[2].get('stepSize'))
            maxQty = float(result.symbols[i].filters[2].get('maxQty'))
            return minQty, stepSize, maxQty

def Calculate_max_Decimal_Qty(stepSize):
    max_decimal_quantity=0
    a = 10
    while stepSize*a<1:
      a = a*10**max_decimal_quantity
      max_decimal_quantity += 1
    return max_decimal_quantity



def Crossover(MF, MS):
    if (MF[0] < MS[0] and MF[1] >= MS[1]):
        return True
    else:
        return False

def Calculate_Qty(price, money, minQty, maxQty, maxDeciamlQty):

    Q = money / price
    if (Q < minQty or Q > maxQty):
        return False
    Q = np.round(Q, maxDeciamlQty)
    return Q
