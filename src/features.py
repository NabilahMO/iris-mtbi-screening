import numpy as np # pyright: ignore[reportMissingImports]

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def compute_inter_iris_distance(left_mid, right_mid):
    return euclidean_distance(left_mid, right_mid)


def compute_iris_diameter(inner, outer):
    return euclidean_distance(inner, outer)


def compute_average_diameter(left_inner, left_outer, right_inner, right_outer):
    left_diameter = compute_iris_diameter(left_inner, left_outer)
    right_diameter = compute_iris_diameter(right_inner, right_outer)
    return (left_diameter + right_diameter) / 2


def normalise_distance(inter_iris_distance, avg_diameter):
    if avg_diameter == 0 or avg_diameter is None:
        return None  # or np.nan
    return inter_iris_distance / avg_diameter


def compute_time_series_std(norm_dist_series):
    return np.std(norm_dist_series)


def flag_mTBI(std_dev, threshold=0.1):
    return std_dev > threshold

