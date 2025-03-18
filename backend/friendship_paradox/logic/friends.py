import numpy as np

def make_arr_symmetric(arr):
    return np.tril(arr) + np.triu(arr.T, 1)

def normal_friends(size: int, popularity_mean = 0.5, popularity_std = 0.15):
    popularity_scores = np.random.normal(popularity_mean, popularity_std, size)
    popularity_scores = np.clip(popularity_scores, a_min=0, a_max=1)
    popularity_matrix = np.outer(popularity_scores, popularity_scores)

    rand_matrix = np.random.rand(size, size)
    friend_arr = (rand_matrix < popularity_matrix).astype(int)
    return friend_arr

def make_friends(size: int, normal = False):
    friend_arr = np.random.choice((0,1), size=(size, size))
    if normal:
        friend_arr = normal_friends(size = size)
    friend_arr = make_arr_symmetric(friend_arr)
    np.fill_diagonal(friend_arr, 0)
    return friend_arr


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


def analyse_friends(friend_arr):
    # let's look in a row wise manner to begin with
    # each row represents a person. The row sum is the number of friends that person has.
    # the sum of each column for the values in the row which are 1 represents the sum of friends for each person that the original person is friends with.
    # return an array which has a row for each person, with a column denoting their number of friends, and a column denoting the mean number of friends of the original person's friends

    friend_comparisons = create_friend_comparison(friend_arr)
    person_mean, friend_mean = calculate_friend_means(friend_comparisons)
    print(f'person mean: {person_mean}')
    print(f'friend mean: {friend_mean}')
    return person_mean, friend_mean



