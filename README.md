# 🐦 Bird Observation Dashboard

## 📌 Project Overview

This project presents a comprehensive **Exploratory Data Analysis (EDA)** of bird observation data collected across varied landscapes and environmental settings. It aims to deliver interactive insights on bird species behavior, environmental influences, and conservation alerts using visual storytelling.

---

## 🔍 Approach

### 1. Data Cleaning and Preprocessing

* Managed missing data and standardized observation metrics.
* Filtered key columns such as species names, environmental conditions, and timestamps.
* Merged datasets from forest and grassland units to enable consistent analysis.

### 2. Exploratory Data Analysis (EDA)

#### Temporal Analysis

* **Seasonal Trends:** Evaluated how sightings vary across years, months, and seasons.
* **Observation Time:** Studied start and end times to identify high-activity periods.

#### Spatial Analysis

* **Location Insights:** Grouped by `Location_Type` to pinpoint biodiversity hotspots.
* **Plot-Level Analysis:** Compared bird activity across different `Plot_Name` entries.

#### Species Analysis

* **Diversity Metrics:** Counted unique species per location and habitat.
* **Activity Patterns:** Examined activity types using `Interval_Length` and `ID_Method`.

#### Environmental Conditions

* **Weather Correlation:** Analyzed how `Temperature`, `Humidity`, `Sky`, and `Wind` impact bird sightings.
* **Disturbance Effect:** Investigated the role of environmental disturbance on bird behavior.

#### Distance and Behavior

* **Distance Analysis:** Explored species occurrence relative to observation distance.
* **Flyover Frequency:** Tracked flyover behavior by species and distance.

#### Observer Trends

* **Observer Bias:** Studied data consistency and volume across individual observers.
* **Visit Patterns:** Analyzed the impact of repeated visits on bird diversity and sightings.

#### Conservation Insights

* **Watchlist Trends:** Used `PIF_Watchlist_Status` and `Regional_Stewardship_Status` to highlight conservation-critical species.
* **AOU Code Patterns:** Connected species trends with AOU codes for conservation mapping.

---

## 📊 Visualization

Built using **Plotly** and deployed via **Streamlit**, the dashboard includes:

* Interactive scatter plots, bar charts, box plots, and pie charts.
* Filters and dropdowns for user-guided exploration.
* Optional export capabilities and CSV downloads.
* Integration-ready for Power BI (if needed).

---