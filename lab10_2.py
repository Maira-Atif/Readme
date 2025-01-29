import numpy as np
from collections import Counter

# Given dataset
dataset = [
    (1, 1, 'A'),
    (2, 2, 'A'),
    (3, 3, 'B'),
    (4, 4, 'B'),
    (5, 5, 'B')
]

# New data point
new_point = (3, 3)

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = []
for point in dataset:
    dist = euclidean_distance(new_point, (point[0], point[1]))
    distances.append((dist, point[2]))

# Sort distances and find k-nearest neighbors (k=3)
k = 3
distances.sort()
k_nearest = distances[:k]

# Determine the majority class
classes = [neighbor[1] for neighbor in k_nearest]
most_common_class = Counter(classes).most_common(1)[0][0]

print("3 Nearest Neighbors:", k_nearest)
print("Classified as:", most_common_class)
