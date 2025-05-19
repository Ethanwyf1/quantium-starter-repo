# Quantium Price Impact Visualiser

An interactive dashboard built using Dash and Python to analyse the impact of **Pink Morsel** price changes on sales. Developed as part of the **Quantium Software Engineering Job Simulation** on Forage.

This project demonstrates data cleaning, dynamic data visualisation, user interaction design, testing automation, and CI-ready engineering practices.

---

## Overview

- Cleaned and transformed raw transaction data using `data_munger.py`
- Built an interactive line chart showing sales trends with event markers
- Added region filters (North, East, South, West, All) to support exploratory analysis
- Implemented a vertical dashed line to highlight the price change date
- Wrote automated tests using `pytest` and `dash[testing]`
- Created a Bash script to support CI-style test execution

---

## Tech Stack

- **Language:** Python 3.9
- **Frameworks:** Dash, Plotly, Pandas
- **Testing:** Pytest, Dash Testing
- **Automation:** Bash, CI-compatible
- **Deployment:** Local server (Dash built-in)

---

## Project Structure

```
quantium-starter-repo/
├── app.py               # Dash application entry point
├── data_munger.py       # Data cleaning script
├── formatted_data.csv   # Cleaned sales data
├── data/                # Raw CSV input files
├── test_app.py          # Pytest UI tests
├── run_tests.sh         # Bash script for automated testing
└── requirements.txt     # Python dependencies
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ethanwyf1/quantium-starter-repo.git
cd quantium-starter-repo
```

### 2. Set up and activate virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# or: source .venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

### 3. Run the app locally

```bash
python app.py
```

Then open [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your browser.

---

## Run Tests

```bash
./run_tests.sh
```

This command activates your virtual environment and runs all UI tests.

---

## Features

- Interactive line chart with hover tooltips and annotations
- Region filter for comparative analysis
- Modular Dash architecture (data → layout → callback)
- Automated UI testing with `pytest`
- CI-compatible test runner script