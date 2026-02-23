Overview

This project performs exploratory data analysis on the Netflix Movies and TV Shows dataset from Kaggle. The objective is to clean real-world data, compute key statistical measures, and create required visualisations to analyse content trends on Netflix.

Dataset

Source: https://www.kaggle.com/datasets/shivamb/netflix-shows

Total records: 8,807 titles (Movies and TV Shows)

Data Preparation

Removed duplicates

Converted date_added to datetime

Extracted year_added

Cleaned missing values

Extracted numeric duration for movies

Statistical Moments (Movie Duration)

Mean: 99.58 minutes

Variance: 800.36

Skewness: 0.20

Kurtosis: 2.29

Visualisations

Content type distribution (categorical plot)

Release year vs duration (relational scatter plot)

Correlation heatmap (statistical plot)

Key Insight

Movies dominate the Netflix catalogue (~70%). Movie duration averages around 100 minutes and shows weak correlation with release year.