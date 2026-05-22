import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("Dataset .csv")

print("Dataset Loaded Successfully")

# =========================
# BASIC DATA INFO
# =========================

print("\nDataset Shape:")
print(df.shape)

print("\nCities in Dataset:")
print(df['City'].nunique())

# =========================
# TOP 10 CITIES WITH MOST RESTAURANTS
# =========================

city_counts = df['City'].value_counts().head(10)

print("\nTop 10 Cities:")
print(city_counts)

# =========================
# BAR PLOT - TOP CITIES
# =========================

plt.figure(figsize=(12,6))

sns.barplot(
    x=city_counts.index,
    y=city_counts.values
)

plt.xticks(rotation=45)

plt.title("Top 10 Cities with Most Restaurants")

plt.xlabel("City")

plt.ylabel("Number of Restaurants")

plt.tight_layout()

plt.savefig("top_cities.png")

plt.close()

# =========================
# AVERAGE RATING BY CITY
# =========================

avg_rating = df.groupby('City')['Aggregate rating'].mean()

avg_rating = avg_rating.sort_values(
    ascending=False
).head(10)

print("\nTop Cities by Average Rating:")
print(avg_rating)

# =========================
# RATING VISUALIZATION
# =========================

plt.figure(figsize=(12,6))

sns.barplot(
    x=avg_rating.index,
    y=avg_rating.values
)

plt.xticks(rotation=45)

plt.title("Top Cities by Average Restaurant Rating")

plt.xlabel("City")

plt.ylabel("Average Rating")

plt.tight_layout()

plt.savefig("city_ratings.png")

plt.close()

# =========================
# PRICE RANGE ANALYSIS
# =========================

avg_price = df.groupby('City')['Price range'].mean()

avg_price = avg_price.sort_values(
    ascending=False
).head(10)

print("\nCities with Highest Average Price Range:")
print(avg_price)

# =========================
# MOST COMMON CUISINES
# =========================

cuisine_counts = df['Cuisines'].value_counts().head(10)

print("\nMost Common Cuisines:")
print(cuisine_counts)

# =========================
# CUISINE VISUALIZATION
# =========================

plt.figure(figsize=(12,6))

sns.barplot(
    x=cuisine_counts.values,
    y=cuisine_counts.index
)

plt.title("Most Common Cuisines")

plt.xlabel("Count")

plt.ylabel("Cuisine")

plt.tight_layout()

plt.savefig("common_cuisines.png")

plt.close()

# =========================
# CREATE RESTAURANT MAP
# =========================

restaurant_map = folium.Map(
    location=[
        df['Latitude'].mean(),
        df['Longitude'].mean()
    ],
    zoom_start=2
)

# Add sample restaurant markers

sample_df = df.sample(100)

for index, row in sample_df.iterrows():

    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name']
    ).add_to(restaurant_map)

# Save map

restaurant_map.save("restaurant_map.html")

print("\nMap saved as restaurant_map.html")

# =========================
# FINAL INSIGHTS
# =========================

print("\nLocation-Based Analysis Completed Successfully")