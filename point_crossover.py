import numpy as np

def single_point_crossover(a: np.ndarray, b: np.ndarray, point: int) -> tuple[np.ndarray, np.ndarray]:
    
        #a: one-dimensional array, first parent
        #b: one-dimensional array, second parent
        #point: crossover point
        p1 = a
        p2 = b
        point= point+1
        for i in range(point,len(a)):
            p1[i],p2[i] = b[i],a[i]       #swap the genetic information
       #a,b = ''.join(a),''.join(b)
        
        return p1,p2
    #Return:
       # Two np.ndarray objects -- the offspring

        raise NotImplemetnedError()


def two_point_crossover(a: np.ndarray, b: np.ndarray, first: int, second: int) -> tuple[np.ndarray, np.ndarray]:
    """Performs two point crossover of `a` and `b` using `first` and `second` as crossover points.
    Chromosomes between `first` and `second` are swapped
    Args:
        a: one-dimensional array, first parent
        b: one-dimensional array, second parent
        first: first crossover point
        second: second crossover point
    Return:
        Two np.ndarray objects -- the offspring"""
    p1 = np.zeros(len(a), dtype=int)
    p2 = np.zeros(len(b), dtype=int)
    for i in range(len(a)):
        if i >= first+1 and i <= second-1:
            p1[i],p2[i] = b[i],a[i]
        else:
            p1[i],p2[i] = a[i],b[i]
    return p1,p2

    raise NotImplemetnedError()


def k_point_crossover(a: np.ndarray, b: np.ndarray, points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Performs k point crossover of `a` and `b` using `points` as crossover points.
    Chromosomes between each even pair of points are swapped
    Args:
        a: one-dimensional array, first parent
        b: one-dimensional array, second parent
        points: one-dimensional array, crossover points
    Return:
        Two np.ndarray objects -- the offspring"""
    # Initialize some variables
    p1 = a
    p2 = b
    left_point = 0
    right_point = 10 
    arr = []

    points = np.append(points, left_point)
    points = np.append(points, right_point)
    points = sorted(points)
    # Perform the crossover
    for i in range(len(points)-1):
        if i%2!=0 and i!=0:
            arr.append(points[i])
            arr.append(points[i+1])
    x = 0
    while x < len(arr)-1:
        p1,p2 = two_point_crossover(p1, p2, arr[x], arr[x+1])
        x+=2
    return p1,p2


	
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
prep = lambda x: ' '.join(map(str, x))
print(*map(prep, single_point_crossover(a, b, 4)), '', sep='\n')
print(*map(prep, two_point_crossover(a, b, 2, 7)), '', sep='\n')
print(*map(prep, k_point_crossover(a, b, np.array([1, 5, 8]))), '', sep='\n')