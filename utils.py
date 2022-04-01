import pandas as pd

def transform_dict_to_pandas(dict):
    df = pd.DataFrame(dict, index=[1])
    return df