"""
Zachary Noctor
CSCI 332 Spring 2025
Programming Assignment #2 JarvisConvexHull
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

from typing import List, Tuple

Point = Tuple[float, float]


def get_orientation(p1,p2,p3):
    ori = (p2[1]-p1[1])*(p3[0]-p2[0])-(p3[1]-p2[1])*(p2[0]-p1[0])
    if ori == 0:
        return  0 #"Collinear"
    elif ori > 0:
        return 1 #'Clockwise'
    else :
        return 2 #"Counter-clockwise"




def convex_hull_jarvis(points: List[Point]) -> List[Point]:
    # Remove duplicate points
    points = list(set(points))

    #a convex hull needs atleast three points
    n = len(points)
    if n < 3:
        return []

    start = points[0]
    start_idx = 0
    for i in range(n):
        if start[0] == max(start[0], points[i][0]):
            start = points[i]
            start_idx = i

    hull = []
    p = start_idx
    q = start_idx + 1
    while(True):

        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if get_orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q    

        if p == start_idx:
            break

    return hull

if __name__ == "__main__":
    points = [(0, 3), (0,3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)

#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]