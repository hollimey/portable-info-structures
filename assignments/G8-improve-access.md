## About
The information structure provides values for ocean data like tide levels, sea surface temperature, wave height, and other information. Users can quickly view the ocean information at the beach or sea closest to them. Any Apple Weather users will be able to see the widget displaying the data visually in a graph.

#### Data sources used:
Data guide- https://www.ndbc.noaa.gov/docs/ndbc_web_data_guide.pdf <br/>
Latest observation list (lat/long included)- https://www.ndbc.noaa.gov/data/latest_obs/latest_obs.txt <br/>
Data descriptions- https://www.ndbc.noaa.gov/faq/measdes.shtml

#### Other sources not used but helpful:
Real time data file list- https://www.ndbc.noaa.gov/data/realtime2/ <br/>
Global monitoring data map- https://viz.pmel.noaa.gov/osmc/?color_by=platform_type&platform_code=PTAW1 <br/>
US (plus some global) buoy data map- https://www.ndbc.noaa.gov/ <br/>
US tide data- https://tidesandcurrents.noaa.gov/map/

## Methodology
Datasets, for now, are manually downloaded per day from the NOAA's water station webpages. The datasets are then uploaded into code for processing, cleaning, and visualization. As datasets get verified, the newly verified data will take priority over "preliminary" and "predicted" data. Our maintenance process will consist of re-uploading verified datasets after release, in case users wish to look at past data. We will also only be keeping 2 weeks and 1 day worth of data, for the current data and the week before and week after. This reduces storage needs and eases maintenance needs. Thus, future data will come from the predicted column and past data will either be preliminary or verified. 

## Access
1. Download datasets and python code script from github repository.
2. Input desired datasets for date range of examination into Flask App.
3. Run Flask App.
4. Run python script in Flask App.
5. View graphs of tidal levels by hour and on selected days.

## Structure
There are 22 columns in the information structure.

#### The structure is broken down as follows:
+ `#STN` represents the station number of the vessel the ocean observation came from. <br/>
+ `LAT` and `LON` represents the lattitude and longitude in degrees. <br/>
+ `YYYY MM DD` and `hh mm` represents the date, and the hour and minute the observation was recorded at. <br/>
+ `WDIR` represents the wind direction in degrees True (degT). <br/>
+ `WSPD` and `GST` represents the wind and gusts speed in meters per second (m/s). <br/>
+ `WVHT` represents the significant wave height, meaning the average height of the highest one-third of the waves. Measured in meters. <br/>
+ `DPD` and `APD` represents the dominant and the average wave period in seconds. The dominant period is the time between wave crests of the most energetic/dominant waves in the spectrum. It's the time interval between successive wave peaks of the dominant wave system. The dominant measurement helps describe the primary swell affecting an area. The average period is the measurement of all detected waves over a sampling interval. It represents a mean value, not necessarily tied to a specific wave system. The average measurement gives a general sense of the wave environment's average rhythm. <br/>
+ `MWD` represents the mean wave direction in degrees True (degT). This indicates the direction from which the waves are coming, measured relative to true north, not the magnetic north. <br/>
+ `PRES` and `PTDY` represents the sea-level pressure and the pressure tendency in hectopascals (hPa). The pressure tendency is the change in atmospheric pressure; a positive value means the pressure is rising, and a negative value means the pressure is falling. <br/>
+ `ATMP`, `WTMP`, and `DEWP` represents the air temperature, water/sea surface temperature, and the dew point temperature in degrees Celsius (degC). The dew point indicates the moisture content in the air. <br/>
+ `VIS` represents the visibility in nautical miles (nmi). Meaning, the distance over which an object or light can be clearly seen at sea. <br/>
+ `TIDE` represents the tide in feet (ft). This refers to the vertical height of the ocean's surface relative to a reference level; usually mean lower low water or MLLW. The tide measurement tells you how high or low the sea level is at a particular time and place due to the tide pattern caused by the gravitational pull of the moon and sun. <br/>
<br/>

> [!TIP]
> Please follow these [code instructions](portable-info-structures/final-overview/code/readme.md) to view the data structure. Or, for a more simplified approach, you can also find a similar example of the information structure [here](example-structure/G8_CO-OPS_9444900_wl.csv).
