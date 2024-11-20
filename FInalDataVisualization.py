import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# We read in the data from the data sets
# roadConditionData = pd.read_csv("./Data/Real-Time_Road_Conditions_20241120.csv")
# trafficIncidentData = pd.read_csv("./Data/Real-Time_Traffic_Incident_Reports_20241120.csv",
#                                   low_memory=False)
# pedestrianSignalData = pd.read_csv("./Data/Traffic_Signals_and_Pedestrian_Signals_20241120.csv")


# Define the custom datetime format for date parsing
# date_format_roadCondition = "%m/%d/%Y %I:%M:%S %p"
# date_format_trafficIncident = "%m/%d/%Y %I:%M:%S %p %z"
# roadConditionData['timestamp'] = pd.to_datetime(roadConditionData['timestamp'], format=date_format_roadCondition)
# roadConditionData['date'] = roadConditionData['timestamp'].dt.date
# roadConditionData.set_index('date', inplace=True)
# trafficIncidentData['Published Date'] = pd.to_datetime(trafficIncidentData['Published Date'], format=date_format_trafficIncident)
# trafficIncidentData['date'] = trafficIncidentData['Published Date'].dt.date

# Temporary pickle section for debugging purposes and maybe for people who pull this repo

# roadConditionData.to_pickle("./roadConditionData.pkl")
# trafficIncidentData.to_pickle("./trafficIncidentData.pkl")

roadConditionData = pd.read_pickle("./roadConditionData.pkl")
trafficIncidentData = pd.read_pickle("./trafficIncidentData.pkl")

# TODO Create a time series graph that plots the crashes in Austin throughout the year. If you can combine it with road temperatures too all the better

# Create the data frames and the date ranges we'll use. We have more road condition data than traffic incident data, so the date range will be the range of the incident reports
daily_crashes = trafficIncidentData.groupby('date').size()
date_index = pd.date_range(start=daily_crashes.index.min(), end=daily_crashes.index.max())

# Calculate average temperature for each day across all roads in Austin
temperatures = roadConditionData.loc[date_index.min().date():date_index.max().date()].resample('D').mean()

print(temperatures.head(5))

# sns.set_theme(style='darkgrid')
# plt.figure(figsize = (15,6))
#
# plt.plot()
#
# plt.title("Daily Traffic Incidents Reported in Austin TX")
# plt.xlabel('Date')
# plt.legend()

# TODO Create a heat map of road grip (using roadConditionData) and pedestrianSignalData

# TODO Create a bar graph that plots the roads with the number of crahes reported on them

# TODO If we want to add that sidewalk data set, plot in a bar graph which roads have the most sidewalks