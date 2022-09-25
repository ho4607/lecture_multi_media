import numpy as np

def random_idx_idy():
    
    return

def shuffle_2D_matrix(matrix, seed, axis = 0):
    """
    Shuffle 2D matrix by column or row.
    
    Arguments:
    matrix: 2D matrix to be shuffled
    seed  : seed of numpy.random
    axis  : zero - by column, non-zero - by row
    
    Returns:
    shuffled_matrix: shuffled matrix
    """
    
    np.random.seed(seed)
    
    if axis == 0: # by column
        m = matrix.shape[1]
        permutation = list(np.random.permutation(m))
        shuffled_matrix = matrix[:, permutation]
    else:          # by row
        m = matrix.shape[0]
        permutation = list(np.random.permutation(m))
        shuffled_matrix = matrix[permutation, :]

    return shuffled_matrix