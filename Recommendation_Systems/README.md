# 🚀 Hybrid Recommender System Portfolio: Cold Start to Personalization

## Project Overview

This repository showcases a comprehensive, multi-stage recommender system built to address the three core challenges in content discovery: **general popularity ranking, cold start problems, and personalized rating prediction.**

The final output is a **Hybrid Switching Model (File 04)** that intelligently combines the strengths of three different algorithms to ensure maximum coverage and high accuracy for all users, regardless of their interaction history.

## 💡 System Architecture: The Switching Hybrid

The final system uses a **Switching Hybrid** approach:

1.  **Priority (Known Users):** If a user has sufficient interaction history, the **Collaborative Filtering (SVD)** engine provides personalized predictions.
2.  **Fallback (Cold Start):** If the user is new or lacks history, the system defaults to the **Content-Based Model** for contextual recommendations, or the **Weighted Ranking** for general discovery.

## 📊 Models Implemented

| File | Model Type | Core Problem Solved | Key Deliverable |
| :--- | :--- | :--- | :--- |
| `01_Ranking_Engine.ipynb` | Weighted Ranking | **General Discovery/Initial Fallback** | Robust Top-N list (IMDb formula) |
| `02_Content_Based_Engine.ipynb` | Content-Based Filtering | **New Users/Item Cold Start** | Cosine Similarity Matrix |
| `03_Collaborative_Filtering.ipynb` | Matrix Factorization (SVD/KNN) | **Personalized Rating Prediction** | Benchmarking and lowest RMSE model selection |
| `04_Hybrid_Switching_Model.ipynb` | **System Fusion** | **System Robustness & Full Coverage** | The integrated switching logic function |

## 🛠️ Technical Stack & Dependencies

The project is implemented in Python and relies on specialized libraries for data manipulation and recommendation algorithms.

To install dependencies, run: `pip install -r requirements.txt`

## ⚙️ Repository Setup

1. **Data:** All CSV files must be located inside the `data/` directory.
2. **Large Files:** The `ratings.csv` file is managed using **Git LFS** (Large File Storage). Ensure Git LFS is installed before cloning to download the data correctly.
