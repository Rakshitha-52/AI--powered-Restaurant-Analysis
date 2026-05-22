# Task 2: Restaurant Recommendation 

##  Overview

This project focuses on building a Restaurant Recommendation System using Machine Learning techniques. The system recommends restaurants to users based on their preferences such as cuisine type, city, and price range.

The recommendation system uses a content-based filtering approach, where restaurants with similar features are suggested to the user.

---

# 🎯 Objective

The main goal of this project is to Create a restaurant recommendation system based on user preferences by analyzing restaurant features like:
- cuisines
- location
- pricing
- online delivery availability

---

#  Technologies Used

- Python
- Pandas
- Scikit-learn

---

# 📂 Dataset Information

The dataset contains information about restaurants including:
- Restaurant Name
- City
- Cuisines
- Price Range
- Online Delivery
- Aggregate Rating

Dataset Size:
- 9551 restaurants
- 21 features

---

#  Recommendation Approach

This project uses a **Content-Based Recommendation System**.

The recommendation process works as follows:

1. Important restaurant features are selected
2. Features are combined into a single text column
3. Text data is converted into numerical vectors
4. Similar restaurants are identified using cosine similarity

---

#  Features Used

```python
features = [
    'Cuisines',
    'City',
    'Price range',
    'Has Online delivery'
]
```

---

# 🔄 Project Workflow

## Step 1 — Data Preprocessing

- Loaded the dataset
- Handled missing values
- Selected useful features

---

## Step 2 — Feature Combination

Restaurant features were combined into a single column called `tags`.

Example:

```text
North Indian New Delhi 2 Yes
```

---

## Step 3 — Text Vectorization

The text data was converted into vectors using:

```python
CountVectorizer()
```

Vector Shape:

```text
(9551, 314)
```

---

## Step 4 — Similarity Calculation

Cosine similarity was used to measure similarity between restaurants.

Restaurants with higher similarity scores are recommended to the user.

---

# Sample Recommendation

## User Preference

```text
Cuisine      : North Indian
City         : New Delhi
Price Range  : 2
```

## Recommended Restaurants

| Restaurant | Cuisine | Rating |
|---|---|---|
| Food Scouts | North Indian, Chinese, Continental | 4.3 |
| The Vintage Avenue | North Indian, Chinese, Continental, Italian | 3.9 |
| Indian Bites | North Indian, Chinese, Continental | 2.7 |
| Pradhan Ji Multi Cuisine Restaurant | North Indian, Chinese, Continental | 3.3 |

---

#  Output Analysis

The recommendation system was able to:
- recommend restaurants with similar cuisines
- match restaurants from the same city
- consider user budget preferences
- provide relevant restaurant suggestions

---

#  What I Learned

Through this project, I learned:
- how recommendation systems work
- content-based filtering concepts
- text vectorization using CountVectorizer
- cosine similarity calculations
- feature engineering techniques

---

#  Advantages

- Simple and fast recommendation system
- Personalized suggestions
- Easy to improve and expand
- Works without user history

---

#  Limitations

- Recommendations are based only on restaurant features
- User reviews and user behavior are not considered
- Similar restaurants may sometimes repeat

---

#  Future Improvements

Possible future enhancements:
- Add collaborative filtering
- Build a web application using Flask or Streamlit
- Include user ratings and reviews
- Improve recommendation accuracy
- Add restaurant search functionality


---

# 📁 Project Structure

```text
task2/
│
├── Dataset.csv
├── task2.py
├── README.md
```

---

#  Conclusion

This project demonstrates how machine learning techniques can be used to build a restaurant recommendation system. Using content-based filtering and cosine similarity, the system successfully recommends restaurants based on user preferences.

The project also helped in understanding recommendation algorithms and real-world applications of machine learning.

---
