# AI-Powered Smart Energy Consumption Prediction

## Project Overview

This project predicts household appliance energy consumption using machine learning. It uses environmental sensor readings, weather conditions, lighting usage, and time-based features to estimate energy consumption and support smarter energy management.

The project follows a complete machine learning workflow consisting of:

The project follows a complete machine learning workflow consisting of:

- Dataset selection and preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Regression model training
- Model evaluation and comparison
- Cross-validation
- Final model selection
- Model serialization using Joblib
- Deployment-ready Streamlit application

---

## Problem Statement

Households may consume electricity inefficiently because future energy usage is difficult to predict accurately. This project develops machine learning regression models to predict household appliance energy consumption based on environmental, weather, lighting, and time-related features.

The predicted energy consumption can support smarter energy management, improve energy efficiency, and help reduce unnecessary electricity usage.

---

## Dataset

**Dataset:** Appliance Energy Prediction Dataset

**Source:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/loveall/appliances-energy-predictions

### Dataset Information

* **Rows:** 19,735
* **Columns:** 29
* **Target Variable:** `Appliances`
* **Problem Type:** Regression

The dataset contains information related to:

* Indoor temperature and humidity
* Weather conditions
* Lighting usage
* Date and time information
* Household appliance energy consumption

---

# Project Tasks

## Task 1: Dataset Selection and Preprocessing

The dataset was explored, cleaned, and prepared for machine learning model development.

The following preprocessing steps were performed:

* Dataset exploration
* Dataset dimension analysis
* Feature analysis
* Data type inspection
* Statistical summary generation
* Missing value analysis
* Duplicate record analysis
* Outlier detection using the IQR method
* Date and time feature extraction
* Removal of irrelevant random features (`rv1` and `rv2`)
* Feature scaling using `StandardScaler`
* Saving the processed dataset

Since this project is a regression problem with a continuous target variable, class imbalance analysis and SMOTE-Tomek were not applicable.

---

## Task 2: Feature Engineering and Exploratory Data Analysis

Feature engineering and exploratory data analysis were performed to improve the dataset representation, understand feature relationships, and identify important patterns before model development.

### Feature Engineering

The original `date` column was transformed into the following numerical features:

* `Year`
* `Month`
* `Day`
* `Hour`
* `Minute`
* `DayOfWeek`
* `IsWeekend`

These features allow machine learning models to capture temporal patterns in appliance energy consumption. For example, energy usage may vary depending on the hour of the day, the day of the week, or whether the observation occurred on a weekend.

### Feature Transformation

Feature scaling was performed using `StandardScaler`.

Since the dataset contains numerical variables with different ranges, such as temperature, humidity, pressure, and wind speed, scaling was applied to bring the features to a comparable scale.

### Feature Selection and Analysis

The following feature analysis techniques were used:

* Correlation analysis
* Correlation heatmap
* Variance Threshold
* Mutual Information analysis
* Removal of irrelevant random features (`rv1` and `rv2`)

Correlation analysis was used to identify relationships between numerical features and the target variable.

Variance Threshold was used to identify features with very low variability.

Mutual Information was used to evaluate how much information each feature provides for predicting appliance energy consumption.

### Exploratory Data Analysis

The following visualizations were created:

* Histograms
* KDE plot
* Count plots
* Box plots
* Pair plots
* Scatter plots
* Target variable distribution
* Correlation heatmap

These visualizations were used to analyze:

* Feature distributions
* Skewness
* Potential outliers
* Relationships between variables
* Temporal feature distributions
* Relationships between input features and appliance energy consumption

### Non-Applicable Techniques

The following techniques were not applicable:

* **Text Feature Extraction:** The dataset contains numerical and date-related features and does not contain text attributes.
* **Class-wise Comparison Plots:** The project is a regression problem with a continuous target variable (`Appliances`), so there are no classes to compare.

---

## Task 3: Model Training and Evaluation

The processed dataset was used to train and compare the following regression models:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression

The dataset was divided into:

* **Training Data:** 80%
* **Testing Data:** 20%

The models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score
* 5-Fold Cross-Validation

---

## Model Performance

