# AI-Powered Smart Energy Consumption Prediction

## Project Overview

This project predicts household appliance energy consumption using machine learning. It uses environmental sensor readings, weather conditions, lighting usage, and time-based features to estimate energy consumption and support smarter energy management.

The project follows a complete machine learning workflow consisting of:

* Dataset selection and preprocessing
* Feature engineering
* Exploratory Data Analysis (EDA)
* Regression model training
* Model evaluation and comparison
* Cross-validation
* Final model selection

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

## Project Structure

```text
AI-Powered-Smart-Energy-Consumption-Prediction/
│
├── notebooks/
│   ├── Task_1_Dataset_Selection_and_Preprocessing.ipynb
│   ├── Task_2_Feature_Engineering_and_EDA.ipynb
│   └── Task_3_Model_Training_and_Evaluation.ipynb
│
├── data/
│   ├── energydata_complete.csv
│   └── energy_preprocessed.csv
│
├── reports/
│   └── One_Page_Report_Dataset_Selection_and_Preprocessing.pdf
│
└── README.md
```

---

## Technologies and Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Git
* GitHub

---

## Installation

Clone the repository:

```bash
git clone (https://github.com/SaribShahid/Smart-Energy-Consumption-Prediction.git)
```

Move into the project directory:

```bash
cd AI-Powered-Smart-Energy-Consumption-Prediction
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## How to Run

1. Clone or download the repository.
2. Install the required Python libraries.
3. Open the project folder in **Jupyter Notebook**, **Google Colab**, or **Visual Studio Code**.
4. Run the notebooks in the following order:

```text
1. Task_1_Dataset_Selection_and_Preprocessing.ipynb
2. Task_2_Feature_Engineering_and_EDA.ipynb
3. Task_3_Model_Training_and_Evaluation.ipynb
```

5. Run each notebook from top to bottom.

> Make sure that `energy_preprocessed.csv` is available in the `data/` folder before running the Task 2 and Task 3 notebooks.

---

## Repository Contents

* **notebooks/** – Contains notebooks for preprocessing, feature engineering, EDA, model training, and evaluation.
* **data/** – Contains the original and preprocessed datasets.
* **reports/** – Contains project reports.
* **README.md** – Contains project documentation, methodology, results, and execution instructions.

---

## Future Improvements

Possible improvements include:

* Hyperparameter tuning using `GridSearchCV` or `RandomizedSearchCV`
* Adding more relevant features
* Performing additional feature selection
* Testing Random Forest Regressor
* Testing Gradient Boosting Regressor
* Improving prediction accuracy through advanced feature engineering
* Deploying the trained model as a web application or REST API
* Creating an interactive dashboard for energy consumption predictions

---

## Author

**Sarib Shahid**

BS Computer Science
University of Central Punjab
