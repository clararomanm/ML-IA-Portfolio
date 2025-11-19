"""model_selection.py
Compare multiple Surprise algorithms using cross-validation to choose the best model.
"""
from surprise import SVD, KNNBasic, BaselineOnly
from surprise.model_selection import cross_validate

ALGORITHMS = {
    'SVD': SVD,
    'KNNBasic': KNNBasic,
    'BaselineOnly': BaselineOnly
}

def benchmark(algo_classes, data, measures=['rmse','mae'], cv=3, verbose=True):
    results = {}
    for name, Algo in algo_classes.items():
        algo = Algo()
        res = cross_validate(algo, data, measures=measures, cv=cv, verbose=verbose, n_jobs=1)
        results[name] = res
    return results
