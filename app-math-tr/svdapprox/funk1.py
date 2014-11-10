# Requires Movielens 100k data 
from scipy.io import mmread, mmwrite
import numpy as np, time, sys
from numba import jit
import os

def get_user_ratings(user_id, review_matrix):
    """
    Returns a numpy array with the ratings that user_id has made

    :rtype : numpy array
    :param user_id: the id of the user
    :return: a numpy array with the ratings that user_id has made
    """
    user_reviews = review_matrix[user_id]
    user_reviews = user_reviews.toarray().ravel()
    user_rated_movies, = np.where(user_reviews > 0)
    user_ratings = user_reviews[user_rated_movies]
    return user_ratings

def get_movie_ratings(movie_id, review_matrix):
    """
    Returns a numpy array with the ratings that movie_id has received

    :rtype : numpy array
    :param movie_id: the id of the movie
    :return: a numpy array with the ratings that movie_id has received
    """
    movie_reviews = review_matrix[:, movie_id]
    movie_reviews = movie_reviews.toarray().ravel()
    movie_rated_users, = np.where(movie_reviews > 0)
    movie_ratings = movie_reviews[movie_rated_users]
    return movie_ratings

def calculate_global_average(review_matrix):
    all_reviews = review_matrix.toarray().ravel()
    average = np.average(all_reviews, weights=(all_reviews > 0))
    return average

def compute_averages(A, user_pseudo_average_ratings, movie_pseudo_average_ratings, global_average):

    """
    Calculates the pseudo averages for every user and movie and stores the
    values in user_pseudo_average_ratings and
    movie_pseudo_average_ratings arrays respectively. This is done
    previous to the training of the data in order to save time
    (the averages are stored in cache).

    :rtype : void
    """
    AA = A.tocsr()
    for user in range(len(user_pseudo_average_ratings)):
        user_pseudo_average_ratings[user] = \
            calculate_pseudo_average_user_rating(user, AA, global_average)

    for movie in range(len(movie_pseudo_average_ratings)):
        movie_pseudo_average_ratings[movie] = \
            calculate_pseudo_average_movie_rating(movie, AA, global_average)

def create_user_feature_matrix(review_matrix, NUM_FEATURES, FEATURE_INIT_VALUE):
    """
    Creates a user feature matrix of size NUM_FEATURES X NUM_USERS
    with all cells initialized to FEATURE_INIT_VALUE

    :rtype : numpy matrix
    :return: a matrix of size NUM_FEATURES X NUM_USERS
    with all cells initialized to FEATURE_INIT_VALUE
    """
    num_users = review_matrix.shape[0]
    user_feature_matrix = np.empty((NUM_FEATURES, num_users))
    user_feature_matrix[:] = FEATURE_INIT_VALUE
    return user_feature_matrix

def create_movie_feature_matrix(review_matrix, NUM_FEATURES, FEATURE_INIT_VALUE):
    """
    Creates a user feature matrix of size NUM_FEATURES X NUM_MOVIES
    with all cells initialized to FEATURE_INIT_VALUE

    :rtype : numpy matrix
    :return: a matrix of size NUM_FEATURES X NUM_MOVIES
    with all cells initialized to FEATURE_INIT_VALUE
    """
    num_movies = review_matrix.shape[1]
    movie_feature_matrix = np.empty((NUM_FEATURES, num_movies))
    movie_feature_matrix[:] = FEATURE_INIT_VALUE
    return movie_feature_matrix

def calculate_pseudo_average_movie_rating(movie_id, review_matrix, global_average):
    """
    Calculates the weighted average of the movie ratings which deals with
    the cases where there are few ratings for a movie

    :rtype : float
    :param movie_id: the id of the movie
    :return: the weighted average of the movie ratings which deals with
    the cases where there are few ratings for a movie
    """
    movie_ratings = get_movie_ratings(movie_id, review_matrix)
    k = 25
    return (global_average * k + np.sum(movie_ratings)) / (
        k + np.size(movie_ratings))

def calculate_pseudo_average_user_rating(user_id, review_matrix, global_average):
    """
    Calculates the weighted average of the user ratings which deals with
    the cases where there are few ratings by a user

    :rtype : float
    :param user_id: the id of the user
    :return: the weighted average of the movie ratings which deals with
    the cases where there are few ratings by a user
    """
    user_ratings = get_user_ratings(user_id, review_matrix)
    k = 25
    return (global_average * k + np.sum(user_ratings)) / (
        k + np.size(user_ratings))


