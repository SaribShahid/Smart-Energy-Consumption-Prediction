# AI-Powered Smart Energy Consumption Prediction

## Project Overview

This project predicts household appliance energy consumption using machine learning. It utilizes environmental sensor readings, weather conditions, lighting usage, and time-based features to forecast future electricity consumption, helping improve energy efficiency in smart homes.

---

## Problem Statement

Many households consume electricity inefficiently because future energy usage cannot be accurately predicted. This project develops a machine learning regression model that predicts appliance energy consumption to support smarter energy management and reduce unnecessary electricity usage.

---

## Dataset

**Dataset:** Appliance Energy Prediction Dataset

**Source:** Kaggle

**Dataset Link:**[ https://www.kaggle.com/datasets/loveall/appliances-energy-predictions](https://www.kaggle.com/code/gaganmaahi224/appliances-energy-time-series-analysis/input)

**Dataset Information**

* Rows: 19,735
* Columns: 29
* Target Variable: `Appliances`
* Problem Type: Regression

---

## Project Structure

```text
Energy-Consumption-Prediction-ML/
│
├── notebooks/
│   └── Task_1_Dataset_Selection_and_Preprocessing.ipynb
│
├── data/
│   ├── energydata_complete.csv
│   └── energy_preprocessed.csv
│
├── reports/
│   └── One_Page_ReportOne_Page_Report_Dataset_Selection_and_Preprocessing.pdf
└── README.md
```

---

## Preprocessing Steps

The following preprocessing steps were completed:

* Dataset exploration
* Dataset dimension analysis
* Feature analysis
* Data type inspection
* Statistical summary generation
* Missing value analysis
* Duplicate record analysis
* Outlier detection using the IQR method
* Feature engineering from the `date` column
* Removal of random features (`rv1` and `rv2`)
* Feature scaling using StandardScaler

Since this is a regression problem, class imbalance analysis and SMOTE-Tomek were not applicable.

---

## Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## How to Run the Notebook

1. Clone this repository.
2. Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

3. Open `Task_1_Dataset_Selection_and_Preprocessing.ipynb` in Jupyter Notebook or VS Code.
4. Run the notebook from top to bottom.

---

## Repository Contents

* **notebooks/** – Jupyter Notebook containing dataset selection and preprocessing.
* **data/** – Original and preprocessed datasets.
* **reports/** – One-page project report in PDF format.
* **README.md** – Project documentation and execution instructions.

---

## Author

**Sarib Shahid**

BS Computer Science

University of Central Punjab
