"""model_training.py
Script to train a selected Surprise model on the full dataset and persist it.
"""
import joblib
from surprise import SVD
from surprise.model_selection import train_test_split

def train_and_save(algo_class, dataset, model_path, **algo_kwargs):
    trainset = dataset.build_full_trainset()
    algo = algo_class(**algo_kwargs)
    algo.fit(trainset)
    # Save using joblib: Surprise algorithms are pickleable
    joblib.dump(algo, model_path)
    return algo
