import pandas as pd
import numpy as np

chat_id = 42791670 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    ln_checks = np.log(x)
    alpha_hat = np.exp(np.mean(ln_checks))
    return alpha_hat
