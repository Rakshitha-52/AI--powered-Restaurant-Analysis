import pandas as pd

# Vectorization
from sklearn.feature_extraction.text import CountVectorizer

# Similarity
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("Dataset .csv")

print("Dataset Loaded Successfully")

# =========================
# HANDLE MISSING VALUES
# =========================

df['Cuisines'] = df['Cuisines'].fillna("Unknown")

# =========================
# CREATE TAGS COLUMN
# =========================

def combine_features(row):

    return (
        str(row['Cuisines']) + " " +
        str(row['City']) + " " +
        str(row['Price range']) + " " +
        str(row['Has Online delivery'])
    )

df["tags"] = df.apply(combine_features, axis=1)

print("\nCombined Feature Tags:")
print(df["tags"].head())

# =========================
# CONVERT TEXT TO VECTORS
# =========================

cv = CountVectorizer(stop_words='english')

vector = cv.fit_transform(df['tags'])

print("\nVector Shape:")
print(vector.shape)

# =========================
# CALCULATE COSINE SIMILARITY
# =========================

similarity = cosine_similarity(vector)

print("\nSimilarity Matrix Shape:")
print(similarity.shape)

# =========================
# RECOMMENDATION FUNCTION
# =========================

def recommend_restaurants(cuisine, city, price_range):

    print("\nRecommended Restaurants:\n")

    # Filter restaurants matching user preference

    filtered = df[
        (df['Cuisines'].str.contains(cuisine, case=False, na=False)) &
        (df['City'].str.contains(city, case=False, na=False)) &
        (df['Price range'] == price_range)
    ]

    # Sort by rating

    filtered = filtered.sort_values(
        by='Aggregate rating',
        ascending=False
    )

    # No matches found

    if filtered.empty:
        print("No matching restaurants found.")
        return

    # Best matching restaurant

    restaurant_index = filtered.index[0]

    # Similarity scores

    distances = similarity[restaurant_index]

    # Create sorted similarity list

    restaurant_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    # Track duplicates

    recommended_names = set()

    count = 0

    # =========================
    # DISPLAY RECOMMENDATIONS
    # =========================

    for i in restaurant_list:

        idx = i[0]

        # Skip same restaurant

        if idx == restaurant_index:
            continue

        restaurant_name = df.iloc[idx]['Restaurant Name']

        # Avoid duplicates

        if restaurant_name in recommended_names:
            continue

        # Apply filters

        if (
            df.iloc[idx]['Price range'] == price_range
            and city.lower() in str(df.iloc[idx]['City']).lower()
        ):

            recommended_names.add(restaurant_name)

            print("Restaurant Name :", restaurant_name)

            print("Cuisine :", df.iloc[idx]['Cuisines'])

            print("City :", df.iloc[idx]['City'])

            print("Rating :", df.iloc[idx]['Aggregate rating'])

            print("Price Range :", df.iloc[idx]['Price range'])

            print("-" * 50)

            count += 1

        # Show only top 5

        if count == 5:
            break

# =========================
# SAMPLE RECOMMENDATION
# =========================

recommend_restaurants(
    cuisine="North Indian",
    city="New Delhi",
    price_range=2
)