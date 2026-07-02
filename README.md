# Hyperspace

🚀 Hyperspace

Calculate realistic hyperspace travel times in the Star Wars galaxy using machine learning and galactic geography.

🌌 Project Overview

Hyperspace is a data science project that predicts travel times between planets in the Star Wars galaxy.

Instead of relying on arbitrary distances, the project combines:

* Galactic coordinates
* Hyperlanes
* Sector and region information
* Navigation difficulty  republic era, imperial era, new republic era
* Machine Learning models

The goal is to estimate how long a hyperspace jump would take while remaining consistent with Star Wars lore.

⸻

📖 Motivation

In Star Wars, hyperspace travel is rarely consistent.

Sometimes planets separated by half the galaxy are reached in hours, while other trips take days.

This project attempts to build a reproducible model capable of estimating travel times from known journeys and galactic data.

📂 Project Structure

Hyperspace/
│
├── raw/                  # Original datasets source : kaggle
├── processed/            # Cleaned datasets
├── notebooks/            # Exploration notebooks
├── models/               # Trained ML models
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app/                  # Web application
├── tests/
└── README.md

🛰 Dataset

The project combines several datasets:

* Star Wars planets
* Hyperlanes
* Galactic regions

After preprocessing:

* Planet IDs
* Coordinates
* Region
* Sector
* System
* Population
* Capital
* Navigation information

⸻

⚙️ Data Cleaning

The preprocessing pipeline:

* removes duplicated planets
* normalizes sector names
* splits galactic coordinates
* assigns unique IDs
* removes planets with unknown coordinates
* validates coordinate formats

⸻

🧠 Machine Learning

Current experiments include:

* Linear Regression
* Random Forest
* Gradient Boosting
* XGBoost (planned)
* Neural Networks (planned)

Features include:

* Euclidean distance
* Manhattan distance
* Hyperlane proximity
* Core / Mid Rim / Outer Rim
* Navigation factor

📅 Roadmap

* ✅ Clean planet dataset
* ✅ Coordinate normalization
* ⬜ Hyperlane graph
* ⬜ Route finding
* ⬜ ML prediction model
* ⬜ Web interface
* ⬜ Interactive galactic map
* ⬜ API
* ⬜ Docker deployment

⸻

🎯 Future Improvements

* Use graph algorithms (A*)
* Integrate canon/Legends switch
* Multiple route optimization
* Explainable AI
* Confidence intervals
* Real-time interactive galaxy map

⸻

📚 Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* NetworkX
* Plotly
* Streamlit (future)
* Docker

⸻

📜 License

MIT License

➡️ overall proccess

Data Collecting
        ↓
Cleaning
        ↓
Feature Engineering
        ↓
Machine Learning
        ↓
Évaluation
        ↓
Déploiement

🚀 Pipeline

             planets.csv
                  │
                  ▼
        Data Cleaning Pipeline
                  │
                  ▼
      Feature Engineering
                  │
                  ▼
      Machine Learning Model
                  │
                  ▼
      Hyperspace Calculator
                  │
                  ▼
          Web Application
