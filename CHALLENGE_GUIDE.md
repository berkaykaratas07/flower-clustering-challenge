# Flower Clustering Challenge Guide

## Challenge Overview
This challenge aims to develop your machine learning skills by analyzing flower images and clustering them based on their similarities. Your goal is to create a model that can distinguish between different flower types and cluster the images to achieve results as close to the original classes as possible.

## Goal
Process the images in the flower dataset using your chosen model and algorithms to group them into clusters, achieving a high accuracy in replicating the original classes. This challenge encourages flexible experimentation with model selection and feature extraction techniques, allowing you to explore various approaches and solutions.

## Success Criteria
The success of your model will be evaluated based on the similarity between the clusters you create and the original classes in the dataset. The overlap ratio between your clusters and the original labels will be the main criterion.

### Scoring System
- 50% - 60% similarity: 1 point
- 60% - 70% similarity: 2 points
- 70% - 80% similarity: 3 points
- 80% - 90% similarity: 4 points
- 90% - 100% similarity: 5 points

A maximum of 25 points can be achieved.

### Recommended Performance Metrics
- **Silhouette Score**: Use the silhouette score to measure the quality of cluster separation. A high silhouette score indicates well-separated clusters.
- **Accuracy**: Compare your results with the original dataset by calculating the proportion of correctly classified images.

## Instructions

The steps below provide a general process to follow throughout the challenge. However, participants are free to choose any model and algorithms, and the steps can be modified as desired.

### 1. Loading the Data
- Load the `.npy` files in the `model/` folder using **numpy**.
- Refer to the example notebook for sample code and detailed instructions if needed.

### 2. Data Preprocessing
- Scale the loaded features using `StandardScaler`. Standardizing the dataset can help clustering algorithms perform better.

### 3. Dimensionality Reduction with PCA (Optional)
- Optionally, reduce the dataset’s dimensions using **Principal Component Analysis (PCA)**. It’s recommended to use 9 components.
- After reducing the dimensions, check the explained variance ratio to assess how much information is retained.

### 4. Choosing and Applying a Clustering Algorithm
- **Gaussian Mixture Model (GMM)** is recommended for clustering, but you’re free to use other clustering algorithms.
- Set the number of clusters to 5, as there are 5 flower types in the dataset. However, feel free to experiment with different numbers if you prefer.

### 5. Model and Feature Extraction (Flexible)
- You are free to choose the model and algorithm to use for clustering the images.
- For **feature extraction**, use any model of your choice. **PCA is optional**; you may experiment with other feature extraction methods.

### Evaluating Results
Measure the similarity between your clusters and the original dataset based on the criteria defined above, and calculate your score accordingly. The similarity score between your clusters and the original classes in the flower dataset will determine your final score.

## Submission Requirements
- **Clustered Data Folders**: Prepare your output folder with one subfolder for each cluster. The folder structure should allow easy comparison with the original dataset.
- **Notebook or Script File**: Submit a Jupyter notebook (`.ipynb`) or Python script (`.py`) explaining the entire process. Your code should be clear and well-documented.
- **Results Report (Optional)**: You may include a brief report summarizing your results. Mention the similarity percentage achieved and your total score. You can also discuss any challenges encountered during clustering and suggest potential improvements.
