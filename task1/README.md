# Task 1: Predict Restaurant Rating 

##  Project Overview

This project focuses on building a **Machine Learning Regression Model** to predict the **aggregate rating of restaurants** based on various restaurant-related features such as cuisines, location, pricing, delivery options, and customer engagement.

This project helped me understand how regression algorithms can be applied to real-world restaurant data to predict customer ratings and analyze important business factors including:
- Data preprocessing
- Feature engineering
- Data visualization
- Model training
- Model evaluation
- Feature importance analysis

---

#  Objective

To build a machine learning model to predict the
aggregate rating of a restaurant based on other features.

---

# 📂 Dataset Information

The dataset contains information about restaurants including:

| Feature | Description |
|---|---|
| Restaurant Name | Name of the restaurant |
| City | Restaurant location |
| Cuisines | Types of cuisines served |
| Average Cost for Two | Approximate dining cost |
| Price Range | Restaurant pricing category |
| Votes | Number of customer votes/reviews |
| Has Online Delivery | Online delivery availability |
| Has Table Booking | Table booking availability |
| Longitude & Latitude | Geographical location |
| Aggregate Rating | Target variable |

Dataset Size:

:contentReference[oaicite:0]{index=0}

---

#  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

#  Machine Learning Algorithms Used

The following regression algorithms were implemented and compared:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

---

#  Data Preprocessing

The following preprocessing steps were performed:

- Handled missing values
- Encoded categorical variables using Label Encoding
- Selected relevant features
- Split dataset into training and testing sets
- Applied feature scaling for Linear Regression

---

#  Features Used for Prediction

```python
features = [
    'Country Code',
    'City',
    'Locality',
    'Longitude',
    'Latitude',
    'Cuisines',
    'Average Cost for two',
    'Has Table booking',
    'Has Online delivery',
    'Is delivering now',
    'Price range',
    'Votes'
]
```

Target Variable:

```python
Aggregate rating
```

---

#  Exploratory Data Analysis

The project includes multiple visualizations for better understanding of the dataset:

- Correlation Heatmap
- Feature Importance Graph
- Actual vs Predicted Ratings Plot

---

#  Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

#  Model Performance

| Model | MAE | MSE | R² Score |
|---|---|---|---|
| Linear Regression | 1.04 | 1.56 | 0.31 |
| Decision Tree Regressor | 0.27 | 0.17 | 0.92 |
| Random Forest Regressor | 0.19 | 0.08 | 0.96 |

Best Performing Model:

**Random Forest Regressor**

Performance:

:contentReference[oaicite:1]{index=1}

---

#  Feature Importance Analysis

The Random Forest model revealed the most influential features affecting restaurant ratings.

Top contributing features:

1. Votes
2. Longitude
3. Latitude
4. Cuisines
5. Average Cost for Two

Key Insight:

> Restaurants with higher customer engagement (votes/reviews) generally received higher ratings.

---

#  Output Visualizations

## Correlation Heatmap
Shows relationships between numerical features.

## Feature Importance Graph
Displays the contribution of each feature toward rating prediction.

## Actual vs Predicted Ratings
Visualizes prediction accuracy of the Random Forest model.

---

#  Key Learnings

Through this project, the following concepts were explored:

- Regression Algorithms
- Feature Engineering
- Data Preprocessing
- Ensemble Learning
- Model Evaluation
- Data Visualization
- Business Insight Extraction

---
# Personal Learning Outcomes

Through this project, I learned:
- how to preprocess real-world datasets
- how regression algorithms work
- how feature importance affects predictions
- how to compare machine learning models using evaluation metrics
- One interesting observation from this project was that customer votes had a much greater impact on ratings than pricing or delivery features.

#  Conclusion

This project successfully demonstrates how machine learning can be used to predict restaurant ratings based on customer behavior, pricing, cuisine, and location-related features.

Among all models, the **Random Forest Regressor** achieved the highest accuracy and best overall performance due to its ability to capture nonlinear relationships and complex feature interactions.

The project highlights the importance of customer engagement metrics such as votes in determining restaurant popularity and ratings.

---

#  Future Improvements

Possible future enhancements include:

- Deploying the model using Flask or Streamlit
- Building a live restaurant recommendation system
- Using advanced ensemble techniques like XGBoost
- Adding sentiment analysis from restaurant reviews
- Hyperparameter tuning for improved accuracy

```

---

# 📁 Project Structure

```text
task1/
│
├── Dataset.csv
├── task1.py
├── README.md
├── feature_importance.png
├── correlation_heatmap.png
├── actual_vs_predicted.png
```

---