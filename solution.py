import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 285100540 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  p = 0.05    
  count = np.array([x_success, x_cnt])
  nobs = np.array([y_success, y_cnt])
  stat, pval = proportions_ztest(count, nobs, alternative='smaller')
  if pval >= p:
    return False
  else:
    return True
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

