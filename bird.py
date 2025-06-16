import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dhinesh@0512",
    database="BIRDS_DATABASE"
)

# Load data
def load_table(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(result, columns=columns)

df = load_table("SELECT * FROM birds_analysis")

# App config
st.set_page_config(page_title="Bird Observation EDA", layout="wide")
st.title("🦉 Bird Observation Dashboard")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📅 Temporal Analysis", "🌍 Spatial Analysis", "🐦 Species Analysis",
    "🌦️ Environmental Conditions", "📏 Distance and Behavior",
    "🧑‍💼 Observer Trends", "🛡️ Conservation Insights", "👤 Creator Info"
])

# 1. Temporal Analysis
with tab1:
    st.header("📅 1. Temporal Analysis")
    option = st.selectbox("Select Category",("Sightings per Month", "Sightings per Season", "Observations by Start Hour", "Observations by Time Period"))
    if option == "Sightings per Month" :
     fig_month = px.histogram(df, x='Month', title="Sightings per Month", width =300)
     st.plotly_chart(fig_month)
    elif option == "Sightings per Season":
     fig_season = px.histogram(df, x='Season', title="Sightings per Season")
     st.plotly_chart(fig_season)
    elif option == "Observations by Start Hour":
     fig_hour = px.histogram(df,x='Start_Hour',title='Observations by Start Hour',labels={'Start_Hour': 'Start Hour'},nbins=24)
     st.plotly_chart(fig_hour)
    elif option == "Observations by Time Period":
     fig_period = px.histogram(df, x='Time_Period', title="Observations by Time Period")
     st.plotly_chart(fig_period)

# 2. Spatial Analysis
with tab2:
    st.header("🌍 2. Spatial Analysis")
    option = st.selectbox("Select Category",("Observations by Location Type","Observations by Plot"))
    if option == "Observations by Location Type":
     fig_loc_type = px.histogram(df, x='Location_Type', title="Observations by Location Type")
     st.plotly_chart(fig_loc_type)
    elif option == "Observations by Plot":
     fig_plot = px.histogram(df, x='Plot_Name', title="Observations by Plot")
     st.plotly_chart(fig_plot)

# 3. Species Analysis
with tab3:
    st.header("🐦 3. Species Analysis")
    option = st.selectbox("Select Category",("Unique Species per Location","Activity by ID Method"))
    if option == "Unique Species per Location":
     species_count = df.groupby("Location_Type")["Scientific_Name"].nunique().reset_index()
     fig_species = px.bar(species_count, x="Location_Type", y="Scientific_Name", title="Unique Species per Location")
     st.plotly_chart(fig_species)
    elif option == "Activity by ID Method" :
     fig_id_method = px.bar(df, x='ID_Method', color='Interval_Length', title="Activity by ID Method")
     st.plotly_chart(fig_id_method)

# 4. Environmental Conditions
with tab4:
    st.header("🌦️ 4. Environmental Conditions")
    option = st.selectbox("Select Category",("Temperature", "Humidity", "Sky", "Wind", "Disturbance"))
    if option in ["Temperature", "Humidity"]:
        data1 = df.groupby([option, 'Distance']).size().reset_index(name='Count')
        fig1 = px.scatter(data1,x=option,y='Count', color='Distance',title=f"{option} vs. Bird Observation Count")
        st.plotly_chart(fig1)
    elif option in ["Sky", "Wind"]:
        data2 = df[option].value_counts().reset_index()
        data2.columns = [option, 'Observation Count']
        fig = px.pie(data2,names=option,values='Observation Count',title=f"Distribution of Observations by {option}")
        st.plotly_chart(fig)
    elif option == "Disturbance":
        dist_obs = df['Disturbance'].value_counts().reset_index()
        dist_obs.columns = ['Disturbance', 'Observation Count']
        fig2 = px.pie(dist_obs,names='Disturbance',values='Observation Count',title="Distribution of Observations by Disturbance")
        st.plotly_chart(fig2)

# 5. Distance and Behavior
with tab5:
    st.header("📏 5. Distance and Behavior")
    option = st.selectbox("Select Category",("Distance of Observations","Close Observed Species","Far Observed Species","Flyover Observations"))
    if option == "Distance of Observations":
     fig_distance = px.bar(df, x='Distance', title="Distance of Observations")
     st.plotly_chart(fig_distance)
    elif option == "Close Observed Species":
     close_species = df[df['Distance'] == '<= 50 Meters']['Scientific_Name'].value_counts().head(10).reset_index().rename(columns={'index': 'Scientific_Name', 'Scientific_Name': 'Scientific_Name'})
     fig_close = px.bar(close_species, x='Scientific_Name',y='count',title="Close Observed Species",color='Scientific_Name')
     st.plotly_chart(fig_close)   
    elif option == "Far Observed Species":
     far_species = df[df['Distance'] == '50 - 100 Meters']['Scientific_Name'].value_counts().head(10).reset_index().rename(columns={'index': 'Scientific_Name', 'Scientific_Name': 'Scientific_Name'})
     fig_far = px.bar(far_species, x='Scientific_Name',y='count',title="Far Observed Species",color='Scientific_Name')
     st.plotly_chart(fig_far)
    elif option == "Flyover Observations":
     fig_flyover = px.bar(df, x='Flyover_Observed', title="Flyover Observations")
     st.plotly_chart(fig_flyover)

# 6. Observer Trends
with tab6:
    st.header("🧑‍💼 6. Observer Trends")
    option = st.selectbox("Select Category",("Observations per Observer","Species Count per Visit"))
    if option == "Observations per Observer":
     fig_observer = px.bar(df, x='Observer', title="Observations per Observer")
     st.plotly_chart(fig_observer)
    elif option == "Species Count per Visit":
     visit_obs = df.groupby('Visit').agg(Total_observations=('Scientific_Name', 'count')).reset_index()
     fig_visit = px.bar(visit_obs, x='Visit',y='Total_observations',title="Species Count per Visit")
     st.plotly_chart(fig_visit)

# 7. Conservation Insights
with tab7:
    st.header("🛡️ 7. Conservation Insights")
    option = st.selectbox("Select Category",("Species by Watchlist","Species by AOU Code"))
    if option == "Species by Watchlist" :
     watchlist_obs = df.groupby('PIF_Watchlist_Status').agg(Total_observations=('Scientific_Name', 'count')).reset_index()
     fig_watchlist = px.bar(watchlist_obs, x='PIF_Watchlist_Status',y='Total_observations',title="Species by Watchlist")
     st.plotly_chart(fig_watchlist)
    elif option == "Species by AOU Code" :
     fig_aou = px.histogram(df, x='AOU_Code', title="Species by AOU Code")
     st.plotly_chart(fig_aou)

# 8. Creator Info
with tab8:
    st.header("👤 Creator of this Project")
    st.markdown("""
    **App Name:** Birds Observation Dashboard  
    **Creator:** DHINESH KUMAR KANNAN  
    **Purpose:** Analyze and visualize bird observation data for research and conservation.
    """)
