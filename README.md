# quant-simulations
Python implementations of quantitative finance simulations, statistical modeling, and algorithmic problem solving.
# Quantitative Simulations & Financial Modeling

This repository contains Python scripts focused on statistical simulations, probability distributions, and financial data analysis. These projects were built to practice mathematical modeling and data manipulation, which are fundamental for Quantitative Trading and HFT roles.

## Projects Included

### 1. Random Walk Market Simulation (`random_walk_simulation.py`)
A Monte Carlo simulation of a financial asset's price movement over time.
- **Concepts Used:** Stochastic processes, normal distribution (`numpy.random.normal`), statistical analysis (mean, standard deviation, max/min), and data visualization with `matplotlib`.
- **Purpose:** To understand the random nature of financial markets and practice statistical modeling.

### 2. Poisson Sports Model (`poisson_sports_model.py`)
A probabilistic simulation of football match outcomes using the Poisson distribution.
- **Concepts Used:** Probability distributions (`numpy.random.poisson`), multidimensional arrays, and simulating random events based on statistical means.
- **Purpose:** To apply probability theory to real-world event modeling and data generation.

### 3. Housing Data Analysis (`housing_data_analysis.py`)
A data analysis script exploring the California Housing dataset.
- **Concepts Used:** Data manipulation with `pandas`, handling missing values, feature engineering (e.g., rooms per person), and geospatial data visualization using `matplotlib`.
- **Purpose:** To practice data cleaning, exploration, and extracting insights from large datasets.
- *Note: The `californiahouse.csv` dataset is required to run this script. If the file is not present due to size limits, the script will need to be pointed to the correct local path or a public URL.*

## Requirements
To run these scripts, you will need Python 3 and the following libraries:
```bash
pip install numpy pandas matplotlib
