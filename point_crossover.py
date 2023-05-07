import numpy as np

def single_point_crossover(a: np.ndarray, b: np.ndarray, point: int) -> tuple[np.ndarray, np.ndarray]:
    
        #a: one-dimensional array, first parent
        #b: one-dimensional array, second parent
        #point: crossover point
        a,b = a.copy(),b.copy()
        point= point+1
        for i in range(point,len(a)):
            a[i],b[i] = b[i],a[i]       #swap the genetic information
       #a,b = ''.join(a),''.join(b)
        
        return a,b
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
    a,b = a.copy(),b.copy()
    a,b = single_point_crossover(a,b,first)
    a,b = single_point_crossover(a,b,second-1)
    return a,b

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
    

    a,b = a.copy(),b.copy()
    # Perform the crossover
    for i,point in enumerate(points):
        if i%2:
              point-=1
        a,b = single_point_crossover(a,b,point)
        
    return a,b


	
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
prep = lambda x: ' '.join(map(str, x))
print(*map(prep, single_point_crossover(a, b, 4)), '', sep='\n')
print(*map(prep, two_point_crossover(a, b, 2, 7)), '', sep='\n')
print(*map(prep, k_point_crossover(a, b, np.array([1, 5, 8]))), '', sep='\n')