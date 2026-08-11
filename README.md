# AI-Powered Smart Energy Consumption Prediction

## Project Overview

This project predicts household appliance energy consumption using machine learning. It uses environmental sensor readings, weather conditions, lighting usage, and time-based features to estimate energy consumption and support smarter energy management.

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

## Task 4: Deployment Preparation

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

### Streamlit Application (Initial Version)

A simple Streamlit web application was developed to demonstrate the deployment workflow.

The initial application allowed users to:

- Enter feature values
- Load the trained model
- Predict household appliance energy consumption instantly

This demonstrated the complete prediction pipeline and served as the initial deployment interface, which was later expanded in Task 5.

---

## Task 5: Complete Application and Deployment

The final implementation phase focused on completing and demonstrating the fully deployed machine learning application.

The trained model was integrated into a functional Streamlit web application that provides an end-to-end prediction system.

### Complete Application

The final application loads the serialized machine learning model and generates predictions based on user-provided input.

The application does not retrain the model during prediction. Instead, it loads:

```text
models/energy_model.joblib
```

The application then processes the input data and passes it to the trained model to generate the predicted appliance energy consumption.

### User Input Options

The application provides multiple input methods so users can choose how they want to provide prediction data.

**1. Manual Input**

Users can manually enter the required feature values through the Streamlit interface. The application processes these values and generates the predicted appliance energy consumption.

**2. CSV File Upload**

Users can upload a CSV file containing the required input features. The application:

- Accepts the uploaded CSV file
- Reads the data using Pandas
- Validates the required features
- Passes the data to the trained model
- Generates predictions
- Displays the prediction results

This allows users to perform predictions using prepared datasets instead of entering values manually.

**3. Excel File Upload**

The application also supports Excel files. Users can upload an `.xlsx` file containing the required input features. The application reads the Excel file, processes the input data, and generates predictions using the trained model. The Excel functionality uses the `openpyxl` library for reading `.xlsx` files.

### Required Input Features

The application accepts/requires the following features for prediction:

```
lights, T1, RH_1, T2, RH_2, T3, RH_3, T4, RH_4, T5, RH_5, T6, RH_6,
T7, RH_7, T8, RH_8, T9, RH_9, T_out, Press_mm_hg, RH_out, Windspeed,
Visibility, Tdewpoint, Year, Month, Day, Hour, Minute, DayOfWeek, IsWeekend
```

### Prediction Workflow

```text
User
  │
  ├── Manual Input
  │
  ├── CSV File
  │
  └── Excel File
        │
        ▼
   Input Validation
        │
        ▼
   Pandas DataFrame
        │
        ▼
   Feature Preparation
        │
        ▼
   Load Serialized Model
        │
        ▼
   Lasso Regression Model
        │
        ▼
   Generate Prediction
        │
        ▼
   Display Energy Consumption
```

This demonstrates a complete end-to-end machine learning prediction system.

### User Interface

The Streamlit application provides separate sections/tabs for different input methods. Users can select the required input method without being required to use all input methods at the same time.

The interface is designed to keep the prediction process simple:

```text
Manual Input                       CSV / Excel Upload
     │                                    │
     └── Enter values                     └── Upload file
             │                                    │
             ▼                                    ▼
          Predict                           Validate Data
             │                                    │
             ▼                                    ▼
      Prediction Result                     Predict
                                                   │
                                                   ▼
                                          Prediction Results
```

This prevents users from becoming confused about which input method they should use.

### Application Output

The application displays the predicted appliance energy consumption after a successful prediction.

Example:

```text
Predicted Energy Consumption: 17.52 Wh
```

For uploaded files containing multiple records, the application can generate predictions for all provided input rows.

### Input Validation

The application validates uploaded files before making predictions. It checks whether all required model features are available. If required columns are missing, the application informs the user instead of attempting to generate an invalid prediction.

### Final Application Features

The completed application provides:

- Trained machine learning model integration
- Serialized model loading using Joblib
- Manual feature input
- CSV file upload
- Excel file upload
- Input validation
- Prediction generation
- Prediction results display
- Streamlit-based user interface
- End-to-end machine learning workflow

---

## Final Project Structure

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

---

## Technologies and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- OpenPyXL
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

If the serialized model is not already available, run:

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

The application will open in your browser. Users can then choose between manual input or CSV/Excel file upload and generate appliance energy consumption predictions.

---

## Requirements

The project dependencies are maintained in `requirements.txt`. The main dependencies include:

```text
pandas
numpy
scikit-learn
joblib
streamlit
openpyxl
matplotlib
seaborn
```

---

## Repository Contents

- **app/** – Streamlit application and supporting prediction modules.
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
- Add prediction history.
- Add interactive energy consumption visualizations and analytics.
- Add downloadable prediction results.
- Add authentication for application users.
- Add monitoring and logging for deployed predictions.

---

## Conclusion

This project demonstrates a complete machine learning development lifecycle, from dataset preprocessing and exploratory analysis to model training, evaluation, serialization, and application deployment.

The final Streamlit application provides users with multiple ways to provide prediction data — manual input, CSV upload, and Excel upload — and generates appliance energy consumption predictions using the trained Lasso Regression model.

The project therefore demonstrates an end-to-end machine learning system that is structured, reusable, documented, and prepared for further deployment and enhancement.

---

## Author

**Sarib Shahid**

BS Computer Science
University of Central Punjab
