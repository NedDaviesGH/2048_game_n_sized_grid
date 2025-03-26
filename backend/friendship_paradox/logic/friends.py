import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from fh_matplotlib import matplotlib2fasthtml

def make_arr_symmetric(arr):
    return np.tril(arr) + np.triu(arr.T, 1)

def get_friends_matrix(size: int, normal: bool, popularity_mean = 0.5, popularity_std = 0.15):
    if normal:
        popularity_scores = np.random.normal(popularity_mean, popularity_std, size)
        popularity_scores = np.clip(popularity_scores, a_min=0, a_max=1)
    else:
        popularity_scores = np.random.rand(size)
        
    popularity_matrix = np.outer(popularity_scores, popularity_scores)

    rand_matrix = np.random.rand(size, size)
    friend_arr = (rand_matrix < popularity_matrix).astype(int)
    return friend_arr, popularity_scores

def make_friends(size: int, normal = False):
    friend_arr, popularity_scores = get_friends_matrix(size = size, normal = normal)
    friend_arr = make_arr_symmetric(friend_arr)
    np.fill_diagonal(friend_arr, 0)
    return friend_arr, popularity_scores

def create_friend_comparison(friend_arr):
    row_sums = np.sum(friend_arr, axis=1)
    all_friend_sums = []

    for row_ind in range(friend_arr.shape[0]):
        friend_indices = np.where(friend_arr[row_ind] == 1)[0]

        if len(friend_indices) > 0:
            friend_sums = row_sums[friend_indices]
            avg_friends = np.mean(friend_sums)
        else:
            avg_friends = 0

        all_friend_sums.append(avg_friends)

    return np.vstack((row_sums, all_friend_sums)).T

def calculate_friend_means(friend_comparisons):
    person_mean, friend_mean = friend_comparisons.mean(axis=0)
    return person_mean, friend_mean

@matplotlib2fasthtml
def plot_friend_matrix(friend_matrix):
    """
    Plots the friendship matrix as a heatmap.
    
    Parameters:
        friend_matrix (numpy.ndarray): A 2D array where each element indicates friendship (1 for friends, 0 otherwise).
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(friend_matrix, cmap="Blues", cbar=False, square=True, linewidths=0.5)
    plt.title("Friendship Matrix")
    plt.xlabel("Person")
    plt.ylabel("Person")


@matplotlib2fasthtml
def plot_popularity_distribution(popularities):
    """
    Plots the distribution of popularity scores (number of friends).
    
    Parameters:
        popularities (numpy.ndarray): An array where each element represents the number of friends a person has.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(popularities, bins=10, color="skyblue", edgecolor="black", alpha=0.7)
    plt.title("Popularity Distribution")
    plt.xlabel("Popularity Score")
    plt.ylabel("Frequency")



# def plot_to_base64(fig):
#     """
#     Converts a Matplotlib figure to a base64-encoded string.

#     Parameters:
#         fig (matplotlib.figure.Figure): The Matplotlib figure to convert.

#     Returns:
#         str: A base64-encoded string of the image.
#     """
#     buf = io.BytesIO()
#     fig.savefig(buf, format="png", bbox_inches="tight")
#     buf.seek(0)
#     img_base64 = base64.b64encode(buf.read()).decode("utf-8")
#     buf.close()
#     return img_base64

def analyse_friends(friend_arr, popularity_scores):
    # let's look in a row wise manner to begin with
    # each row represents a person. The row sum is the number of friends that person has.
    # the sum of each column for the values in the row which are 1 represents the sum of friends for each person that the original person is friends with.
    # return an array which has a row for each person, with a column denoting their number of friends, and a column denoting the mean number of friends of the original person's friends

    friend_comparisons = create_friend_comparison(friend_arr)
    person_mean, friend_mean = calculate_friend_means(friend_comparisons)
    print(f'person mean: {person_mean}')
    print(f'friend mean: {friend_mean}')
    return person_mean, friend_mean





