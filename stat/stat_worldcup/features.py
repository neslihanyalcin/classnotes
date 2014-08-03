
"""
    Turns raw statistics about soccer matches into features we use
    for prediction. Combines a number of games of history to compute
    aggregates that can be used to predict the next game.
"""

import pandas as pd

import match_stats

def get_wc_features(history_size):
    return pd.read_csv('results-20140714-123022.csv',sep=',')

def get_features(history_size):
    return pd.read_csv('results-20140714-123519.csv',sep=',')

def get_game_summaries():
    return pd.read_csv('results-20140714-124014.csv',sep=',')

