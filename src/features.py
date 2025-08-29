import numpy as np # pyright: ignore[reportMissingImports]
""" imports NumPy, needed for calculations """

def euclidean_distance(p1, p2):
    """
    def starts a function. 
    The function euclidean_distance(p1, p2) returns the straight-line 
    distance between p1(x1, y1) and p2(x2, y2) in 2D space. 
    """
    return np.linalg.norm(np.array(p1) - np.array(p2))
"""
    Converts both input points to NumPy arrays
	Subtracts one from the other to get a vector
	np.linalg.norm function returns the length of that vector (distance)
"""

def compute_inter_iris_distance(left_mid, right_mid):
    """the function above computes the distance between left and right 
    iris centers using the prestated formula: 
    np.linalg.norm(np.array(p1) - np.array(p2))"""
    return euclidean_distance(left_mid, right_mid)


def compute_iris_diameter(inner, outer):
    """Compute the diameter of an iris from inner and outer landmarks
    using the same prestated formula"""
    return euclidean_distance(inner, outer)


def compute_average_diameter(left_inner, left_outer, right_inner, right_outer):
    """Calsculates the average of both irises' diameters."""
    left_diameter = compute_iris_diameter(left_inner, left_outer)
    right_diameter = compute_iris_diameter(right_inner, right_outer)
    return (left_diameter + right_diameter) / 2


def normalise_distance(inter_iris_distance, avg_diameter):
    """Returns a normalised version of the inter-iris distance."""
    if avg_diameter == 0 or avg_diameter is None:
        return None  # or np.nan
    return inter_iris_distance / avg_diameter


def compute_time_series_std(norm_dist_series):
    """Compute the standard deviation of a list/array of normalised distances."""
    return np.std(norm_dist_series)


def flag_mTBI(std_dev, threshold=0.1):
    """Return True if user is likely to have mTBI based on threshold."""
    return std_dev > threshold

