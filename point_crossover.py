import numpy as np

def single_point_crossover(a: np.ndarray, b: np.ndarray, point: int) -> tuple[np.ndarray, np.ndarray]:
    
        #a: one-dimensional array, first parent
        #b: one-dimensional array, second parent
        #point: crossover point
        p1 = list(a)
        p2 = list(b)
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
    p1 = a
    p2 = b
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
child_a = ''
child_b = ''
last_point = 0  # Initialize last_point as an integer
point_count = 0

# Perform the crossover
for point in points:
    # Convert point to integer if it's not already one
    if not isinstance(point, int):
        point = int(point)

    # Swap the chromosomes between each even pair of points
    if point_count % 2 == 0:
        child_a += a[last_point:point] + b[last_point:point]
        child_b += b[last_point:point] + a[last_point:point]
    else:
        child_a += b[last_point:point] + a[last_point:point]
        child_b += a[last_point:point] + b[last_point:point]

    # Update the variables
    last_point = point
    point_count += 1

# Add the remaining chromosomes
if point_count % 2 == 0:
    child_a += a[last_point:]
    child_b += b[last_point:]
else:
    child_a += b[last_point:]
    child_b += a[last_point:]

    raise NotImplemetnedError()
	
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
prep = lambda x: ' '.join(map(str, x))
print(*map(prep, single_point_crossover(a, b, 4)), '', sep='\n')
print(*map(prep, two_point_crossover(a, b, 2, 7)), '', sep='\n')
print(*map(prep, k_point_crossover(a, b, np.array([1, 5, 8]))), '', sep='\n')
            
