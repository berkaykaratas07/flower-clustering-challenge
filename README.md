# Flower Clustering Challenge 🌸

Welcome to the **Flower Clustering Challenge**! This project challenges you to develop machine learning techniques to cluster flower images based on their similarities. Your goal is to create a model that effectively groups the images to replicate the original categories as closely as possible.

## Overview
In this challenge, participants are provided with an enhanced version of the popular flower dataset. The dataset has been modified to increase complexity, making the clustering task more challenging and realistic for machine learning applications. The challenge is designed to encourage exploration in feature extraction, dimensionality reduction, and clustering algorithms.

## Dataset
The dataset is hosted on Kaggle. You can download it using the following link:

[Enhanced Flower Dataset for Clustering Challenges](https://www.kaggle.com/datasets/berkaykaratas/enhanced-flower-dataset-for-clustering-challenges/data)

The dataset includes pre-extracted features to simplify the workflow and allow participants to focus on clustering methods.

## Challenge Guide
For detailed instructions on how to approach the challenge, refer to the `CHALLENGE_GUIDE.md` file in this repository. The guide includes:
- **Challenge Goals and Success Criteria**
- **Scoring System**
- **Recommended Performance Metrics**
- **Step-by-Step Instructions**
- **Submission Requirements**

Make sure to read the `CHALLENGE_GUIDE.md` file to understand the challenge criteria and the steps you need to follow.

## Project Structure
- `model/`: Contains pre-extracted features from popular models. Use these features to streamline your clustering process.
- `notebooks/`: Contains the example notebook for setting up your workflow.
- `CHALLENGE_GUIDE.md`: Detailed instructions for the challenge.
- `requirements.txt`: List of dependencies for the project.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/berkaykaratas07/flower-clustering-challenge.git
   cd flower-clustering-challenge
   ```

2. **Install dependencies:** Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Download the dataset:**
  - Go to the Enhanced Flower Dataset on Kaggle.
  - Download the dataset and place it in the model/ folder.

4. **Explore the Example Notebook:**
  - Open the notebook in the notebooks/ folder for a guided example on setting up your clustering workflow.

## Suggested Workflow
- **Data Preprocessing**: Use the provided pre-extracted features or experiment with your feature extraction methods.
- **Dimensionality Reduction (Optional)**: Apply techniques like PCA to reduce dimensionality if desired.
- **Clustering Model**: Experiment with clustering algorithms, such as Gaussian Mixture Models (GMM) or K-means.
- **Evaluation**: Measure the effectiveness of your clusters using metrics such as Silhouette Score or by comparing with the original categories.

For further details, please refer to the `CHALLENGE_GUIDE.md` file.

## Scoring and Evaluation
Participants will be evaluated based on the similarity between their clusters and the original dataset categories. The scoring system is detailed in the `CHALLENGE_GUIDE.md` file.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
