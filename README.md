# AI-- powered Restaurant Analysis

## 📌 Project Overview

This project focuses on applying Machine Learning, Recommendation Systems, and Data Analysis techniques to solve real-world problems in the restaurant industry. The project was developed using restaurant datasets containing information such as cuisines, ratings, pricing, customer votes, delivery availability, and geographical locations.

The project includes three major tasks:

- Restaurant Rating Prediction
- Restaurant Recommendation System
- Location-Based Restaurant Analysis

The main objective of this project is to analyze restaurant data, generate useful business insights, predict restaurant ratings, and provide personalized restaurant recommendations.

---

# 🎯 Objectives

- Predict restaurant ratings using machine learning models
- Build a recommendation system based on user preferences
- Analyze restaurant distribution and trends using geographical data
- Extract insights from restaurant datasets using visualization and statistical analysis

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Folium

---

# 📂 Dataset Information

The dataset contains restaurant-related information including:

| Feature | Description |
|---|---|
| Restaurant Name | Name of the restaurant |
| City | Restaurant location |
| Cuisines | Types of cuisines served |
| Aggregate Rating | Customer rating |
| Votes | Customer engagement |
| Price Range | Restaurant pricing category |
| Online Delivery | Delivery availability |
| Latitude & Longitude | Geographical coordinates |

Dataset Size:
- 9551 Restaurants
- 21 Features

---

# 📌 Tasks Completed

---

# ✅ Task 1 – Restaurant Rating Prediction

## Objective
Build a machine learning model to predict restaurant ratings using restaurant-related features.

## Techniques Used
- Data Preprocessing
- Label Encoding
- Feature Engineering
- Feature Scaling
- Regression Models

## Algorithms Implemented
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

## Best Result
Random Forest Regressor achieved the highest performance with an R² Score of approximately 0.96.

## Key Insight
Customer votes were found to be the most influential factor affecting restaurant ratings.

---

# ✅ Task 2 – Restaurant Recommendation System

## Objective
Develop a content-based restaurant recommendation system based on user preferences.

## Recommendation Criteria
- Cuisine Preference
- City
- Price Range
- Online Delivery Availability

## Techniques Used
- Content-Based Filtering
- CountVectorizer
- Cosine Similarity

## Workflow
- Combined restaurant features into text tags
- Converted text into vectors
- Calculated similarity scores
- Recommended restaurants with similar features

## Sample Recommendation
The system successfully recommended restaurants similar to user preferences such as:
- North Indian cuisine
- New Delhi location
- Medium price range

---

# ✅ Task 4 – Location-Based Analysis

## Objective
Perform geographical and statistical analysis of restaurant data.

## Analysis Performed
- Restaurant distribution by city
- Average ratings by city
- Cuisine popularity analysis
- Price range analysis
- Interactive restaurant mapping

## Visualization Tools
- Matplotlib
- Seaborn
- Folium

## Key Insights
- New Delhi contained the highest number of restaurants
- North Indian cuisine was the most common cuisine
- Highly rated restaurants were concentrated in selected metropolitan regions

---

# 📊 Outputs Generated

## Task 1 Outputs
- Correlation Heatmap
- Feature Importance Graph
- Actual vs Predicted Ratings Graph

## Task 2 Outputs
- Personalized Restaurant Recommendations

## Task 4 Outputs
- Top Cities Visualization
- Cuisine Distribution Graph
- Interactive Restaurant Map

---

# 🚀 Key Learnings

Through this project, I gained hands-on experience in:
- Machine Learning workflows
- Recommendation systems
- Data preprocessing
- Feature engineering
- Model evaluation
- Data visualization
- Geographical analysis
- Business insight generation

---

# 📈 Future Improvements

Possible future enhancements include:
- Deploying the project using Flask or Streamlit
- Adding collaborative filtering techniques
- Integrating sentiment analysis on restaurant reviews
- Building a real-time recommendation system
- Creating an interactive dashboard

---

# ▶️ How to Run the Project

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Run Individual Tasks

### Task 1
```bash
python task1.py
```

### Task 2
```bash
python task2.py
```

### Task 4
```bash
python task4.py
```

---

# 📁 Project Structure

```text
Restaurant_Analytics_Project/
│
├── Task1_Rating_Prediction/
│   ├── task1.py
│   ├── README.md
│   ├── feature_importance.png
│   ├── actual_vs_predicted.png
│   └── correlation_heatmap.png
│
├── Task2_Recommendation_System/
│   ├── task2.py
│   └── README.md
│
├── Task4_Location_Analysis/
│   ├── task4.py
│   ├── restaurant_map.html
│   ├── top_cities.png
│   ├── city_ratings.png
│   ├── common_cuisines.png
│   └── README.md
│
├── Dataset.csv
├── requirements.txt
├── Final_Report.pdf
└── README.md
```

---

# 📌 Conclusion

This project successfully demonstrated the practical application of Machine Learning, Recommendation Systems, and Data Analysis techniques in the restaurant industry. The project provided valuable insights into customer preferences, restaurant trends, rating prediction, and geographical distribution patterns.

By combining predictive analytics, recommendation systems, and visualization techniques, the project highlights how data-driven solutions can support better decision-making and improve user experience in real-world business scenarios.

---

# 👩‍💻 Author

Rakshitha B N
