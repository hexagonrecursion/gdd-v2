# SPDX-FileCopyrightText: 2021 Andrey Bienkowski <hexagon-recursion@posteo.net>
#
# SPDX-License-Identifier: MIT

import cdstoolbox as ct

def get_daily_mean_for_year_and_month(year, month):
    print('get temperature', year, month)
    temperature = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'variable': '2m_temperature',
            'year': str(year),
            'month': str(month),
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        }
    )
    print('got')
    daily_mean = ct.climate.daily_mean(temperature)
    print('daily_mean', year, month)
    return daily_mean
    
def get_gdd_for_year(year):
    by_month = [
        get_daily_mean_for_year_and_month(year, month)
        for month in range(1, 12+1)
    ]
    daily_mean = ct.cube.concat(by_month, dim='time')
    print('daily_mean')
    gdd_min_temperature_celsius = 10
    gdd = ct.cdstools.heuristics.growing_degree_days(
        daily_mean,
        gdd_min_temperature_celsius
    )
    print('gdd')
    return gdd

@ct.application()
@ct.output.download()
def gdd_app():
    by_year = [get_gdd_for_year(year) for year in range(2003, 2020+1)]
    combined = ct.cube.concat(by_year, dim='time')
    print('combined', ct.cdm.get_coordinates(combined))
    return combined