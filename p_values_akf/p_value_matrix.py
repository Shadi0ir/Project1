def p_value_matrix(feature):    
    #Import dependencies
    import pandas as pd
    from scipy import stats
    import matplotlib.pyplot as plt
    import numpy as np

    #Set list of countries
    countries = ['Global', 'US', 'India', 'Brazil', 'UK', 'Malaysia', 'Japan',
    'Australia', 'France', 'South Africa', 'Taiwan', 'Hong Kong']

    # Generate dictionary that holds each pd as country:pd and array of 0's to hold t test values
    pd_dict = {}
    for country in countries:
        path = f'CSV_Output/{country}_top_50_songs.csv'
        pd_dict.update({country : pd.read_csv(path)})

    df = pd.DataFrame(np.zeros(shape=(12,12)), columns = countries, index = countries)

    # Loop to calculate p values from 2 tailed t tests for all possible country combinations
    for i in range(0,12):
        for j in range(0,12):
            df.iloc[i, j] = stats.ttest_ind(pd_dict[countries[i]][feature], pd_dict[countries[j]][feature])[1]
            print(f'Calculating cell ({i}, {j})')

    # Format df to highlight interesting comparisons 
    df = df.style.apply(lambda x: ["background: red" if v < 0.05 else "" for v in x])
    
    return df