| Model                |         MAE |        RMSE |     R² Score | Average Cross-Validation R² |
| -------------------- | ----------: | ----------: | -----------: | --------------------------: |
| Linear Regression    |     52.6161 |     91.1071 |     0.170538 |                    0.115297 |
| Ridge Regression     |     52.6157 |     91.1070 |     0.170540 |                    0.115305 |
| **Lasso Regression** | **52.6106** | **91.1064** | **0.170550** |                **0.115403** |

---

## Best-Performing Model

**Lasso Regression** was selected as the final model because it achieved:

* The lowest MAE
* The lowest RMSE
* The highest R² score
* The highest average cross-validation R² score

Although Lasso Regression performed slightly better, the differences between the three models were very small. This indicates that all three regression models showed similar performance on the dataset.

The relatively low R² scores suggest that the current features explain only a limited portion of the variation in appliance energy consumption. Future improvements may include additional feature engineering, hyperparameter tuning, and testing advanced regression models.

---

# Task 4: Deployment Preparation

The fourth implementation phase focuses on transforming the trained machine learning model into a deployment-ready application.

The notebook implementation was converted into reusable Python modules following a clean and modular project structure.

### Python Modules

The project was organized into the following modules:

- **preprocess.py** – Data preprocessing pipeline
- **feature_engineering.py** – Feature engineering functions
- **train_model.py** – Model training and serialization
- **model_loader.py** – Loads the saved model
- **prediction.py** – Prediction pipeline
- **app.py** – Streamlit web application

### Model Serialization

The best-performing **Lasso Regression** model was serialized using **Joblib**.

Instead of retraining the model each time, the application loads the saved model from:

```text
models/energy_model.joblib
```

This significantly reduces application startup time and makes the project deployment-ready.

### Streamlit Application

A simple Streamlit web application was developed to demonstrate the deployment workflow.

The application allows users to:

- Enter feature values
- Load the trained model
- Predict household appliance energy consumption instantly

This demonstrates the complete prediction pipeline and serves as the initial deployment interface.

## Project Structure

```text
Smart-Energy-Consumption-Prediction/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── model_loader.py
│   └── prediction.py
│
├── data/
│   ├── energydata_complete.csv
│   └── energy_preprocessed.csv
│
├── models/
│   └── energy_model.joblib
│
├── notebooks/
│   ├── Task_1_Dataset_Selection_and_Preprocessing.ipynb
│   ├── Task_2_Feature_Engineering_and_EDA.ipynb
│   └── Task_3_Model_Training_and_Evaluation.ipynb
│
├── reports/
│   └── One_Page_Report_Dataset_Selection_and_Preprocessing.pdf
│
├── train_model.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

## Technologies and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SaribShahid/Smart-Energy-Consumption-Prediction.git
```

Move into the project directory:

```bash
cd Smart-Energy-Consumption-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/SaribShahid/Smart-Energy-Consumption-Prediction.git
```

### Step 2: Navigate to the project

```bash
cd Smart-Energy-Consumption-Prediction
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train the model

```bash
py train_model.py
```

This creates:

```text
models/energy_model.joblib
```

### Step 5: Launch the Streamlit application

```bash
py -m streamlit run app/app.py
```

The application opens in your browser where users can enter feature values and obtain appliance energy consumption predictions.

---
## Repository Contents

- **app/** – Streamlit application and prediction modules.
- **data/** – Original and preprocessed datasets.
- **models/** – Serialized trained machine learning model.
- **notebooks/** – Original implementation notebooks.
- **reports/** – Project reports and documentation.
- **train_model.py** – Model training and model serialization script.
- **requirements.txt** – Project dependencies.
- **README.md** – Complete project documentation.
- **LICENSE** – MIT License.
- **.gitignore** – Git ignore configuration.

---

## Future Improvements

- Improve feature engineering for higher prediction accuracy.
- Perform hyperparameter tuning using GridSearchCV or RandomizedSearchCV.
- Evaluate advanced regression models such as Random Forest, XGBoost, and Gradient Boosting.
- Deploy the application on Streamlit Community Cloud.
- Develop a REST API using FastAPI.
- Support batch prediction using CSV file uploads.
- Add interactive visualizations and energy consumption analytics.

---

## Author

**Sarib Shahid**

BS Computer Science
University of Central Punjab
