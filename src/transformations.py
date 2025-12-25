def transform_data(df):
    return df.filter(df.salary >= 10000)