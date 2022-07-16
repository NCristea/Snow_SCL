import pandas as pd
from datetime import datetime

def calc_water_year(date):
    date = pd.to_datetime(date)
    if 10 <= date.month <= 12:
        water_year = date.year + 1
        return water_year
    else:
        return date.year

def calc_water_year_apply(df):
    df['water_year'] = df.datetime.apply(lambda row: calc_water_year(row))

def snotel_data(path_snotel):
    snotel_obs = pd.read_csv(path_snotel, sep='\s+', header=None)
    snotel_obs.columns = ['year', 'month', 'day', 'daily_P_in', 'Tmax_F', 'Tmin_F', 'Tmean_F', 'SWE_in']
    snotel_obs['Tmean_C'] = (snotel_obs['Tmean_F'] - 32) * (5 / 9)
    snotel_obs = snotel_obs.set_index(pd.DatetimeIndex(pd.to_datetime(snotel_obs[['year', 'month', 'day']])))
    snotel_obs['SWE_m'] = snotel_obs['SWE_in'] * 0.0254
    snotel_obs['datetime'] = snotel_obs.index
    calc_water_year_apply(snotel_obs)
    return snotel_obs

def spu_snotel_data(path_snotel_spu):
    snotel_obs = pd.read_csv(path_snotel, sep='\s+', header=None)
    snotel_obs.columns = ['year', 'month', 'day', 'daily_P_in', 'Tmax_F', 'Tmin_F', 'Tmean_F', 'SWE_in']
    #snotel_obs['Tmean_C'] = (snotel_obs['Tmean_F'] - 32) * (5 / 9)
    snotel_obs = snotel_obs.set_index(pd.DatetimeIndex(pd.to_datetime(snotel_obs[['year', 'month', 'day']])))
    #snotel_obs['SWE_m'] = snotel_obs['SWE_in'] * 0.0254
    #snotel_obs['datetime'] = snotel_obs.index
    #calc_water_year_apply(snotel_obs)
    return snotel_obs
#%%
