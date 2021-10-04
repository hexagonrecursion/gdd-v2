# SPDX-FileCopyrightText: 2021 Andrey Bienkowski <hexagon-recursion@posteo.net>
#
# SPDX-License-Identifier: MIT

import xarray
series = xarray.open_dataset('./gdd.nc').to_dataframe()['gdd']
reshaped = series.unstack('time')
reshaped.to_csv('./gdd.csv')