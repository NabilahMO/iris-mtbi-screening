import numpy as np 
""" imports NumPy, a numerical library used to do math with arrays and 
vectors which will be needed for the Euclidean distance calculations """

def euclidean_distance(p1, p2):
    """
    def starts a function. 
    
    The function euclidean_distance(p1, p2) returns the straight-line 
    distance between two points in 2D space.  p1 and p2 are two 2D points, 
    like (x, y). 
    
    Each point is converted to a NumPy array labelled 
    np.array(p1). 
    
    By subtracting the vectors, it gives a difference vector. 
    np.linalg.norm(np.array(p1) - np.array(p2)) is an array formed as a 
    result of computing np.array(p1) - np.array(p2)).
    """
    return np.linalg.norm(np.array(p1) - np.array(p2))


def compute_inter_iris_distance(left_mid, right_mid):
    """the function above computes the distance between left and right 
    iris centers using the prestated formula: 
    np.linalg.norm(np.array(p1) - np.array(p2))"""
    return euclidean_distance(left_mid, right_mid)


def compute_iris_diameter(inner, outer):
    """Compute the diameter of an iris from inner and outer landmarks
    using the prestated formula: 
    np.linalg.norm(np.array(p1) - np.array(p2))"""
    return euclidean_distance(inner, outer)


def compute_average_diameter(left_inner, left_outer, right_inner, right_outer):
    """Compute average of both irises' diameters."""
    left_diameter = compute_iris_diameter(left_inner, left_outer)
    right_diameter = compute_iris_diameter(right_inner, right_outer)
    return (left_diameter + right_diameter) / 2


def normalise_distance(inter_iris_distance, avg_diameter):
    """Normalise the inter-iris distance by average diameter."""
    if avg_diameter == 0:
        return np.nan  # or raise an exception
    return inter_iris_distance / avg_diameter


def compute_time_series_std(norm_dist_series):
    """Compute the standard deviation of a list/array of normalised distances."""
    return np.std(norm_dist_series)


def flag_mTBI(std_dev, threshold=0.1):
    """Return True if user is likely to have mTBI based on threshold."""
    return std_dev > threshold
