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


def calc_water_year_apply_SPU(df):
    df['water_year'] = df.DateTime.apply(lambda row: calc_water_year(row))


def snotel_data(path_snotel):
    """read PNNL quality controlled data"""
    snotel_obs = pd.read_csv(path_snotel, sep='\s+', header=None)
    snotel_obs.columns = ['year', 'month', 'day', 'daily_P_in', 'Tmax_F', 'Tmin_F', 'Tmean_F', 'SWE_in']
    snotel_obs['Tmean_C'] = (snotel_obs['Tmean_F'] - 32) * (5 / 9)
    snotel_obs['Tmin_C'] = (snotel_obs['Tmin_F'] - 32) * (5 / 9)
    snotel_obs['Tmax_C'] = (snotel_obs['Tmax_F'] - 32) * (5 / 9)
    snotel_obs = snotel_obs.set_index(pd.DatetimeIndex(pd.to_datetime(snotel_obs[['year', 'month', 'day']])))
    snotel_obs['SWE_m'] = snotel_obs['SWE_in'] * 0.0254
    snotel_obs['datetime'] = snotel_obs.index
    calc_water_year_apply(snotel_obs)
    return snotel_obs


def spu_snotel_data(path_SPU):
    """read SPU data"""
    parse_dates = ['DateTime']
    snotel_obs = pd.read_csv(path_SPU,  sep='\s+', parse_dates=parse_dates)
    snotel_obs = snotel_obs.set_index(snotel_obs['DateTime'])
    calc_water_year_apply_SPU(snotel_obs)
    return snotel_obs

def get_model_dataframe(path_model_data):
    '''this fcn reads the DHSVM model point simulations/ pre-processed by Jason'''
    snotel_model = pd.read_csv(path_model_data)
    snotel_model.set_index(pd.DatetimeIndex(snotel_model.iloc[:, 0]), inplace = True)
    snotel_model.index.name = 'datetime'
    # TO DO add water year
    return snotel_model

def model_point_data_xr(model_data_frame):
    """move the dataframe into an xrray
    get precip data in xclim format
    add units for processing with xclim"""
    #snotel_obs_SPU = SPU_data_frame.to_xarray()
    model_data_frame.index.set_names('time', inplace=True)
    ds_model_data = model_data_frame.to_xarray()
    ds_model_data['tmean_ref'].attrs['units'] = "C"
    ds_model_data['tmean_point'].attrs['units'] = "C"
    ds_model_data['prec_point'].attrs['units'] = "mm/d"
    ds_model_data['prec_ref'].attrs['units'] = "mm/d"
    return  ds_model_data

def spu_snotel_data_xr(SPU_data_frame):
    """get precip data in xclim format
    add units for processing with xclim"""
    #snotel_obs_SPU = SPU_data_frame.to_xarray()
    SPU_data_frame.index.set_names('time', inplace=True)
    #snotel_obs_SPU = xr.DataArray(
    #    SPU_data_frame,
    #    coords= [time_index],
    #    dims= 'time',
    #)
    ds_snotel_obs_SPU = SPU_data_frame.to_xarray()
    ds_snotel_obs_SPU['Max'].attrs['units'] = "mm/d"
    ds_snotel_obs_SPU['Min'].attrs['units'] = "mm/d"
    ds_snotel_obs_SPU['Total'].attrs['units'] = "mm/d"
    return ds_snotel_obs_SPU


def bcbq_snotel_data_xr(bcbq_data_frame):
    """get precip data in xclim format
    add units for processing with xclim"""
    bcbq_data_frame.index.set_names('time', inplace=True)
    snotel_obs = bcbq_data_frame.to_xarray()
    #time_index = snotel_obs_.index
    #time_index  = time_index.to_numpy()
    #bcbq_data_frame_ = snotel_obs_.to_array

    #snotel_obs = xr.DataArray(
    #    bcbq_data_frame_,
    #coords= [time_index],
    #dims= 'time',
    #)
    snotel_obs.daily_P_in.attrs['units'] = "mm/d"
    snotel_obs['Tmax_F'].attrs['units'] = "F"
    snotel_obs['Tmin_F'].attrs['units'] = "F"
    snotel_obs['Tmean_F'].attrs['units'] = "F"
    snotel_obs['Tmean_C'].attrs['units'] = "C"
    snotel_obs['SWE_in'].attrs['units'] = "in"
    snotel_obs['SWE_m'].attrs['units'] = "m"
    return snotel_obs


def spu_snotel_data_xr_T(SPU_data_frame_T):
    """get temp data in xclim format
    add units for processing with xclim"""
    # snotel_obs_SPU = SPU_data_frame.to_xarray()
    #SPU_data_frame_T.index.set_names('time', inplace=True)

    SPU_data_frame_T['Tmean_C'] = (SPU_data_frame_T['Avg'] - 32) * (5 / 9)
    SPU_data_frame_T['Tmin_C'] = (SPU_data_frame_T['Min'] - 32) * (5 / 9)
    SPU_data_frame_T['Tmax_C'] = (SPU_data_frame_T['Max'] - 32) * (5 / 9)

    ds_snotel_obs_SPU_T = SPU_data_frame_T.to_xarray()
    ds_snotel_obs_SPU_T['Tmean_C'].attrs['units'] = "C"
    ds_snotel_obs_SPU_T['Tmin_C'].attrs['units'] = "C"
    ds_snotel_obs_SPU_T['Tmax_C'].attrs['units'] = "C"

    return ds_snotel_obs_SPU_T

