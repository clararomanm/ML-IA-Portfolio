"""utils.py
Helper functions for the project.
"""
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
