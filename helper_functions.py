def get_uniswap_data(pool_id, number_of_days,url):
    import requests
    import json
    import csv


    url = url
    query = f"""
    {{
        poolDayDatas(where: {{ pool: "{pool_id}" }}, first: {number_of_days}, orderBy: date, orderDirection: desc) {{
            date
            tick
            sqrtPrice
            liquidity
            volumeUSD
            volumeToken0
            volumeToken1
            tvlUSD
            feesUSD
            close
            open
            low
            high
        }}
    }}
    """
    response = requests.post(url, json={'query': query})
    data = response.json()

    return data['data']['poolDayDatas']

def save_data_to_csv(data, file_path):
    keys = data[0].keys()
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def preprocess_data(data_df):
    import pandas as pd
    data_df['volumeUSD'] = data_df['volumeUSD'].astype(float)
    data_df['volumeToken0'] = data_df['volumeToken0'].astype(float)
    data_df['volumeToken1'] = data_df['volumeToken1'].astype(float)
    data_df['sqrtPrice'] = (data_df['sqrtPrice'].astype(float))
    data_df['liquidity'] = data_df['liquidity'].astype(float)
    data_df['tvlUSD'] = data_df['tvlUSD'].astype(float)
    data_df['feesUSD'] = data_df['feesUSD'].astype(float)
    data_df['close'] = data_df['close'].astype(float)
    data_df['open'] = data_df['open'].astype(float)
    data_df['low'] = data_df['low'].astype(float)
    data_df['high'] = data_df['high'].astype(float)
    
      # Convert date from UNIX timestamp to datetime format
    data_df['date'] = pd.to_datetime(data_df['date'], unit='s')
    # 7 days Rolling averages
    data_df['feesUSD'] = data_df['feesUSD'].rolling(window=7, min_periods=1).mean()

    data_df['date'] = pd.to_datetime(data_df['date'], unit='s')
  
# Check for missing data in the control group
    missing_values = data_df.isnull().sum()
    missing_control = missing_values[missing_values > 0]

    return data_df

def explore_data(df):
    #Raw data analysis
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sklearn
    from sklearn.preprocessing import StandardScaler
    import numpy as np
    from scipy.stats import zscore

    df.plot(x='date', y='sqrtPrice')

    df.plot(x='date', y='feesUSD')
    df.plot(x='date', y='liquidity')

    ax = df.plot(x='date', y='liquidity', color='blue', label='liquidity')
    df.plot(x='date', y='sqrtPrice', color='red', secondary_y=True, ax=ax, label='sqrtPrice')

    ax.set_ylabel('liquidity')
    ax.right_ax.set_ylabel('sqrtPrice')
    plt.title('liquidity and sqrtPrice Over Time')
    plt.show()

    ax = df.plot(x='date', y='liquidity', color='blue', label='liquidity')
    df.plot(x='date', y='feesUSD', color='red', secondary_y=True, ax=ax, label='Fees')

    ax.set_ylabel('liquidity')
    ax.right_ax.set_ylabel('Fees')
    plt.title('liquidity and Fees Over Time')
    plt.show()

    ax = df.plot(x='date', y='volumeToken0', color='blue', label='volumeToken0')
    df.plot(x='date', y='volumeToken1', color='red', secondary_y=True, ax=ax, label='volumeToken1')

    ax.set_ylabel('volumeToken0')
    ax.right_ax.set_ylabel('volumeToken1')
    plt.title('liquidity and Fees Over Time')
    plt.show()

    ax = df.plot(x='date', y='sqrtPrice', color='blue', label='sqrtPrice')
    df.plot(x='date', y='sqrtPrice', color='red', secondary_y=True, ax=ax, label='sqrtPrice')
    ax.set_ylabel('sqrtPrice')
    ax.right_ax.set_ylabel('sqrtPrice')
    plt.title('liquidity and Fees Over Time')
    plt.show()

    #EDA
    plt.hist(df['volumeUSD'])
    plt.show()
    sns.boxplot(x=df['volumeUSD'])
    plt.show()
    plt.scatter(x=df['date'],y=df['volumeUSD'])
    plt.show()
    sns.countplot(df['volumeUSD'])
    plt.show()
    sns.heatmap(df.corr())
    plt.show()
    corr_matrix=df.corr()
    sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')

    #zscore
    df['zscore']=zscore(df['volumeUSD'])
    outliers=df[(df['zscore']>3) | (df['zscore']<-3)]
    print(outliers)

    #transformations
    df['log_transformed']=np.log(df['volumeUSD'])

    #standardization
    scaler = StandardScaler()
    df['standardized_volume'] = scaler.fit_transform(df['volumeUSD'].values.reshape(-1, 1))

    return True

# Function to calculate the market share of a pool in terms of TVL
def calculate_market_share(treatment_data, control_data, start_date, end_date):
    treatment_tvl = treatment_data[(treatment_data['date'] >= start_date) & (treatment_data['date'] <= end_date)]['tvlUSD'].sum()
    control_tvl = control_data[(control_data['date'] >= start_date) & (control_data['date'] <= end_date)]['tvlUSD'].sum()
    total_tvl = treatment_tvl + control_tvl
    treatment_market_share = treatment_tvl / total_tvl
    control_market_share = control_tvl / total_tvl
    return treatment_market_share, control_market_share

# Function to calculate the market share of a pool in terms of feesUSD
def calculate_fees_market_share(treatment_data, control_data, start_date, end_date):
    treatment_fees = treatment_data[(treatment_data['date'] >= start_date) & (treatment_data['date'] <= end_date)]['feesUSD'].sum()
    control_fees = control_data[(control_data['date'] >= start_date) & (control_data['date'] <= end_date)]['feesUSD'].sum()
    total_fees = treatment_fees + control_fees
    treatment_fees_market_share = treatment_fees / total_fees
    control_fees_market_share = control_fees / total_fees
    return treatment_fees_market_share, control_fees_market_share