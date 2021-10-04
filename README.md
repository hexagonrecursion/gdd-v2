<!--
SPDX-FileCopyrightText: 2021 Andrey Bienkowski <hexagon-recursion@posteo.net>

SPDX-License-Identifier: MIT
-->

# Calculate the Growing Degree Days
## 1. Download the temperature data
Input: ./download.py
Input: temperature data from the Copernicus Climate Data Store
Output: ./gdd.nc

1. Register with the Copernicus Climate Data Store, copy ./download.py into the [toolbox editor](https://cds.climate.copernicus.eu/toolbox-editor/) and run it
2. Save the file as ./gdd.nc

## 2. Convert the data to .csv
Input: ./gdd.nc
Output: ./gdd.csv

1. Install [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/)
2. Run `pip install -r requirements.txt`. See https://pip.pypa.io/en/stable/user_guide/#requirements-files
3. Run `python to-csv.py`