@jit(nopython=True)
def predict_rating(user_id, movie_id, user_feature_matrix, movie_feature_matrix):
    """
    Makes a prediction of the rating that user_id will give to movie_id if
    he/she sees it

    :rtype : float
    :param user_id: the id of the user
    :param movie_id: the id of the movie
    :return: a float in the range [1, 5] with the predicted rating for
    movie_id by user_id
    """
    rating = 1.
    for f in range(user_feature_matrix.shape[0]):
        rating += user_feature_matrix[f, user_id] * movie_feature_matrix[f, movie_id]
        
    # We trim the ratings in case they go above or below the stars range
    if rating > 5: rating = 5
    elif rating < 1: rating = 1
    return rating

@jit(nopython=True)
def sgd_inner(feature, A_row, A_col, A_data, user_feature_matrix, movie_feature_matrix, global_average, user_pseudo_average_ratings, movie_pseudo_average_ratings,NUM_FEATURES):
    K = 0.015
    LEARNING_RATE = 0.001
    squared_error = 0
    for k in range(len(A_data)):
        user_id = A_row[k]
        movie_id = A_col[k]
        rating = A_data[k]
        p = predict_rating(user_id, movie_id, user_feature_matrix, movie_feature_matrix)
        u_diff = user_pseudo_average_ratings[user_id] - global_average
        m_diff = movie_pseudo_average_ratings[movie_id] - global_average
        err = rating - global_average - u_diff - m_diff - p
            
        squared_error += err ** 2

        user_feature_value = user_feature_matrix[feature, user_id]
        movie_feature_value = movie_feature_matrix[feature, movie_id]
        user_feature_matrix[feature, user_id] += \
            LEARNING_RATE * (err * movie_feature_value - K * user_feature_value)
        movie_feature_matrix[feature, movie_id] += \
            LEARNING_RATE * (err * user_feature_value - K * movie_feature_value)

    return squared_error

def calculate_features(A_row, A_col, A_data, user_feature_matrix, movie_feature_matrix, global_average, user_pseudo_average_ratings, movie_pseudo_average_ratings,NUM_FEATURES):
    """
    Iterates through all the ratings in search for the best features that
    minimize the error between the predictions and the real ratings.
    This is the main function in Simon Funk SVD algorithm

    :rtype : void
    """
    MIN_IMPROVEMENT = 0.0001
    MIN_ITERATIONS = 100
    rmse = 0
    last_rmse = 0
    print len(A_data)
    num_ratings = len(A_data)
    for feature in xrange(NUM_FEATURES):
        iter = 0
        while (iter < MIN_ITERATIONS) or  (rmse < last_rmse - MIN_IMPROVEMENT):
            last_rmse = rmse
            squared_error = sgd_inner(feature, A_row, A_col, A_data, user_feature_matrix, movie_feature_matrix, global_average, user_pseudo_average_ratings, movie_pseudo_average_ratings,NUM_FEATURES)
            rmse = (squared_error / num_ratings) * 0.5
            iter += 1
        print ('Squared error = %f' % squared_error)
        print ('RMSE = %f' % rmse)
        print ('Feature = %d' % feature)
    return last_rmse


LAMBDA = 0.02
FEATURE_INIT_VALUE = 0.1
NUM_FEATURES = 20

A = mmread('%s/Downloads/A_ml' % os.environ['HOME'])

user_feature_matrix = create_user_feature_matrix(A, NUM_FEATURES, FEATURE_INIT_VALUE)
movie_feature_matrix = create_movie_feature_matrix(A, NUM_FEATURES, FEATURE_INIT_VALUE)
global_average = calculate_global_average(A)

users, movies = A.nonzero()
A = A.tocoo()

user_pseudo_average_ratings = np.array([np.nan for x in range(np.max(users)+1) ])
movie_pseudo_average_ratings = np.array([np.nan for x in range(np.max(movies)+1) ])

compute_averages(A, user_pseudo_average_ratings, movie_pseudo_average_ratings, global_average)
rmse = calculate_features(A.row, A.col, A.data, user_feature_matrix, movie_feature_matrix, global_average, user_pseudo_average_ratings, movie_pseudo_average_ratings, NUM_FEATURES )
print 'rmse', rmse
