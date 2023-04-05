import pandas as pd
import numpy as np


chat_id = 402739329 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 4
    return np.exp(- np.sqrt( x.mean() / t)) # Ваш ответ
