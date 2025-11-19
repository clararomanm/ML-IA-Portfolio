"""recommendation_engine.py
Utilities to generate top-N recommendations for a user from a trained Surprise model.
"""
import pandas as pd

def get_top_n_recommendations(algo, trainset, all_items, user_raw_id, n=10):
    """Return top-n item ids for a given user_raw_id not present in his trainset interactions."""
    # Convert raw ids to inner ids to check known items
    try:
        user_inner = trainset.to_inner_uid(user_raw_id)
    except ValueError:
        # new user: score all items
        user_inner = None

    # items user has rated
    known_items = set([trainset.to_raw_iid(iid) for iid in trainset.ur[user_inner]]) if user_inner is not None else set()

    candidates = [iid for iid in all_items if iid not in known_items]
    predictions = []
    for iid in candidates:
        est = algo.predict(user_raw_id, iid).est
        predictions.append((iid, est))
    predictions.sort(key=lambda x: x[1], reverse=True)
    topn = [iid for iid, _ in predictions[:n]]
    return topn
