import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}

    # computing the matrix from the list
    array = np.array(list)
    matrix = array.reshape(3, 3)

    #computing the means
    mean_on_axis0 = np.mean(matrix, axis=0)
    mean_on_axis1 = np.mean(matrix, axis=1)

    #computing the mean of means
    matrix_mean = np.mean(array)

    #computing the lists back
    list_mean_0 = np.ndarray.tolist(mean_on_axis0)
    list_mean_1 = np.ndarray.tolist(mean_on_axis1)

    calculations.update({"mean": [list_mean_0, list_mean_1, matrix_mean]})

    #computing the variance
    variance_on_axis0 = np.var(matrix, axis=0)
    variance_on_axis1 = np.var(matrix, axis=1)

    #computing the variance of variances
    matrix_variance = np.var(array)

    #computing the lists back
    list_variance_0 = np.ndarray.tolist(variance_on_axis0)
    list_variance_1 = np.ndarray.tolist(variance_on_axis1)

    calculations.update({"variance": [list_variance_0, list_variance_1, matrix_variance]})


    #computing the standard deviation
    std_on_axis0 = np.std(matrix, axis=0)
    std_on_axis1 = np.std(matrix, axis=1)

    #computing the std of stds
    matrix_std = np.std(array)

    #computing the lists back
    list_std_0 = np.ndarray.tolist(std_on_axis0)
    list_std_1 = np.ndarray.tolist(std_on_axis1)

    calculations.update({"standard deviation": [list_std_0, list_std_1, matrix_std]})

    #computing the max
    max_on_axis0 = np.max(matrix, axis=0)
    max_on_axis1 = np.max(matrix, axis=1)

    #computing the max of maxs
    matrix_max = np.max(array)

    #computing the lists back
    list_max_0 = np.ndarray.tolist(max_on_axis0)
    list_max_1 = np.ndarray.tolist(max_on_axis1)

    calculations.update({"max": [list_max_0, list_max_1, matrix_max]})

    # computing the min
    min_on_axis0 = np.min(matrix, axis=0)
    min_on_axis1 = np.min(matrix, axis=1)

    # computing the min of mins
    matrix_min = np.min(array)

    # computing the lists back
    list_min_0 = np.ndarray.tolist(min_on_axis0)
    list_min_1 = np.ndarray.tolist(min_on_axis1)

    calculations.update({"min": [list_min_0, list_min_1, matrix_min]})


    # computing the sum
    sum_on_axis0 = np.sum(matrix, axis=0)
    sum_on_axis1 = np.sum(matrix, axis=1)

    # computing the sum of sums
    matrix_sum = np.sum(array)

    # computing the lists back
    list_sum_0 = np.ndarray.tolist(sum_on_axis0)
    list_sum_1 = np.ndarray.tolist(sum_on_axis1)

    calculations.update({"sum": [list_sum_0, list_sum_1, matrix_sum]})

    return calculations

