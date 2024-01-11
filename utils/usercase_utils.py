import pandas as pd

# 获取测试用例
def get_usercases(path):
    dataset = pd.read_excel(path)
    return dataset.values