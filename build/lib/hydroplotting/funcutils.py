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

import numpy as np

def calc_water_year_da(da):
    return da.dt.year + (da.dt.month >= 10).astype(int)

def nse(sim, obs):
    num = np.sum((obs - sim) ** 2)
    den = np.sum((obs - np.mean(obs)) ** 2)
    return 1 - (num /den)


def kge(simulation_s, evaluation):
    sim_mean = np.mean(simulation_s, axis=0, dtype=np.float64)
    obs_mean = np.mean(evaluation, dtype=np.float64)
    r = np.sum((simulation_s - sim_mean) * (evaluation - obs_mean), axis=0, dtype=np.float64) / \
        np.sqrt(np.sum((simulation_s - sim_mean) ** 2, axis=0, dtype=np.float64) *
                np.sum((evaluation - obs_mean) ** 2, dtype=np.float64))
    alpha = np.std(simulation_s, axis=0) / np.std(evaluation, dtype=np.float64)
    beta = np.sum(simulation_s, axis=0, dtype=np.float64) / np.sum(evaluation, dtype=np.float64)
    kge_ = 1 - np.sqrt((r - 1) ** 2 + (alpha - 1) ** 2 + (beta - 1) ** 2)
    return kge_


def snow_disappearance_date(swe):
    try:
        date_of_peak = swe['time'].values[swe.argmax()]
        end_date = swe['time'].values[-1]
        sub_swe = swe.sel(time=slice(date_of_peak, end_date))
        has_no_swe = sub_swe == 0
        only_no_swe = np.argwhere(has_no_swe.values)
        return sub_swe['time'].values[only_no_swe[0][0]]
    except:
        return np.datetime64('NaT')


def sdd_diff(swe1, swe2):
    diff = snow_disappearance_date(swe1) - snow_disappearance_date(swe2)
    if isinstance(diff, np.timedelta64):
        return diff.astype('timedelta64[h]') / np.timedelta64(1, 'D')
    else:
        return np.datetime64('NaT')


def peak_swe(swe):
    return swe.max().values[()]


def ps_diff(swe1, swe2):
    return peak_swe(swe1) - peak_swe(swe2)


def mbe(sim, obs):
    return np.nanmean(obs - sim)


#%%
