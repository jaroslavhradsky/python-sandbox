# Pure Python
points = [[9,2,8],[4,7,2],[3,4,4],[5,6,9],[5,0,7],[8,2,7],[0,3,2],[7,3,0],[6,1,1],[2,9,6]]
qPoint = [4,5,3]
minIdx = -1
minDist = -1
for idx, point in enumerate(points):  # iterate over all points
    dist = sum([(dp-dq)**2 for dp,dq in zip(point,qPoint)])**0.5  # compute the euclidean distance for each point to q
    if dist < minDist or minDist < 0:  # if necessary, update minimum distance and index of the corresponding point
        minDist = dist
        minIdx = idx

print('Nearest point to q: {0}'.format(points[minIdx]))

# Equivalent NumPy vectorization 
import numpy as np
points = np.array([[9,2,8],[4,7,2],[3,4,4],[5,6,9],[5,0,7],[8,2,7],[0,3,2],[7,3,0],[6,1,1],[2,9,6]])
qPoint = np.array([4,5,3])
minIdx = np.argmin(np.linalg.norm(points-qPoint,axis=1))  # compute all euclidean distances at once and return the index of the smallest one
print('Nearest point to q: {0}'.format(points[minIdx]))
