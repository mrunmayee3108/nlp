# Emotion Detection from Text

## 📌 Overview
This project identifies specific emotions from text data. It involves a rigorous comparison of multiple machine learning architectures to find the most precise classifier.

## 📊 Model Comparison (TF-IDF)
| Model | Accuracy (Baseline) | Accuracy (Tuned) |
| :--- | :--- | :--- |
| **Linear SVM** | 89.18% | **90.49%** |
| Random Forest | 88.03% | - |
| Logistic Regression | 86.06% | - |
| Naive Bayes | 66.12% | - |



## 🏗 Key Insights
* **SVM Superiority:** Linear SVM significantly outperformed Naive Bayes and Logistic Regression for this specific multi-class task.
* **BOW vs. TF-IDF:** While Naive Bayes performed better with Bag-of-Words (76.8%), the linear models reached their peak performance using TF-IDF vectorization.
* **Hyperparameter Tuning:** Tuning the Linear SVM pushed the model past the 90% accuracy threshold, making it the production-ready choice for this project.

## 🛠 Tech Stack
* **Vectorization:** Bag-of-Words (BOW), TF-IDF.
* **Algorithms:** MultinomialNB, Logistic Regression, Random Forest, Linear SVC.
