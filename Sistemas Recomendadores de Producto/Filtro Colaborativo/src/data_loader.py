"""data_loader.py
Utilities to load and preprocess rating datasets for the recommender pipeline.
"""
import pandas as pd
from surprise import Dataset, Reader

def load_ratings_csv(path, user_col='userId', item_col='itemId', rating_col='rating', sample=None):
    """Load ratings from a CSV into a pandas DataFrame and optionally sample."""
    df = pd.read_csv(path)
    if sample is not None:
        df = df.sample(n=sample, random_state=42)
    return df[[user_col, item_col, rating_col]].rename(columns={user_col:'userId', item_col:'itemId', rating_col:'rating'})

def surprise_dataset_from_df(df):
    """Convert a pandas DataFrame with columns userId,itemId,rating into a Surprise Dataset."""
    reader = Reader(rating_scale=(df.rating.min(), df.rating.max()))
    return Dataset.load_from_df(df[['userId','itemId','rating']], reader)
