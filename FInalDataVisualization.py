import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# We read in the data from the data sets
roadConditionData = pd.read_csv("./Data/Real-Time_Road_Conditions_20241120.csv")
trafficIncidentData = pd.read_csv("./Data/Real-Time_Traffic_Incident_Reports_20241120.csv",
                                  low_memory=False)
pedestrianSignalData = pd.read_csv("./Data/Traffic_Signals_and_Pedestrian_Signals_20241120.csv")

# Define the custom datetime format for date parsing
date_format_roadCondition = "%m/%d/%Y %I:%M:%S %p"
date_format_trafficIncident = "%m/%d/%Y %I:%M:%S %p %z"
roadConditionData['date'] = pd.to_datetime(roadConditionData['timestamp'], format=date_format_roadCondition)
roadConditionData['date'] = roadConditionData['date'].dt.normalize()
trafficIncidentData['date'] = pd.to_datetime(trafficIncidentData['Published Date'], format=date_format_trafficIncident)
trafficIncidentData['date'] = trafficIncidentData['date'].dt.normalize()

# Temporary pickle section for debugging purposes and maybe for people who pull this repo
roadConditionData.to_pickle("./roadConditionData.pkl")
trafficIncidentData.to_pickle("./trafficIncidentData.pkl")

roadConditionData = pd.read_pickle("Pickles/roadConditionData.pkl")
trafficIncidentData = pd.read_pickle("Pickles/trafficIncidentData.pkl")


# region Creates the visualizations for Daily Crashes and Daily Average Road Temperature

# Create the data frames and the date ranges we'll use. We have more road condition data than traffic incident data, so the date range will be the range of the incident reports
daily_crashes = trafficIncidentData.groupby('date').size()
date_index = pd.date_range(start=daily_crashes.index[0], end=daily_crashes.index[-1])

# Calculate average temperature for each day across all roads in Austin
start = date_index[0].asm8
end = date_index[-1].asm8

# This block filters the condition data by date, converts the temp_surface column to Fahrenheit, and gets the daily average of that column
temperatures = roadConditionData[(roadConditionData['date'] >= start) & (roadConditionData['date'] <= end) & (roadConditionData['temp_surface'] != 100.1)]
temperatures['temp_surface'] = temperatures['temp_surface'].apply(lambda x: (x * 9/5) + 32)
temperatures = temperatures[['date', 'temp_surface']].groupby('date').mean()

# This block displays the Daily Traffic Incidents
sns.set_theme(style='darkgrid')
plt.figure(figsize=(15, 6))
daily_crashes.plot()
plt.title("Daily Traffic Incidents Reported in Austin TX")
plt.xlabel('Date')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.show()

# This block displays the Average Daily Road Temperature
sns.set_theme(palette=sns.color_palette("flare"))
temperatures.plot()
plt.title("Daily Average Surface Temperatures of Roads in Austin TX")
plt.ylabel("Temperature (F)")
plt.legend(['Temperature'])
plt.figure().set_layout_engine(layout='none')
plt.show()

# endregion

# TODO Create a heat map of road grip (using roadConditionData) and pedestrian infrastructure (pedestrianSignalData)

# TODO Create a bar graph that plots the roads with the number of crashes reported on them

# TODO If we want to add that sidewalk data set, plot in a bar graph which roads have the most sidewalks
