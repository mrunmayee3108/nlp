# Twitter Sentiment Analysis (1.6M Tweets)

## Project Overview

This project is an end-to-end sentiment analysis pipeline built using Python. It classifies 1,600,000 tweets into **Positive** or **Negative** categories. The project focuses on handling large-scale text data efficiently using sparse matrices and optimized linear models.

## Tech Stack & Requirements

* **Pandas:** For data loading and preprocessing.
* **NumPy:** For high-performance numerical operations and array management.
* **Scikit-Learn:** For TF-IDF vectorization, model training, and hyperparameter tuning.
* **Matplotlib & Seaborn:** For visualizing model performance and confusion matrices.

## Model Performance

I evaluated three different classification algorithms to find the best balance between speed and precision.

| Model | Accuracy | Notes |
| --- | --- | --- |
| **Logistic Regression (Tuned)** | **79.13%** | Final selected model|
| Logistic Regression (Default) | 79.18% | Baseline performance before regularization tuning. |
| Linear SVC | 78.71% | Strong performance but slower training time. |
| Multinomial Naive Bayes | 77.78% | Fastest training; excellent for baseline comparison. |

## Key Steps

* **TF-IDF Vectorization:** Converted raw text into a numerical format using N-grams (unigrams and bigrams) to capture context.
* **Hyperparameter Tuning:** Conducted `GridSearchCV` on a 50,000-row subset to find the optimal `C` parameter for Logistic Regression, ensuring the model generalizes well to unseen data.

## Results & Analysis

The final tuned Logistic Regression model achieves a stable **79.13% accuracy**. While the default model had a slightly higher decimal, the tuned version provides better **regularization**, making it more robust against the noise and slang found in real-world Twitter data.

