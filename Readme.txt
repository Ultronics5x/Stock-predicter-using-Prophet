Stock-prediction-using-Time-series-and-Streamlit-for-frontend
The code provided is a Python script for disease prediction using different types of machine learning algorithms. Here's a summary of what the script does:

1. Import necessary libraries including Streamlit, pandas, numpy, matplotlib, nltk, and scikit-learn modules.
2. Creates a simple frontend using Streamlit for users to input medical issue descriptions.
3. Reads data from a CSV file containing symptom-disease mappings.
4. Cleans the text data by removing punctuation and stopwords using NLTK.
5. Visualizes frequent words in the dataset using a word cloud.
6. Splits the data into training and testing sets.
7. Implements text vectorization using TF-IDF (Term Frequency-Inverse Document Frequency).
8. Provides options for model selection including K-Nearest Neighbors (KNN), Support Vector Machines (SVM), Random Forest Classifier (RFC), and Neural Networks (NN).
9. Trains and evaluates the selected model on the dataset.
10. Makes predictions on custom test cases provided in the script.
11. Displays accuracy scores and classification reports for model evaluation.

Overall, the script provides a user-friendly interface for disease prediction based on symptom descriptions using various machine learning techniques.
