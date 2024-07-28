import pandas as pd
import numpy as np
import statistics

def multiply_list(int_string):
    str_list = int_string.split()
    
    if not str_list:
        return 0
    
    int_list = [int(num) for num in str_list]
    
    product = 1
    
    for num in int_list:
        product *= num
    
    return product

def count_common_chars(words):
    word1, word2 = words.split()
    return len(set(word1) & set(word2))

def sum_divisible_by_k(N, K): 
    if K == 0: 
        return -1 
    return sum(i for i in range(1, N+1) if i % K == 0)

def highest_common_factor(num1, num2):
    factors_num1 = set()
    factors_num2 = set()
    
    for i in range(1, num1+1):
        if num1 % i == 0:
            factors_num1.add(i)
    
    for i in range(1, num2+1):
        if num2 % i == 0:
            factors_num2.add(i)
    
    common_factors = factors_num1.intersection(factors_num2)
    
    return max(common_factors)

def get_minimum(data):
    return min(data)

def rename_col(dataframe, old_col_name, new_col_name):
    dataframe.rename(columns={old_col_name: new_col_name}, inplace=True)
    return dataframe

def standard_deviation(series):
    return statistics.stdev(series)

def correlation_sum(numbers):
    try:
        data = np.array(numbers.split()).astype(float).reshape(3, 3)
        df = pd.DataFrame(data)
        corr_matrix = df.corr()
        sum_corr = np.sum(corr_matrix.values)
        return round(sum_corr, 1)
    except:
        return 0

  
